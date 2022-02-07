import streamlit as st
import time

def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1

            st.write("Time Up!")

def main():
    st.title("Pomodoro")
    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=25)
    time_in_seconds = time_minutes * 60

    if st.button("FOCUS"):
        count_down(int(time_in_seconds))

if __name__ == '__main__':
    main()
