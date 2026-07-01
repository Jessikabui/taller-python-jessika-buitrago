# analisis.py
# Carga el CSV y hace un analisis estadistico basico
 
import pandas as pd
 
# Cargar el archivo
df = pd.read_csv("datos_ejemplo.csv")
 
# 1. Primeras 5 filas
print("Primeras 5 filas:")
print(df.head())
print()
 
# 2. Resumen estadistico de las variables numericas
print("Resumen estadistico:")
print(df.describe())
print()
 
# 3. Conteo de personas por area
print("Conteo por área:")
print(df["area"].value_counts())
print()
 
# 4. Promedio de ingreso por area
print("Promedio de ingreso por área:")
print(df.groupby("area")["ingreso"].median().round(0))
print()
 
# 5. Promedio de ingreso por sexo y edad
print("Promedio de ingreso por sexo y edad:")
print(df.groupby(["sexo", "area"])["ingreso"].mean().round(0))

variMean = df.groupby(["sexo", "area"])["ingreso"].mean().round(0)
variMean.to_excel("resumen.xlsx", index= False)
