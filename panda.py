import os
import pandas as pd



df = pd.read_csv('hospital.csv')

carpeta_resultados = 'analisis_hospital'
if not os.path.exists(carpeta_resultados):
    os.makedirs(carpeta_resultados)

consultas_por_genero = df['GENERO'].value_counts()
consultas_por_genero.to_csv(os.path.join(carpeta_resultados, 'consultas_por_genero.csv'))


consultas_por_tipo = df['TIPO DE CONSULTA'].value_counts()
consultas_por_tipo.to_csv(os.path.join(carpeta_resultados, 'consultas_por_tipo.csv'))

consultas_por_aseguradora = df['ASEGURADOR EAPB'].value_counts()
consultas_por_aseguradora.to_csv(os.path.join(carpeta_resultados, 'consultas_por_aseguradora.csv'))

consultas_por_municipio = df['MUNICIPIO'].value_counts()
consultas_por_municipio.to_csv(os.path.join(carpeta_resultados, 'consultas_por_municipio.csv'))

edad_describe = df['EDAD'].describe()
edad_describe.to_csv(os.path.join(carpeta_resultados, 'analisis_de_edad.csv'))


bins = [0, 18, 30, 40, 50, 60, 100] 
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '60+']
df['RANGO EDAD'] = pd.cut(df['EDAD'], bins=bins, labels=labels, right=False)
consultas_por_rango_edad = df['RANGO EDAD'].value_counts()
consultas_por_rango_edad.to_csv(os.path.join(carpeta_resultados, 'consultas_por_rango_edad.csv'))


agrupado_genero_tipo = df.groupby(['GENERO', 'TIPO DE CONSULTA']).size().unstack(fill_value=0)
agrupado_genero_tipo.to_csv(os.path.join(carpeta_resultados, 'agrupado_genero_tipo.csv'))

print(f"Análisis completado. Todos los resultados se han guardado en la carpeta '{carpeta_resultados}'.")
