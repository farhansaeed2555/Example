import streamlit as st
import time
from datetime import datetime, timedelta
from playsound import playsound     # Import playsound library for playing audio

# Define function to play alarm sound 
def play_alarm_sound():
    playsound("sound.wav")

# Set page configration
st.set_page_config(
    page_title="Alarm Clock",
    page_icon=":alarm_clock:",
    layout="centered"
)

# Page Title and Description
st.title("Alarm Clock")
st.write("Bano Qabil")
st.write("Campus: Pakistan Central Homeopathic College")
st.write("Day: Monday & Wednesday")
st.write("Timing: 08 to 10")
st.write("Sir Name: Gufran KamalUddin")
st.write("Create a personalized alarm clock project with date and sound features using Streamlit. Allow users to set alarms by selecting a date and time. Additionally, implement a snooze functionality to provide users with the option to delay alarms, adding flexibility to their morning routines.")

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
        current_time = time.localtime()
        if current_time.tm_hour == alarm_time.hour and current_time.tm_min ==alarm_time.minute:
            st.write("Wake up! Its time!")
            play_alarm_sound()  # Play alarm sound
            snooze_time = current_time.tm_min + snooze_duration
            break
        time.sleep(1)  # Check every minute

    while True:
        current_time = time.localtime()
        if current_time.tm_min == snooze_time % 60 and current_time.tm_hour == alarm_time.hour:
            st.write("Snooze time's up!")
            play_alarm_sound()  # Play alarm sound
            snooze_time = current_time.tm_min + snooze_duration
        time.sleep(1)   # Check every minute

        