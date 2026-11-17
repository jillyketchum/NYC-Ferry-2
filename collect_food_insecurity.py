"""Download FAO moderately or severely food insecure people (million, 3-year average) from World Bank Data360."""
from data360_client import save_indicator

if __name__ == "__main__":
    save_indicator("FAO_FS", "FAO_FS_210081", "Moderately or severely food insecure people (million) (3-year average)")
