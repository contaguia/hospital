import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar consultas por municipio
municipality_count = data['MUNICIPIO'].value_counts().head(10)  # Mostrar los 10 municipios con más consultas

# Crear la figura y el eje
fig, ax = plt.subplots()

# Gráfico de barras
municipality_count.plot(kind='bar', color='skyblue', ax=ax, width=0.7)

# Gráfico de línea (curva) sobre las barras
municipality_count.plot(kind='line', marker='o', color='orange', ax=ax, linewidth=2, linestyle='-', markerfacecolor='red')

# Añadir los valores exactos en las barras
for i, v in enumerate(municipality_count):
    ax.text(i, v + 10, str(v), color='black', ha='center', fontweight='bold')  # Ajustar la posición del texto

# Títulos y etiquetas
plt.title('Top 10 de Municipios con Más Consultas (Enero a Junio 2024)')
plt.xlabel('Municipio')
plt.ylabel('Cantidad de Consultas')

# Mostrar el gráfico
plt.show()