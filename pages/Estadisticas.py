import streamlit as st
import pandas as pd
df_map = pd.read_excel("df_filled.xlsx")

df_map["cantidad"] = 1

st.title("Estadisticas")
st.dataframe(df_map[["Lider", "cantidad"]].groupby(by="Lider").count())

st.subheader("Cantidad total de cedulas")
st.bar_chart(df_map.groupby(by="Lider").count(), y="cantidad")

st.subheader("Cantidad quitando duplicados")
st.bar_chart(df_map.drop_duplicates(subset=["Cedula"], keep="first").groupby(by="Lider").count(), y="cantidad")
