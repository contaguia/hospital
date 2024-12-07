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