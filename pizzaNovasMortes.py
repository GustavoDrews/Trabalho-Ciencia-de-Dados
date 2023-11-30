import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("covid.csv")

cases_by_country = dados.groupby('country')['daily_new_cases'].sum().head(5) 

df = pd.DataFrame({'country': cases_by_country.index, 'daily_new_cases': cases_by_country.values})

df.plot.pie(y='daily_new_cases', labels=df['country'], autopct='%1.1f%%', startangle=90, legend=True)

plt.title('Novos casos Diarios (Covid-19)')

plt.show()
