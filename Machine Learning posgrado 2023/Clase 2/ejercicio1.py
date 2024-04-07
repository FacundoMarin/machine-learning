import pandas as pd
import matplotlib.pyplot as plt


input_file = "casos_covid_bahia.csv"


# Reading the file
df = pd.read_csv(input_file, header = 0)

#Plotting the data using pyplot

plt.scatter(df['fecha'], df['aislamiento_por_contacto_estrecho'])
plt.xlabel('fecha')
plt.ylabel('aislamiento_por_contacto_estrecho')
plt.title('Scatter Plot')
plt.show()