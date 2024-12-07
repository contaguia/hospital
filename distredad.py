import pandas as pd
import matplotlib.pyplot as plt

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