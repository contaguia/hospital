import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar consultas por municipio
municipality_count = data['MUNICIPIO'].value_counts().head(10)  # Mostrar los 10 municipios con más consultas

# Crear gráfico de barras horizontales con más espacio entre las columnas
plt.figure(figsize=(10, 6))  # Aumentar el tamaño de la figura

# Asignar colores diferentes a cada barra usando una paleta de colores
colors = plt.cm.get_cmap('tab10', len(municipality_count))  # Usamos una paleta de 10 colores

# Gráfico de barras horizontales con colores diferentes
ax = municipality_count.plot(kind='barh', color=colors(range(len(municipality_count))))

# Títulos y etiquetas
plt.title('Top 10 de Municipios con Más Consultas (Enero a Junio 2024)', fontsize=14)
plt.xlabel('Cantidad de Consultas', fontsize=12)
plt.ylabel('Municipio', fontsize=12)

# Añadir los valores exactos dentro de las barras
for i, v in enumerate(municipality_count):
    ax.text(v + 10, i, str(v), color='black', va='center', fontweight='bold')  # Ajusta el valor de '10' según sea necesario

# Ajustar el diseño para más espacio entre las barras y las etiquetas
plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)  # Ajustar márgenes

# Rotar las etiquetas del eje Y para mayor claridad si son largas
plt.yticks(rotation=0, fontsize=10)  # Puedes ajustar el tamaño de las etiquetas si es necesario

# Mostrar el gráfico
plt.show()