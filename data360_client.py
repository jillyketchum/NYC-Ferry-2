"""Shared helper for downloading one indicator from the World Bank Data360 API.

API base: https://data360api.worldbank.org
Endpoint:  GET /data360/data?DATABASE_ID=...&INDICATOR=...&skip=N
Responses are paginated JSON: {"count": <total rows>, "value": [<row>, ...]}.
"""
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

API_URL = "https://data360api.worldbank.org/data360/data"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
LICENSES = {
    "FAO_CP_23014": "CC BY 4.0",
    "FAO_CP_23013": "CC BY 4.0",
    "FAO_FS_210081": "CC BY-NC-SA 3.0 IGO",
}


def fetch_indicator(database_id: str, indicator_id: str, page_size: int = 1000) -> pd.DataFrame:
    """Download every row for one indicator, following pagination."""
    rows, skip, total = [], 0, None
    while True:
        params = {"DATABASE_ID": database_id, "INDICATOR": indicator_id, "skip": skip}
        for attempt in range(3):  # retry on temporary network errors
            try:
                resp = requests.get(API_URL, params=params, timeout=60)
                resp.raise_for_status()
                break
            except requests.RequestException as err:
                if attempt == 2:
                    raise
                print(f"  retrying after error: {err}")
                time.sleep(2 ** attempt)
        payload = resp.json()
        page = payload.get("value", [])
        total = payload.get("count", total)
        if not page:
            break
        rows.extend(page)
        skip += len(page)
        print(f"  {indicator_id}: {len(rows):,} / {total or '?'} rows")
        if total is not None and len(rows) >= total:
            break
    return pd.DataFrame(rows)


def save_indicator(database_id: str, indicator_id: str, label: str) -> Path:
    """Download an indicator and save it to data/raw/, with a provenance record."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    df = fetch_indicator(database_id, indicator_id)
    if df.empty:
        raise RuntimeError(f"No data returned for {indicator_id}")
    out = RAW_DIR / f"{indicator_id}.csv"
    df.to_csv(out, index=False)

    provenance = {
        "dataset": label,
        "indicator_id": indicator_id,
        "database_id": database_id,
        "source_page": f"https://data360.worldbank.org/en/indicator/{indicator_id}",
        "api_request": f"{API_URL}?DATABASE_ID={database_id}&INDICATOR={indicator_id}",
        "producer": "Food and Agriculture Organization of the United Nations (FAO)",
        "distributor": "World Bank Data360",
        "license": LICENSES.get(indicator_id, "see Data360 metadata"),
        "downloaded_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "rows": len(df),
    }
    (RAW_DIR / f"{indicator_id}_provenance.json").write_text(json.dumps(provenance, indent=2))
    print(f"Saved {len(df):,} rows -> {out}")
    return out
