import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import streamlit as st
from maps_request import req
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
from PIL import Image

# Loading Image using PIL
im = Image.open('icon.png')

st.set_page_config(layout="wide", page_title="Panel de control", page_icon = im)
st.sidebar.title("Navigation")

df = pd.read_excel("df_filled.xlsx")
df_map = df.dropna(subset=["lat"])
df_map["cantidad"] = 1

st.title("Mapa de Calor")
# st.dataframe(df_map)
lideres = st.multiselect("Selecciona la lista", df_map.Lider.unique())

m = leafmap.Map(center=[6.376944444444, -75.44611111], zoom=13)
m.add_heatmap(
   df_map[df_map.Lider.isin(lideres)],
   latitude="lat",
   longitude="lon",
   value="cantidad",
   name="Mapa de calor",
   radius=20)

m.add_points_from_xy(
    df_map[df_map.Lider.isin(lideres)],
    x="lon",
    y="lat",
    color_column='Lider',
    icon_names=lideres,
    spin=True,
    add_legend=True,
)
m.to_streamlit(height=700)
