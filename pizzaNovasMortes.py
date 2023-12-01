import pandas as pd
import matplotlib.pyplot as plt

def getGraficoPizza(quant):
    dados = pd.read_csv("covid.csv")

    cases_by_country = dados.groupby('country')['daily_new_cases'].sum() 

    df = pd.DataFrame({'country': cases_by_country.index, 'Novos casos diários': cases_by_country.values})

    df = df.sort_values(by='Novos casos diários', ascending=False).head(quant)

    df.plot.pie(y='Novos casos diários', labels=df['country'], autopct='%1.1f%%', startangle=90, legend=False)

    plt.title('TOP '+str(quant)+' Novos casos Diários (Covid-19)')

    plt.show()