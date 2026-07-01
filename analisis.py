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
 
# 3. Conteo de personas por sexo
print("Conteo por sexo:")
print(df["sexo"].value_counts())
print()
 
# 4. Promedio de ingreso por sexo
print("Promedio de ingreso por sexo:")
print(df.groupby("sexo")["ingreso"].mean().round(0))
print()
 
# 5. Promedio de ingreso por sexo y area
print("Promedio de ingreso por sexo y area:")
print(df.groupby(["sexo", "area"])["ingreso"].mean().round(0))
