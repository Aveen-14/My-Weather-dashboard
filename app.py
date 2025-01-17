import streamlit as st
import requests
import pandas as pd
import json
st.title("AVEEN'S WEATHER DASHBOARD")
st.header("see the weather outside")


lat = st.sidebar.number_input("Enter Latitued",value=0.0)
lon = st.sidebar.number_input("Enter longitued",value=0.0)

api_url=f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,is_day,rain,showers,snowfall,cloud_cover,pressure_msl,surface_pressure,wind_direction_10m&hourly=temperature_2m,relative_humidity_2m,rain,showers,snowfall,wind_speed_180m,wind_direction_180m,temperature_180m,soil_temperature_54cm,soil_moisture_27_to_81cm&daily=temperature_2m_max,wind_speed_10m_max&timezone=auto'
resp = requests.get(api_url)
value = json.loads(resp.text)
temp = value["current"]["temperature_2m"]
heu = value["current"]["relative_humidity_2m"]
day = value["current"]["is_day"]
rain = value["current"]["rain"]
sho = value["current"]["showers"]
sno = value["current"]["snowfall"]

select_box = st.sidebar.selectbox("select a data to insert into the line chart",("temperature","rain","showers","snowfall","relative_humidity","wind_direction_180m"))


def Day_Night():
    return "Day" if day == 1 else "Night"

col1, col2, col3, col4 ,col5, col6 = st.columns(6)
with col1:
    st.metric("Temperature",temp)
with col2:
    st.metric("relative_humidity",heu)
with col3:
    st.metric("day or night",Day_Night() )
with col4:
    st.metric("rain",rain)
with col5:
    st.metric("showers",sho)
with col6:
    st.metric("snowfall",sno)

x = pd.DataFrame(value['hourly']["temperature_2m"],
                value["hourly"]["time"])

a = pd.DataFrame(value['hourly']["rain"],
                value["hourly"]["time"])

b = pd.DataFrame(value['hourly']["showers"],
                value["hourly"]["time"])

c = pd.DataFrame(value['hourly']["snowfall"],
                value["hourly"]["time"])

d = pd.DataFrame(value['hourly']["relative_humidity_2m"],
                value["hourly"]["time"])

e = pd.DataFrame(value['hourly']["wind_direction_180m"],
                value["hourly"]["time"])

    
if select_box == "temperature":
    st.line_chart(x)

elif select_box == "rain":
    st.line_chart(a)

elif select_box == "showers":
    st.line_chart(b)

elif select_box == "snowfall":
    st.line_chart(c)

elif select_box == "relative_humidity":
    st.line_chart(d)

else:
    st.line_chart(e)




# import pandas as pd
# st.title("AVEEN'S WEATHER DASHBOARD")
# st.header("see the weather outside")
# st.write("see the weather outside")
# st.text("see the weather outside")
# st.image("wa.jpg")
# st.video("https://v.ftcdn.net/01/97/53/00/700_F_197530009_kMXZkyaafoDKXkegww5b5AeWfIcKnA4O_ST.mp4")
# st.button("wa.jpg")
# st.checkbox("Agree?")
# st.text_input("enter your name ,town, city, country")
# name = st.text_input("enter your name")
# st.write(f"Hello {name} welcome to My Weather dashboard ")