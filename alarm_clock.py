import streamlit as st
import time
import datetime

def alarm_clock(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        st.title("Alarm Clock")
        st.write(f"Current Time: {current_time}")

        if current_time == alarm_time:
            st.success("Time to wake up!")
            break

        time.sleep(1)

def main():
    st.header("Set Alarm")
    alarm_time = st.time_input("Choose alarm time", value=datetime.time(8, 0))
    alarm_time_str = alarm_time.strftime("%H:%M:%S")

    st.write(f"Alarm set for: {alarm_time_str}")

    st.warning("Keep the Streamlit app running to trigger the alarm.")

    alarm_clock(alarm_time_str)

if __name__ == "__main__":
    main()
