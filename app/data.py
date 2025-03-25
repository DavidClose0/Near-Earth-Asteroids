import requests
import json

def get_data(date: str) -> dict:
    """
    Gets data from Neo API for a given date.
    Args:
        date (str): Date in YYYY-MM-DD format.
    Returns:
        dict: Dictionary containing data from Neo API.
    """
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key=DEMO_KEY"

    try:
        data = requests.get(url, timeout=10).json()
        return data
    except Exception as e:
        print(f"Error getting data: {e}")
        return {}
    
data = get_data("2025-03-24")
with open("app\data.json", "w") as f:
    json.dump(data, f, indent=4)