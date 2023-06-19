import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('trade_data.csv', delimiter='\s+')

plt.figure(figsize=(10, 6))  

for country in data['Страна'].unique():
    country_data = data[data['Страна'] == country]
    plt.plot(country_data['Год'], country_data['Объем'], marker='o', label=country)

plt.xlabel('Год')
plt.ylabel('Объем торговли')
plt.legend()

plt.savefig('trade_volume.png')
plt.show()  
