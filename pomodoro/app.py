import streamlit as st
import time

def count_down(ts):
    #with st.empty():
    while ts:
        mins, secs = divmod(ts,60)
        time_now = '{:02d}:{:02d}'.format(mins,secs)
        st.header(time_now)
        time.sleep(1)
        ts -= 1
    st.header("Time up!!")



def main():
    st.title("Pomodoro Timer")
    time_in_minutes = st.number_input("Enter the time in minutes",min_value = 1,value = 25)
    time_in_seconds = time_in_minutes*60
    if st.button("START"):
        count_down(time_in_seconds)







if __name__ =='__main__':
    main()