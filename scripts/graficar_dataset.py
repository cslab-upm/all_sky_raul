import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datos2.csv')

aux = pd.DataFrame(data['Objeto'].value_counts())
plt.pie(data['Objeto'].value_counts(), labels = aux.index)
plt.show()
