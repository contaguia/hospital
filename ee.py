import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Contar consultas por género
gender_count = data['GENERO'].value_counts()

# Gráfico
gender_count.plot(kind='bar', color=['skyblue', 'pink'])
plt.title('Distribución de Consultas por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Consultas')
plt.show()


df=pd.read_csv("hospital.csv")

edad=df["CICLO DE VIDA"].value_counts()

plt.figure(figsize=(12,8))
plt.pie(edad,labels=edad.index, autopct="%2.1f%%",startangle=90)
plt.title('Distribución de Consultas por edades')
plt.show()


# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Filtrar los datos solo para el año 2024 y de enero a junio
data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) & (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# Crear rangos de edad
bins = [0, 18, 30, 40, 50, 60, 100]
labels = ['Menor de 18', '18-30', '31-40', '41-50', '51-60', 'Mayor de 60']
data_2024['RANGO DE EDAD'] = pd.cut(data_2024['EDAD'], bins=bins, labels=labels)

# Contar consultas por rango de edad y género
age_gender_count = data_2024.groupby(['RANGO DE EDAD', 'GENERO']).size().unstack(fill_value=0)

# Gráfico de barras apiladas
ax = age_gender_count.plot(kind='bar', stacked=True, color=['skyblue', 'pink'])

# Añadir las cifras sobre las barras
for p in ax.patches:
    height = p.get_height()
    width = p.get_width()
    x, y = p.get_xy()  # obtiene las coordenadas del bloque de la barra
    ax.text(x + width / 2, y + height / 2, str(int(height)), 
            ha='center', va='center', color='black', fontsize=10)

# Títulos y etiquetas
plt.title('Consultas por Edad y Género (Enero a Junio 2024)')
plt.xlabel('Rango de Edad')
plt.ylabel('Cantidad de Consultas')
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos para personas entre 60 y 105 años
data_age_filtered = data[(data['EDAD'] >= 60) & (data['EDAD'] <= 105)]

# Contar personas por edad y género
age_gender_count = pd.crosstab(data_age_filtered['EDAD'], data_age_filtered['GENERO'])

# Crear el gráfico de barras apiladas
age_gender_count.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='coolwarm', edgecolor='black')

# Personalizar el gráfico
plt.title('Distribución de Personas por Edad (60-105 años) y Género', fontsize=16)
plt.xlabel('Edad', fontsize=14)
plt.ylabel('Cantidad de Personas', fontsize=14)
plt.legend(title='Género', title_fontsize=12, fontsize=10)
plt.xticks(rotation=45)  # Gira las etiquetas del eje X para mayor claridad

# Etiquetas precisas sobre las barras
for i, age in enumerate(age_gender_count.index):
    cumulative_height = 0
    for gender in age_gender_count.columns:
        value = age_gender_count.loc[age, gender]
        if value > 0:  # Mostrar etiquetas solo si hay valores
            plt.text(i, cumulative_height + value / 2, str(value),
                     ha='center', va='center', fontsize=8, color='white', fontweight='bold')
            cumulative_height += value

# Ajustar diseño
plt.tight_layout()
plt.show()


# Cargar los datos desde el archivo CSV
# data = pd.read_csv('hospital.csv')
df=pd.read_csv("hospital.csv")

consultas_por_municipio= df["MUNICIPIO"].value_counts()
municipios_mas_200 = consultas_por_municipio[consultas_por_municipio > 200]
plt.figure(figsize=(8, 6))
municipios_mas_200.plot(kind='bar', color='lightblue')
plt.title('Número de Consultas por Municipio (más de 200 consultas)') 
plt.xlabel('Municipio')
plt.ylabel('Número de Consultas')
plt.tight_layout()  # Ajustar el diseño para que no se corte el texto
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar las consultas por tipo de consulta
type_of_consultation_count = data['TIPO DE CONSULTA'].value_counts()  # Contar las consultas por tipo de consulta

# Crear la figura y el eje
fig, ax = plt.subplots()

# Gráfico de barras
type_of_consultation_count.plot(kind='bar', color='lightblue', ax=ax, width=0.7)

# Gráfico de línea sobre las barras
type_of_consultation_count.plot(kind='line', marker='o', color='orange', ax=ax, linewidth=2, linestyle='-', markerfacecolor='red')

# Añadir los valores exactos en las barras
for i, v in enumerate(type_of_consultation_count):
    ax.text(i, v + 5, str(v), color='black', ha='center', fontweight='bold')  # Ajustar la posición del texto

# Títulos y etiquetas
plt.title('Cantidad de Consultas por Tipo de Consulta')
plt.xlabel('Tipo de Consulta')
plt.ylabel('Cantidad de Consultas')

# Mostrar el gráfico
plt.show()

consultas_por_aseguradora = df["ASEGURADOR EAPB"].value_counts()
aseguradora_mas_20 = consultas_por_aseguradora[consultas_por_aseguradora > 20]
plt.figure(figsize=(8, 6))
aseguradora_mas_20.plot(kind='bar', color='purple')
plt.title('Número de Consultas por Aseguradora (más de 20 consultas)')
plt.xlabel('Aseguradora')
plt.ylabel('Número de Consultas')
plt.tight_layout()  # Ajustar el diseño para que no se corte el texto
plt.show()



municipios_mas_100= consultas_por_municipio[consultas_por_municipio > 100]

plt.figure(figsize=(10, 6))
municipios_mas_100.plot(kind='bar', color='purple')
plt.title('Número de Consultas por Municipio (más de 100 consultas)')  
plt.xlabel('Municipio') 
plt.ylabel('Número de Consultas')
plt.tight_layout()  # Ajustar el diseño para que no se corte el texto
plt.show()

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos del año 2024 y meses de enero a junio
data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) &
                 (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# Tabla de conteo cruzado: Ciclo de Vida vs Tipo de Régimen
cycle_vs_regimen = pd.crosstab(data_2024['CICLO DE VIDA'], data_2024['REGIMEN'])

# Crear el gráfico de barras apiladas
cycle_vs_regimen.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6), edgecolor='black')

# Personalización del gráfico
plt.title('Ciclo de Vida por Tipo de Régimen (Enero - Junio 2024)', fontsize=16)
plt.xlabel('Ciclo de Vida', fontsize=14)
plt.ylabel('Cantidad de Consultas', fontsize=14)
plt.legend(title='Régimen', title_fontsize=12, fontsize=10, loc='upper right')

# Etiquetas precisas sobre las barras
for i, bar_group in enumerate(cycle_vs_regimen.iterrows()):
    total_values = bar_group[1]
    cumulative_height = 0
    for value in total_values:
        if value > 0:  # Mostrar solo si hay valores
            plt.text(i, cumulative_height + value / 2, str(value),
                     ha='center', va='center', fontsize=9, color='white', fontweight='bold')
            cumulative_height += value

# Ajustar diseño
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()