import time
import requests

# Federal spending API link
BASE_URL = "https://api.usaspending.gov/api/v2/search/spending_by_award/"

# Codes for various types of purchases
CONTRACT_AWARD_TYPES = ["A", "B", "C", "D"]

# Fields requested from API
FIELDS = [
    "Award ID",
    "Recipient Name",
    "Recipient UEI",
    "Start Date",
    "End Date",
    "Award Amount",
    "Total Outlays",
    "Awarding Agency",
    "Awarding Sub Agency",
    "Funding Agency",
    "Funding Sub Agency",
    "Award Type",
    "Contract Award Type",
    "NAICS",
    "PSC",
    "Place of Performance State Code",
    "Place of Performance Country Code",
    "Last Modified Date",
    "generated_internal_id",
]

# Minimum contract spend to fetch
SPEND_FLOOR = 100_000_000


# Function to fetch awards
def fetch_awards(start_date: str, end_date: str, page_limit: int = 100) -> list[dict]:
    """Return all contract award records in [start_date, end_date]"""
    results: list[dict] = []
    page = 1
    while True:
        body = {
            "subawards": False,
            "limit": page_limit,
            "page": page,
            "filters": {
                "award_type_codes": CONTRACT_AWARD_TYPES,
                "time_period": [{"start_date": start_date, "end_date": end_date}],
                "award_amounts": [{"lower_bound": SPEND_FLOOR}]
            },
            "fields": FIELDS
        }

        response = requests.post(BASE_URL, json=body, timeout=60)
        response.raise_for_status()
        # Convert response into python objects
        payload = response.json()
        # Add the response (list of dicts - dicts are rows in the data) to the results
        results.extend(payload.get("results", []))

        # Print statement to check responses
        ###has_next = payload.get("page_metadata", {}).get("hasNext")
        ###print(f"page {page}: got {len(payload.get('results', []))} rows, hasNext={has_next}")

        # Break if no more pages remain
        if not payload.get("page_metadata").get("hasNext"):
            print
            break
        page += 1
        time.sleep(0.3)
    return results
