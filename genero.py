import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("hospital.csv")

plt.figure(figsize=(12,8))
sns.countplot(data=df,x="GENERO",palette="coolwarm")
plt.title('Distribución de Consultas por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Consultas')
plt.show()
