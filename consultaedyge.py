import pandas as pd
import matplotlib.pyplot as plt

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