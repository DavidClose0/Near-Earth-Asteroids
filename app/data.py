import streamlit as st
import requests

@st.cache_data(ttl=60)  # Cache data for 1 minute
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
        st.error(f"Error getting data: {e}")
        return {}