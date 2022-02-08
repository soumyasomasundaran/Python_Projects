import requests
import streamlit as st

API_KEY = ''
DEGREE_SIGN = u'\N{DEGREE SIGN}'


def convert_to_celcius(k):
    return k - 273.15

def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    general = weather_data['weather'][0]['main']
    icon_id = weather_data['weather'][0]['icon']
    icon = "http://openweathermap.org/img/w/" + icon_id + ".png"
    temperature = round(convert_to_celcius(weather_data['main']['temp']))
    return general, temperature, icon



def main():
    st.header("Find the Weather")
    city = (st.text_input("Enter the city")).lower()

    if st.button('find'):
        general, temp, icon = find_current_weather(city)
        with st.container():
            temp = f"{temp}{DEGREE_SIGN}C"
            c1, c2 = st.columns((2, 2))
            c1.metric(label="Temperature", value=temp)
            c2.image(icon)
            c2.header(general)

if __name__ == '__main__':
    main()
