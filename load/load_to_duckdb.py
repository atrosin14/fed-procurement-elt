import sys
from pathlib import Path
import duckdb

DB_PATH = "warehouse.duckdb"

def load(json_path: str) -> int:
    """Loads raw data..."""
    con = duckdb.connect(DB_PATH)
    con.execute("CREATE SCHEMA IF NOT EXISTS raw;")

    # Create the table from the .json files inferred schema, don't populate with rows yet
    con.execute(f"""
            CREATE TABLE IF NOT EXISTS raw.awards AS
            SELECT * FROM read_json_auto('{json_path}') LIMIT 0;
    """)

    # Insert only rows where award ID is not yet present
    con.execute(f"""
        INSERT INTO raw.awards
        SELECT * FROM read_json_auto('{json_path}') src
        WHERE src."Award ID" NOT IN (SELECT "Award ID" FROM raw.awards);
    """)

    count = con.execute("SELECT COUNT(*) FROM raw.awards;").fetchone()[0]
    con.close()
    print(f"Loaded {json_path}: raw.awards now has {count} rows.")
    return count

if __name__ == "__main__":
    load(sys.argv[1])
