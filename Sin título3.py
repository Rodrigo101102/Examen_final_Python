# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:25:26 2024

@author: Usuario
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
data = pd.read_csv('living.csv')
data.rename(columns={'Cost of living, 2017': 'Costo de Vida'}, inplace=True)

# Mostrar las primeras filas para explorar los datos
print(data.head())

# Información básica sobre el dataset
print(data.info())

# Número de filas y columnas
num_filas, num_columnas = data.shape

# Costo de vida promedio
costo_vida_promedio = data['Costo de Vida'].mean()

# País con costo de vida más alto y más bajo
pais_costo_vida_alto = data.loc[data['Costo de Vida'].idxmax(), 'Countries']
pais_costo_vida_bajo = data.loc[data['Costo de Vida'].idxmin(), 'Countries']

# Costo de vida en Perú y ranking
costo_vida_peru = data.loc[data['Countries'] == 'Peru', 'Costo de Vida'].values[0]
ranking_peru = data.loc[data['Countries'] == 'Peru', 'Global rank'].values[0]  # Cambiado 'Global Rank' a 'Global rank'

# Imprimir el resumen
# Imprimir el resumen
print(f"Número de Filas: {num_filas}")
print(f"Número de Columnas: {num_columnas}")
print(f"Costo de vida promedio: {costo_vida_promedio}")
print(f"País con costo de vida más alto: {pais_costo_vida_alto}")
print(f"País con costo de vida más bajo: {pais_costo_vida_bajo}")
print(f"Costo de Vida en Perú: {costo_vida_peru}")
print(f"Ranking de Perú: {ranking_peru}")


# Filtrar los 10 países con el costo de vida más alto
top_10_alto = data.nlargest(10, 'Costo de Vida')

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
plt.barh(top_10_alto['Countries'], top_10_alto['Costo de Vida'], color='skyblue')
plt.xlabel('Costo de Vida')
plt.ylabel('Países')
plt.title('Top 10 países con el costo de vida más alto')
plt.gca().invert_yaxis()  # Invertir el eje Y para que el país con el mayor costo esté arriba
plt.show()


# Filtrar los 10 países con el costo de vida más bajo
top_10_bajo = data.nsmallest(10, 'Costo de Vida')

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
plt.barh(top_10_bajo['Countries'], top_10_bajo['Costo de Vida'], color='salmon')
plt.xlabel('Costo de Vida')
plt.ylabel('Países')
plt.title('Top 10 países con el costo de vida más bajo')
plt.gca().invert_yaxis()  # Invertir el eje Y para que el país con el menor costo esté arriba
plt.show()


# Filtrar los países de América
paises_america = data[data['Continent'] == 'America']

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
plt.barh(paises_america['Countries'], paises_america['Costo de Vida'], color='lightgreen')
plt.xlabel('Costo de Vida')
plt.ylabel('Países')
plt.title('Costo de vida en los países de América')
plt.gca().invert_yaxis()  # Invertir el eje Y para que los países se alineen en orden de mayor a menor
plt.show()

