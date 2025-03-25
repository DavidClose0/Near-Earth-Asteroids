"""
This module contains a function to get data from the Neo API.
"""
import os
import streamlit as st
import requests

@st.cache_data(ttl=3600)  # Cache data for 1 hour
def get_data(date: str) -> dict:
    """
    Gets data from Neo API for a given date.
    Args:
        date (str): Date in YYYY-MM-DD format.
    Returns:
        dict: Dictionary containing data from Neo API.
    """
    api_key = os.environ["API_KEY"]
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={api_key}"

    try:
        data = requests.get(url, timeout=10).json()
        return data
    except Exception as e:
        st.error(f"Error getting data: {e}")
        return {}