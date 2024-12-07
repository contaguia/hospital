import pandas as pd
import matplotlib.pyplot as plt

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