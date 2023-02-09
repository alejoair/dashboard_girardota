import pandas as pd
from maps_request import req
import numpy as np

df = pd.read_excel("db.xlsx")
df['Direccion'].fillna(df['Barrio/Vereda'], inplace=True)

#df.dropna(subset=["Direccion"], inplace=True)
l1, l2 = [], []
for val in df.Direccion:

    try:
        resp = req(val + ", girardota" )
        l1.append(resp[0])
        l2.append(resp[1])
    except:
        l1.append(np.nan)
        l2.append(np.nan)

l1 = pd.Series(l1)
l2 = pd.Series(l2)

df["lat"] = l1
df["lon"] = l2

df.to_excel("df_filled.xlsx")

