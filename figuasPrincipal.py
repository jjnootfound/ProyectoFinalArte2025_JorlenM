import pandas as pd
import funciones
from funciones import circulo, triangulo, rectangulo

dataFile = pd.read_csv("figuras.csv")

print("procesando figuras... \n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
	if row["FIGURA"] == "t":
		area = triangulo(row["MEDIDA1"], row["MEDIDA2"])
	elif row["FIGURA"] == "r":
		area = rectangulo(row["MEDIDA1"], row["MEDIDA2"])
	elif row["FIGURA"] == "c":
		area = circulo(row["MEDIDA1"])
	else:
		area = 0
	print(f"Fila {index}: Figura {row['FIGURA']}, Medida1 = {row['MEDIDA1']}, Medida2 = {row['MEDIDA2']}, Area = {area}")

