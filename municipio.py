import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("hospital.csv")

ax=df["MUNICIPIO"].value_counts().head(10)

plt.figure(figsize=(12,8))
ax.plot(kind='bar',color="orange")
plt.title('Distribución de Consultas por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Consultas')
plt.show()