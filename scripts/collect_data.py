"""Download all three FAO indicators from the World Bank Data360 API.

Usage: python scripts/collect_data.py

Saves each dataset to data/raw/<INDICATOR_ID>.csv plus a provenance file
(<INDICATOR_ID>_provenance.json) recording the source, license, and download time.

API: GET https://data360api.worldbank.org/data360/data?DATABASE_ID=...&INDICATOR=...&skip=N
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

DATASETS = [
    {"database_id": "FAO_CP", "indicator_id": "FAO_CP_23014",
     "label": "Food price inflation", "license": "CC BY 4.0"},
    {"database_id": "FAO_CP", "indicator_id": "FAO_CP_23013",
     "label": "Consumer prices, food indices (2015 = 100)", "license": "CC BY 4.0"},
    {"database_id": "FAO_FS", "indicator_id": "FAO_FS_210081",
     "label": "Moderately or severely food insecure people (million) (3-year average)",
     "license": "CC BY-NC-SA 3.0 IGO"},
]


def fetch_indicator(database_id, indicator_id):
    """Download every row for one indicator, following pagination."""
    rows, skip, total = [], 0, None
    while True:
        params = {"DATABASE_ID": database_id, "INDICATOR": indicator_id, "skip": skip}
        for attempt in range(3):
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
def save_dataset(ds):
    """Download one dataset and save the CSV and provenance file to data/raw/."""
    print(f"Downloading {ds['label']} ({ds['indicator_id']})...")
    df = fetch_indicator(ds["database_id"], ds["indicator_id"])
    if df.empty:
        raise RuntimeError(f"No data returned for {ds['indicator_id']}")

    out = RAW_DIR / f"{ds['indicator_id']}.csv"
    df.to_csv(out, index=False)

    provenance = {
        "dataset": ds["label"],
        "indicator_id": ds["indicator_id"],
        "database_id": ds["database_id"],
        "source_page": f"https://data360.worldbank.org/en/indicator/{ds['indicator_id']}",
        "api_request": f"{API_URL}?DATABASE_ID={ds['database_id']}&INDICATOR={ds['indicator_id']}",
        "producer": "Food and Agriculture Organization of the United Nations (FAO)",
        "distributor": "World Bank Data360",
        "license": ds["license"],
        "downloaded_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "rows": len(df),
    }
    (RAW_DIR / f"{ds['indicator_id']}_provenance.json").write_text(json.dumps(provenance, indent=2))
    print(f"Saved {len(df):,} rows -> {out}\n")


if __name__ == "__main__":
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for ds in DATASETS:
        save_dataset(ds)
    print("Done. All datasets saved to", RAW_DIR)
