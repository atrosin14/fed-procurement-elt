import json
from datetime import date, timedelta
from pathlib import Path

# Local import
from extract.client import fetch_awards

# Create a path object for the raw data landing location
RAW_DIR = Path("data/raw")

def run_extraction(lookback_days: int=7) -> Path:
    """Run the fetch_awards function for a set time range and store the results"""

    # Establish the start and end date range
    end = date.today()
    start = end - timedelta(days=lookback_days)

    # Run the fetch
    records = fetch_awards(start.isoformat(), end.isoformat())

    # Create the landing directory if it doesn't exist
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    # Establish the path to write to
    out_path = RAW_DIR / f"awards_{end.isoformat()}.json"
    out_path.write_text(json.dumps(records, indent=2))

    print(f"Fetched {len(records)} awards for {start}..{end} -> {out_path}")

if __name__ == "__main__":
    run_extraction()
