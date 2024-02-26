import streamlit as st
import time
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Alarm Clock",
    page_icon=":alarm_clock:",
    layout="wide"
)

# Page Title and Description
st.title("Alarm Clock")
st.write("Bano Qabil")
st.write("Campus: Pakistan Central Homeopathic College")
st.write("Day: Monday & Wednesday")
st.write("Timing: 08 to 10")
st.write("Sir Name: Gufran KamalUddin")
st.write("Create a personalized alarm clock project with date and sound features using Streamlit. Allow users to set alarms by selecting a date and time. Additionally, implement a snooze functionality to provide users with the option to delay alarms, adding flexibility to their morning routines.")

# Add tabs
tabs = ["Set Alarm", "About"]
selected_tab = st.sidebar.radio("Tabs", tabs)

if selected_tab == "Set Alarm":
    # Get user input for the alarm date
    alarm_date = st.date_input("Set alarm date")

    # Set Alarm Time 
    alarm_time = st.time_input("Set Alarm Time")

    # Combine the selected date and time into a single datetime object
    alarm_datetime = datetime.combine(alarm_date, alarm_time)

    # Set Snooze Duration
    snooze_duration = st.slider("Snooze Duration (minutes)", 1, 60, 5)

    # Start Alarm Button
    if st.button("Start Alarm"):
        st.write(f"Alarm set for {alarm_datetime}")
        while True:
            current_time = datetime.now()
            if current_time >= alarm_datetime:
                st.write("Wake up! It's time!")
                break
            time.sleep(1)  # Check every second

        while True:
            current_time = datetime.now()
            if current_time >= alarm_datetime + timedelta(minutes=snooze_duration):
                st.write("Snooze time's up!")
                break
            time.sleep(1)  # Check every second

elif selected_tab == "About":
    st.write("This is a simple alarm clock application built with Streamlit.")
    st.write("It allows users to set alarms and provides a snooze functionality.")
    st.write("Developed by [Your Name]")
