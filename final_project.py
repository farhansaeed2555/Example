import streamlit as st
import time
from datetime import datetime, timedelta
from playsound import playsound

def play_alarm_sound():
    playsound("sound.wav")

st.set_page_config(
    page_title="Alarm Clock",
    page_icon=":alarm_clock:",
    layout="centered"
)

# Sidebar Navigation
sidebar_selection = st.sidebar.radio("Navigation", ["Home", "Project", "Contact Us", "About Us"])

if sidebar_selection == "Home":
    st.image("BANO QABIL LOGO 1.jpg")
    st.title("Bano Qabil 2.0")
    st.write("Welcome to Python Final Project")

elif sidebar_selection == "Project":
    st.title("Alarm Clock Project")
    st.write("Create a personalized alarm clock project with date and sound features using Streamlit. "
             "Allow users to set alarms by selecting a date and time. Additionally, implement a snooze functionality "
             "to provide users with the option to delay alarms, adding flexibility to their morning routines.")

    # Get user input for the alarm date
    alarm_date = st.date_input("Set alarm date")

    # Set Alarm Time 
    alarm_time = st.time_input("Set Alarm Time")

    # Combine the selected date and time into a single datetime object
    alarm_datetime = datetime.combine(alarm_date, alarm_time)

    # Set Snooze Duration
    snooze_duration = st.slider("Snooze Duration (minutes)", 1, 60, 5)

elif sidebar_selection == "Contact Us":
    st.title("Contact Us")
    st.write("Group Leader: Farhan Saeed")
    st.write("Member NO.2: Wajahat Shaikh")
    st.write("Member No.3: Umer Farooq")

elif sidebar_selection == "About Us":
    st.title("Discription:")
    st.write("Welcome to the Streamlit Alarm Clock project! This application is designed to provide a personalized and flexible alarm experience for users. Developed using Streamlit, a powerful Python library for creating web applications, this project allows you to set alarms, choose specific dates and times, and even incorporate a snooze feature for added convenience.")
    st.title("Features:")
    st.write("1. Customizable Alarms")
    st.write("Set your alarms by selecting a date and time that suits your schedule. Whether it's for waking up in the morning, reminding you of an important event, or any other time-sensitive tasks, this alarm clock is tailored to your needs.")
    st.write("2. Snooze Functionality")
    st.write("Not ready to wake up immediately? No problem! The snooze functionality lets you delay alarms by a specified duration, providing flexibility to your morning routine.")
    st.write("3. User-Friendly Interface")
    st.write("With an intuitive user interface built using Streamlit, the application ensures a seamless experience. The sidebar navigation allows you to explore different sections, such as Home, Project Details, Contact Us, and About Us.")
    st.write("4. Informative Project Section")
    st.write("Learn more about the Project features and functionality in the project section. Understand how the alarm setup works, from selecting dates and times to experiencing the alarm and snooze features in action.")
    st.title("How to Use:")
    st.write("1: Navigate to the sidebar to explore different sections - Home, Project, Contact Us, and About Us.")
    st.write("2: In the Project section, set your alarm by selecting a date, time, and snooze duration.")
    st.write("3: Click on Start Alarm to experience the wake-up call and snooze functionality.")
    st.write("4: Visit Contact Us for any inquiries or check out the About Us section to learn more about the developers.")
    st.write("We hope you enjoy using the Streamlit Alarm Clock project! Wake up refreshed and ready to tackle your day with this customizable and user-friendly alarm application.")
# ... (user information and input)

# Check if the section is "Project" before displaying the button
if sidebar_selection == "Project" and st.button("Start Alarm"):
    st.write(f"Alarm set for {alarm_datetime}")
    while datetime.now() < alarm_datetime:
        time.sleep(1)

    st.write("Wake up! It's time!")
    play_alarm_sound()

    snooze_time = datetime.now() + timedelta(minutes=snooze_duration)

    while True:
        current_time = datetime.now()

        if current_time >= snooze_time:
            st.write("Snooze time's up!")
            play_alarm_sound()
            snooze_time = current_time + timedelta(minutes=snooze_duration)

        time.sleep(1)
