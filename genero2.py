import pandas as pd
import matplotlib.pyplot as plt

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