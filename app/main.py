"""
Streamlit frontend for NASA's Near Earth Object (NEO) API.
Implements a scatter plot and a table view for daily NEO data.
I used Gemini 2.0 Flash Thinking for help with debugging.
"""

import streamlit as st
from datetime import date, timedelta
from data import get_data
import pandas as pd
import altair as alt

st.set_page_config(page_title="Near Earth Objects", page_icon=":comet:")
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["NEO Scatter Plot", "NEO Table"])

today = date.today().strftime("%Y-%m-%d")

# Initialize session state date if not set
if "current_date" not in st.session_state:
    st.session_state.current_date = today

# Get data from NEO API for current date
current_date = st.session_state.current_date
neo_data = get_data(current_date)

st.header(f"Near Earth Objects for {current_date}")

if page == "NEO Scatter Plot":
    # Check if data is available
    if neo_data and "near_earth_objects" in neo_data and current_date in neo_data["near_earth_objects"]:
        # Check if there are any NEOs for current date
        neos = neo_data["near_earth_objects"][current_date]
        if neos:
            # Format NEO data for scatter plot
            neo_list = []
            for neo in neos:
                diameter_min = float(neo["estimated_diameter"]["miles"]["estimated_diameter_min"])
                diameter_max = float(neo["estimated_diameter"]["miles"]["estimated_diameter_max"])
                diameter_avg = (diameter_min + diameter_max) / 2
                miss_distance = float(neo["close_approach_data"][0]["miss_distance"]["miles"])
                is_hazardous = "Yes" if neo["is_potentially_hazardous_asteroid"] else "No"

                neo_list.append({
                    "diameter_avg": diameter_avg,
                    "miss_distance": miss_distance,
                    "is_hazardous": is_hazardous
                })
            df = pd.DataFrame(neo_list)

            chart = alt.Chart(df).mark_circle().encode(
                x=alt.X("diameter_avg:Q", title="Estimated Diameter (miles)"),
                y=alt.Y("miss_distance:Q", title="Miss Distance (miles)"),
                color=alt.Color("is_hazardous:N", 
                                scale=alt.Scale(domain=["Yes", "No"], range=["red", "green"]), 
                                title="Is Potentially Hazardous?"),
                tooltip=["diameter_avg", "miss_distance", "is_hazardous"]
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write(f"No Near Earth Objects found for {current_date}.")
    else:
        st.write("Failed to fetch Near Earth Object data.")
elif page == "NEO Table":
    # Check if data is available
    if neo_data and "near_earth_objects" in neo_data and current_date in neo_data["near_earth_objects"]:
        # Check if there are any NEOs for current date
        neos = neo_data["near_earth_objects"][current_date]
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
                    "Is Potentially Hazardous?": is_hazardous
                })

            df = pd.DataFrame(neo_list)
            st.table(df)
        else:
            st.write(f"No Near Earth Objects found for {current_date}.")
    else:
        st.write("Failed to fetch Near Earth Object data.")

# Date navigation
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Previous Day"):
        previous_date = (date.fromisoformat(current_date) - timedelta(days=1)).strftime("%Y-%m-%d")
        st.session_state.current_date = previous_date
        st.rerun()

with col2:
    if st.button("Today"):
        st.session_state.current_date = today
        st.rerun()

with col3:
    if st.button("Next Day"):
        next_date = (date.fromisoformat(current_date) + timedelta(days=1)).strftime("%Y-%m-%d")
        st.session_state.current_date = next_date
        st.rerun()