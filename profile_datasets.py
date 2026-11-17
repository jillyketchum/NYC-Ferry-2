"""Exploratory quality profile of the three FAO / World Bank Data360 datasets.

Usage: python scripts/profile_datasets.py <food_insecurity.csv> <food_cpi.csv> <food_inflation.csv>
Prints accuracy, completeness, timeliness and consistency checks used in StatusReport.md.
"""
import sys
import pandas as pd

fs_path, cpi_path, inf_path = sys.argv[1:4]
fs = pd.read_csv(fs_path, dtype=str)
cpi = pd.read_csv(cpi_path, dtype=str)
inf = pd.read_csv(inf_path, dtype=str)

for name, df in [("Food insecurity", fs), ("Food CPI", cpi), ("Food inflation", inf)]:
    vals = pd.to_numeric(df.OBS_VALUE, errors="coerce")
    print(f"\n== {name}: {len(df):,} rows, {df.REF_AREA.nunique()} countries")
    print("  Period:", df.TIME_PERIOD.min(), "to", df.TIME_PERIOD.max(), "| freq:", df.FREQ_LABEL.unique())
    print("  Missing values:", int(vals.isna().sum()), "| OBS_STATUS:", df.OBS_STATUS_LABEL.value_counts().to_dict())
    print("  Constant (droppable) columns:", sum(df[c].nunique(dropna=False) == 1 for c in df.columns))

# Food insecurity: sex breakdown creates duplicate country-years
print("\nFood insecurity rows by sex:", fs.SEX_LABEL.value_counts().to_dict())
fs_t = fs[fs.SEX == "_T"].copy()
print("Duplicate country-years after keeping SEX == _T:", fs_t.duplicated(["REF_AREA", "TIME_PERIOD"]).sum())
print("Countries reporting per year:", fs_t.groupby("TIME_PERIOD").REF_AREA.nunique().to_dict())
yrs = fs_t.TIME_PERIOD.nunique()
print("Countries with all", yrs, "years:", (fs_t.groupby("REF_AREA").TIME_PERIOD.nunique() == yrs).sum())

# Country overlap (join feasibility)
a, b, c = set(fs_t.REF_AREA), set(cpi.REF_AREA), set(inf.REF_AREA)
print("\nCountries in all three datasets:", len(a & b & c), "| in food insecurity only:", sorted(a - b - c))

# Is inflation derived from the CPI? (consistency / redundancy)
c2 = cpi.assign(v=pd.to_numeric(cpi.OBS_VALUE), t=pd.PeriodIndex(cpi.TIME_PERIOD, freq="M"))
c2 = c2.sort_values(["REF_AREA", "t"])
c2["yoy"] = c2.groupby("REF_AREA").v.pct_change(12) * 100
m = c2.merge(inf.assign(i=pd.to_numeric(inf.OBS_VALUE)), on=["REF_AREA", "TIME_PERIOD"]).dropna(subset=["yoy", "i"])
print("Share of inflation values equal to YoY % change in CPI (±0.05):", round(((m.yoy - m.i).abs() < 0.05).mean(), 4))

# Extreme values (accuracy / outliers)
iv = pd.to_numeric(inf.OBS_VALUE, errors="coerce")
print("\nInflation range:", iv.min(), "to", iv.max())
print("Country-months with inflation > 100%:", inf[iv > 100].REF_AREA_LABEL.value_counts().head(8).to_dict())
