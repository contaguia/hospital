import pandas as pd
# import matplotlib.pyplot as plt

# Crear un DataFrame
df = pd.read_csv("hospital.csv")
df = pd.read_csv("hospital.csv",encoding="unicode_escape")
# print(df)  
# df.to_csv("hospital2.csv", index=False)


# print(df.head(10))      # Primeras 5 filas
# print(df.tail())       # Últimas 5 filas
# print(df.info())      # Información general
# print(df.describe())   # Estadísticas descriptivas

# Selección de columna
# print(df["EDAD"])

# Selección de varias columnas
# print(df[["CICLO DE VIDA", "REGIMEN"]])

# Filtrado de datos
# print(df[df["ANO DE LA CONSULTA"] > 2022])
           
# print(df[["INGRESO", "TRIMESTRE"]] )


# print(df[["MUNICIPIO","INGRESO","EDAD",]])
# print(df["EDAD"].mean())
# print(df["EDAD"].median())
# print(df["EDAD"].std())

# import matplotlib.pyplot as plt

# # Cargar los datos
# data = pd.read_csv('hospital.csv')

# # Contar consultas por género
# gender_count = data['GENERO'].value_counts()

# # Gráfico
# gender_count.plot(kind='bar', color=['skyblue', 'pink'])
# plt.title('Distribución de Consultas por Género')
# plt.xlabel('Género')
# plt.ylabel('Cantidad de Consultas')
# plt.show()

# import numpy as np

# arr_1d = np.array([1, 2, 3])
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
   
# # Array unidimensional
# print(arr_1d)
# print(arr_2d)
# # Array bidimensional

# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar los datos desde el archivo CSV
# data = pd.read_csv('hospital.csv')

# # Contar consultas por municipio
# municipality_count = data['MUNICIPIO'].value_counts().head(10)  # Mostrar los 10 municipios con más consultas

# # Gráfico de barras horizontales
# ax = municipality_count.plot(kind='barh', color='orange')

# # Títulos y etiquetas
# plt.title('Top 10 de Municipios con Más Consultas (Enero a Junio 2024)')
# plt.xlabel('Cantidad de Consultas')
# plt.ylabel('Municipio')

# # Añadir los valores exactos dentro de las barras
# for i, v in enumerate(municipality_count):
#     ax.text(v + 10, i, str(v), color='black', va='center', fontweight='bold')  # Ajusta el valor de '10' según sea necesario

# # Mostrar el gráfico
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar los datos desde el archivo CSV
# data = pd.read_csv('hospital.csv')

# # Filtrar los datos solo para el año 2024 y de enero a junio
# data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) & (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# # Crear rangos de edad
# bins = [0, 18, 30, 40, 50, 60, 100]
# labels = ['Menor de 18', '18-30', '31-40', '41-50', '51-60', 'Mayor de 60']
# data_2024['RANGO DE EDAD'] = pd.cut(data_2024['EDAD'], bins=bins, labels=labels)

# # Contar consultas por rango de edad y género
# age_gender_count = data_2024.groupby(['RANGO DE EDAD', 'GENERO']).size().unstack(fill_value=0)

# # Gráfico de barras apiladas
# ax = age_gender_count.plot(kind='bar', stacked=True, color=['skyblue', 'pink'])

# # Añadir las cifras sobre las barras
# for p in ax.patches:
#     height = p.get_height()
#     width = p.get_width()
#     x, y = p.get_xy()  # obtiene las coordenadas del bloque de la barra
#     ax.text(x + width / 2, y + height / 2, str(int(height)), 
#             ha='center', va='center', color='black', fontsize=10)

# # Títulos y etiquetas
# plt.title('Consultas por Edad y Género (Enero a Junio 2024)')
# plt.xlabel('Rango de Edad')
# plt.ylabel('Cantidad de Consultas')
# plt.xticks(rotation=45)

# # Mostrar el gráfico
# plt.show()

