"""Download FAO consumer prices, food indices (2015 = 100, monthly) from World Bank Data360."""
from data360_client import save_indicator

if __name__ == "__main__":
    save_indicator("FAO_CP", "FAO_CP_23013", "Consumer prices, food indices (2015 = 100)")
