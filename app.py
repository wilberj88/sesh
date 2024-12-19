import streamlit as st
from streamlit_echarts import st_echarts
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64
from streamlit_timeline import st_timeline
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import folium
from streamlit_folium import st_folium
import time

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Demo Sesh by Novus ♬", page_icon="♬")

#TITULO
st.title('Mando ♬ Sesh')
st.header('Music Industry and Artists Management')

validos2023 = 900000
meta2023 = validos2023*0.36

meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338


colored_header(
    label="Real Time Performance",
    description="Based on Tiktok and other APIs",
    color_name="violet-70",
)
current_time = time.ctime()
st.write("Siendo HOY y AHORA las: ", current_time)

my_grid = grid(3, 3, vertical_align="bottom")
# Row 1:
my_grid.selectbox("Indica un País", ["Zona 1", "Zona 2", "Zona 3", "Zona 4"])
my_grid.selectbox("Indica Artista", ["18a 25 años", "25-45 años", "45-60 años", "+60años"])
my_grid.selectbox("Indica un Género", ["Mujer", "Hombre", "LGBTQI+"])

# Row 2:
my_grid.button("General Campañas de Márketing", use_container_width=True)
my_grid.button("Última Campaña de Márketing", use_container_width=True)
my_grid.button("Penúltima Campaña de Marketing", use_container_width=True)


options = {
            "title": {"text": "Alcance Campañas HOY por horas"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["Zona_9", "Zona_8", "Zona_7", "Zona_6", "Zona_5", "Zona_4", "Zona_3", "Zona_2", "Zona_1"]},
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": ["10am", "11am", "12md", "1pm", "2pm", "3pm", "4pm"],
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Zona_9",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_9*0.1, meta_zona_9*0.2, meta_zona_9*0.35, meta_zona_9*0.45, meta_zona_9*0.5, meta_zona_9*0.75, meta_zona_9],
                },
                {
                    "name": "Zona_8",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_8*0.1, meta_zona_8*0.2, meta_zona_8*0.35, meta_zona_8*0.45, meta_zona_8*0.5, meta_zona_8*0.75, meta_zona_8],
                },
                {
                    "name": "Zona_7",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_7*0.1, meta_zona_7*0.2, meta_zona_7*0.35, meta_zona_7*0.45, meta_zona_7*0.5, meta_zona_7*0.75, meta_zona_7],
                },
                  {
                    "name": "Zona_6",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_6*0.1, meta_zona_6*0.2, meta_zona_6*0.35, meta_zona_6*0.45, meta_zona_6*0.5, meta_zona_6*0.75, meta_zona_6],
                },
                 {
                    "name": "Zona_5",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                },
                  {
                    "name": "Zona_4",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                },
                  {
                    "name": "Zona_3",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                },
                  {
                    "name": "Zona_2",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                },
                  {
                    "name": "Zona_1",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                },
            ],
        }
st_echarts(options=options, height="400px") 


my_grid1 = grid(4, vertical_align="bottom")
my_grid1.button("Push Email", use_container_width=True)
my_grid1.button("Push Tik Tok", use_container_width=True)
my_grid1.button("Push Facebook e IG", use_container_width=True)
my_grid1.button("Google & Youtube", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Correos", "300000", "14%")
col2.metric("Celulares", "4500000", "-18%")
col3.metric("ID_Meta", "1000000", "13%")
col4.metric("ID_Google", "950000", "18%")


col6, col7 = st.columns(2)
with col6:
    option = {
        "title": {"text": "Eficacia de la Campaña de Marketing", "subtext": "Porcentaje Conversión(%)"},
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
        "toolbox": {
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            }
        },
        "legend": {"data": ["Contactados", "Interesados", "Oyentes", "Seguidor", "Fan"]},
        "series": [
            {
                "name": "Contactados",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "label": {"formatter": "{b}%"},
                "labelLine": {"show": False},
                "itemStyle": {"opacity": 0.7},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}预期: {c}%"}
                },
                "data": [
                    {"value": 60, "name": "Fan"},
                    {"value": 40, "name": "Seguidor"},
                    {"value": 20, "name": "Oyentes"},
                    {"value": 80, "name": "Interesados"},
                    {"value": 100, "name": "Contactados"},
                ],
            },
            {
                "name": "Margen",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "maxSize": "80%",
                "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}实际: {c}%"}
                },
                "data": [
                    {"value": 30, "name": "Fan"},
                    {"value": 10, "name": "Seguidor"},
                    {"value": 5, "name": "Oyentes"},
                    {"value": 50, "name": "Interesados"},
                    {"value": 80, "name": "Contactados"},
                ],
                "z": 100,
            },
        ],
    }
    st_echarts(option, height="500px")    

with col7:
    option = {
        "legend": {},
        "tooltip": {"trigger": "axis", "showContent": False},
        "dataset": {
            "source": [
                ["product", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
                ["Correos", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                ["Facebook & IG", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                ["Google & Youtube", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                ["Celular", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
            ]
        },
        "xAxis": {"type": "category"},
        "yAxis": {"gridIndex": 0},
        "grid": {"top": "55%"},
        "series": [
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "pie",
                "id": "pie",
                "radius": "30%",
                "center": ["50%", "25%"],
                "emphasis": {"focus": "data"},
                "label": {"formatter": "{b}: {@2012} ({d}%)"},
                "encode": {"itemName": "product", "value": "Lunes", "tooltip": "Lunes"},
            },
        ],
    }
    st_echarts(option, height="500px", key="echarts")

my_grid2 = grid(3, vertical_align="bottom")
my_grid2.button("Oyentes País", use_container_width=True)
my_grid2.button("Oyentes Género", use_container_width=True)
my_grid2.button("Oyentes Artista", use_container_width=True)


# center on Liberty Bell, add marker
m = folium.Map(location=[10.4735, -73.2486], zoom_start=13)
n = folium.Map(location=[10.45358, -73.26678], zoom_start=13)
l = folium.Map(location=[10.44664, -73.30750], zoom_start=13)

#zona1
folium.Marker(
    [10.47358, -73.248639], popup="Z1 PV1 PV1 COL Nacional Loperena 3de10K", tooltip="Z1 PV1 PV1 COL Nacional Loperena. 3K de 8K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.474139, -73.25125], popup="Z1 PV2 PV2 ESC Bellas Artes. 2K de 5K", tooltip="Z2 PV2 PV2 ESC Bellas Artes. 2K de 5K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.478472, -73.245361], popup="Z1 PV3 PV3 UDES. 1,5K de 4K", tooltip="Z1 PV3 PV3 UDES. 1,5K de 4K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.468500, -73.247278], popup="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", tooltip="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.469667, -73.238056], popup="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", tooltip="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.474130, -73.251115], popup="PV6 COL Parroquial El Carmelo (Nuevo 2023)", tooltip="PV6 COL Parroquial El Carmelo", icon=folium.Icon(icon='cloud')
).add_to(m)
#zona2
folium.Marker(
    [10.46006, -73.22889], popup="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", tooltip="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.46322, -73.23575], popup="Z2 PV2 PV8 I.E. Manuel Germán Cuello. 2K de 4K", tooltip="Z2 PV1 PV8 I.E. Manuel Germán Cuello. 2K de 4K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.45389, -73.24211], popup="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", tooltip="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.45100, -73.23672], popup="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", tooltip="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", icon=folium.Icon(icon='flag')
).add_to(m)
#zona3
folium.Marker(
    [10.44578, -73.25128], popup="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", tooltip="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", icon=folium.Icon(icon='star')
).add_to(m)
folium.Marker(
    [10.44950, -73.25075], popup="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", tooltip="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", icon=folium.Icon(icon='star')
).add_to(n)
folium.Marker(
    [10.45131, -73.25711], popup="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", tooltip="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", icon=folium.Icon(icon='star')
).add_to(n)
folium.Marker(
    [10.45714, -73.25153], popup="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", tooltip="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", icon=folium.Icon(icon='star')
).add_to(n)
folium.Marker(
    [10.43650, -73.25356], popup="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", tooltip="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", icon=folium.Icon(icon='star')
).add_to(n)
#zona4
folium.Marker(
    [10.45358, -73.26678], popup="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", tooltip="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", icon=folium.Icon(icon='info-sign')
).add_to(n)
folium.Marker(
    [10.45892, -73.25958], popup="Z4 PV2 PV21 COL Nacionalizado UPAR. 3,5K de 8K", tooltip="Z4 PV2 PV21 COL Nacionalizado UPAR 8K. 3,5K de 8K", icon=folium.Icon(icon='info-sign')
).add_to(n)
folium.Marker(
    [10.46157, -73.26789], popup="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", tooltip="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", icon=folium.Icon(icon='info-sign')
).add_to(n)
folium.Marker(
    [10.46661, -73.25814], popup="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", tooltip="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    [10.44381, -73.27533], popup="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", tooltip="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", icon=folium.Icon(icon='info-sign')
).add_to(m)
#zona5
folium.Marker(
    [10.47242, -73.26011], popup="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", tooltip="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47242, -73.26011], popup="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", tooltip="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47928, -73.27719], popup="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", tooltip="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47842, -73.29089], popup="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", tooltip="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.48606, -73.28081], popup="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", tooltip="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", icon=folium.Icon(icon='bicycle')
).add_to(m)
#zona6
folium.Marker(
    [10.48044, -73.24781], popup="Z6 PV1 PV33 COL. Pablo Sexto 5K", tooltip="Z6 PV1 PV33 COL. Pablo Sexto 5K", color='red'
).add_to(m)
folium.Marker(
    [10.48181, -73.25644], popup="Z6 PV2 PV34 CONC.San Joaquin 4K", tooltip="Z6 PV2 PV34 CONC.San Joaquin 4K", color='red'
).add_to(l)
folium.Marker(
    [10.49319, -73.26533], popup="Z6 PV3 PV35 COL. Sagrada Familia 3K", tooltip="Z6 PV3 PV35 COL. Sagrada Familia 3K", color='red'
).add_to(l)
#zona7
folium.Marker(
    [10.47475, -73.25969], popup="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", tooltip="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", color='red'
).add_to(l)
#zona8
folium.Marker(
    [10.46442, -73.25625], popup="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", tooltip="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", color='red'
).add_to(l)
folium.Marker(
    [10.44664, -73.30750], popup="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", tooltip="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", color='red'
).add_to(l)

colA, colB, colC = st.columns(3)
with colA:
    st_data = st_folium(m, width=500)
with colB:
    st_data = st_folium(n, width=500)
with colC:
    st_data = st_folium(l, width=500)



colored_header(
    label="Alarmas",
    description="TODAY",
    color_name="violet-70",
)

st.header('Tendencias y Climas Mundiales 🌎')

colored_header(
    label="Búsquedas online en Google",
    description="Última hora y día",
    color_name="violet-70",
)

pytrends = TrendReq(hl='en-US', tz=360)
col4, col5, col6 = st.columns(3)
with col4:
    st.write("🇺🇸 USA Top10 Trending Search in last hour")
      # Google Trends data
    df1 = pytrends.trending_searches(pn='united_states')
    st.dataframe(df1.head(10))
with col5:
    st.write("🇬🇧 UK Top10 Trending Search in last hour")
      # Google Trends data
    df2 = pytrends.trending_searches(pn='united_kingdom')
    st.dataframe(df2.head(10))
with col6:
    st.write("🇨🇴 COL Top10 Trending Search in last hour")
    df3 = pytrends.trending_searches(pn='colombia')
    st.dataframe(df3.head(10))
    




colored_header(
    label="Wheater Now",
    description="América, EU & ASIA",
    color_name="red-70",
)

#ALARMS CONFIGURATION
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "146090ad17fa8843bc9eca97c53926b4"
sity1 = "New York"
sity2 = "San Francisco"
sity3 = "Toledo"
sity4 = "London"
sity5 = "Pekin"
sity6 = "Bombai"
URL1 = BASE_URL + "q=" + sity1 + "&appid=" + API_KEY
URL2 = BASE_URL + "q=" + sity2 + "&appid=" + API_KEY
URL3 = BASE_URL + "q=" + sity3 + "&appid=" + API_KEY
URL4 = BASE_URL + "q=" + sity4 + "&appid=" + API_KEY
URL5 = BASE_URL + "q=" + sity5 + "&appid=" + API_KEY
URL6 = BASE_URL + "q=" + sity6 + "&appid=" + API_KEY


response1 = requests.get(URL1)
response2 = requests.get(URL2)
response3 = requests.get(URL3)
response4 = requests.get(URL4)
response5 = requests.get(URL5)
response6 = requests.get(URL6)

if response1.status_code == 200:
   # getting data in the json format
   data1 = response1.json()
   # getting the main dict block
   main1 = data1['main']
  # getting temperature
   temperature1 = main1['temp']
   # getting the humidity
   humidity1 = main1['humidity']
   # getting the pressure
   pressure1 = main1['pressure']
   # weather report
   report1 = data1['weather']

if response2.status_code == 200:
   # getting data in the json format
   data2 = response2.json()
   # getting the main dict block
   main2 = data2['main']
  # getting temperature
   temperature2 = main2['temp']
   # getting the humidity
   humidity2 = main2['humidity']
   # getting the pressure
   pressure2 = main2['pressure']
   # weather report
   report2 = data2['weather']

if response3.status_code == 200:
   # getting data in the json format
   data3 = response3.json()
   # getting the main dict block
   main3 = data3['main']
  # getting temperature
   temperature3 = main3['temp']
   # getting the humidity
   humidity3 = main3['humidity']
   # getting the pressure
   pressure3 = main3['pressure']
   # weather report
   report3 = data3['weather']

if response4.status_code == 200:
   # getting data in the json format
   data4 = response4.json()
   # getting the main dict block
   main4 = data4['main']
  # getting temperature
   temperature4 = main4['temp']
   # getting the humidity
   humidity4 = main4['humidity']
   # getting the pressure
   pressure4 = main4['pressure']
   # weather report
   report4 = data4['weather']

if response5.status_code == 200:
   # getting data in the json format
   data5 = response5.json()
   # getting the main dict block
   main5 = data5['main']
  # getting temperature
   temperature5 = main5['temp']
   # getting the humidity
   humidity5 = main5['humidity']
   # getting the pressure
   pressure5 = main5['pressure']
   # weather report
   report5 = data5['weather']

if response6.status_code == 200:
   # getting data in the json format
   data6 = response6.json()
   # getting the main dict block
   main6 = data6['main']
  # getting temperature
   temperature6 = main6['temp']
   # getting the humidity
   humidity6 = main6['humidity']
   # getting the pressure
   pressure6 = main6['pressure']
   # weather report
   report6 = data6['weather']

col4, col5, col6 = st.columns(3)

with col4:
    st.write("🌧 USA ☀️")
    st.write(f"{sity1:-^30}")
    st.write(f"Temperature (Kelvins): {temperature1}")
    st.write(f"Humidity: {humidity1}")
    st.write(f"Pressure: {pressure1}")
    st.write(f"Weather Report: {report1[0]['description']}")
    st.write(f"{sity2:-^30}")
    st.write(f"Temperature (Kelvins): {temperature2}")
    st.write(f"Humidity: {humidity2}")
    st.write(f"Pressure: {pressure2}")
    st.write(f"Weather Report: {report2[0]['description']}")

with col5:
    st.write("🌧 Europe ☀️")
    st.write(f"{sity3:-^30}")
    st.write(f"Temperature (Kelvins): {temperature3}")
    st.write(f"Humidity: {humidity3}")
    st.write(f"Pressure: {pressure3}")
    st.write(f"Weather Report: {report3[0]['description']}")
    st.write(f"{sity4:-^30}")
    st.write(f"Temperature (Kelvins): {temperature4}")
    st.write(f"Humidity: {humidity4}")
    st.write(f"Pressure: {pressure4}")
    st.write(f"Weather Report: {report4[0]['description']}")
    
with col6:
    st.write("🌧 Asia ☀️")
    st.write(f"{sity5:-^30}")
    st.write(f"Temperature (Kelvins): {temperature5}")
    st.write(f"Humidity: {humidity5}")
    st.write(f"Pressure: {pressure5}")
    st.write(f"Weather Report: {report5[0]['description']}")
    st.write(f"{sity6:-^30}")
    st.write(f"Temperature (Kelvins): {temperature6}")
    st.write(f"Humidity: {humidity6}")
    st.write(f"Pressure: {pressure6}")
    st.write(f"Weather Report: {report6[0]['description']}")
    

col1, col2, col3 = st.columns(3)
with col1:
  acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 50, "name": "Alcance"}],
            }
        ],
    }

  st_echarts(options=acelerometro1)

with col2:
  acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 85, "name": "Engagement"}],
            }
        ],
    }

  st_echarts(options=acelerometro2)

with col3:
  acelerometro3 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 20, "name": "Comments"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)


colored_header(
    label="Recomendaciones de Márketing Musical",
    description="PARA MAÑANA",
    color_name="violet-70",
)

colx, coly, colz = st.columns(3)
colx = st.checkbox('Territoriales: festivos y días especiales')
coly = st.checkbox('Climática: condiciones para tus ciudades con mayores oyentes')
colz = st.checkbox('Por Canales: Redes Sociales, Email & En Vivos')
