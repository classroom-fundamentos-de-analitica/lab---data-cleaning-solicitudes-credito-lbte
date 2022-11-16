"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re

def clean_data():
  ruta_gh = "solicitudes_credito.csv"
  df = pd.read_csv(ruta_gh, sep=";")
  df.drop(df.columns[0], inplace=True, axis=1)
  df.iloc[:,0:4] =  df.iloc[:,0:4].apply(lambda x : x.str.lower().str.replace("[_-]", " "), axis=1)
  df.línea_credito =  df.línea_credito.apply(lambda x : re.sub(r"[_-]", " ", x.lower()))
  df.monto_del_credito =  df.monto_del_credito.apply(lambda x : re.sub(r"\$\s|\.00|,", "", x)).astype(int)
  df.fecha_de_beneficio = df.fecha_de_beneficio.apply(lambda x : pd.to_datetime(x, format="%Y/%m/%d") if re.match('^\d{4}\/', x) else pd.to_datetime(x, format="%d/%m/%Y"))
  df.drop_duplicates(inplace=True)
  df.dropna(inplace=True)
  return df
