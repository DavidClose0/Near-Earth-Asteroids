import streamlit as st
from datetime import date
from data import get_data
import pandas as pd

st.set_page_config(page_title="Near Earth Objects", page_icon=":comet:")

today = date.today().strftime("%Y-%m-%d")
neo_data = get_data(today)

st.header(f"Near Earth Objects for {today}")

# Check if data is available
if neo_data and "near_earth_objects" in neo_data and today in neo_data["near_earth_objects"]:
    # Check if there are any NEOs for today's date
    neos = neo_data["near_earth_objects"][today]
    if neos:
        # Format NEO data for table
        neo_list = []
        for neo in neos:
            name_link = f"[{neo['name']}]({neo['nasa_jpl_url']})"
            diameter_min = round(neo["estimated_diameter"]["miles"]["estimated_diameter_min"], 2)
            diameter_max = round(neo["estimated_diameter"]["miles"]["estimated_diameter_max"], 2)
            diameter = f"{diameter_min} - {diameter_max}"
            miss_distance = (float(neo["close_approach_data"][0]["miss_distance"]["miles"]))
            miss_distance_formatted = f"{miss_distance:.2e}"
            is_hazardous = "Yes" if neo["is_potentially_hazardous_asteroid"] else "No"

            neo_list.append({
                "Name": name_link,
                "Estimated Diameter (miles)": diameter,
                "Miss Distance (miles)": miss_distance_formatted,
                "Is Potentially Hazardous": is_hazardous
            })

        df = pd.DataFrame(neo_list)
        st.table(df)
    else:
        st.write(f"No Near Earth Objects found for {today}.")
else:
    st.write("Failed to fetch Near Earth Object data.")