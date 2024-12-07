import pandas as pd
import matplotlib.pyplot as plt

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