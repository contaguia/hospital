import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("hospital.csv")

edad=df["CICLO DE VIDA"].value_counts()

plt.figure(figsize=(12,8))
plt.pie(edad,labels=edad.index, autopct="%2.1f%%",startangle=90)
plt.title('Distribución de Consultas por edades')
plt.show()