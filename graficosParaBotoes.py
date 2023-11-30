import pandas as pd
import matplotlib.pyplot as plt
import index

def casosDiariosPaises(paisSelecionado):
    caminho_arquivo = 'covid.csv'

    countriesdados = index.getCountries()

    for country in countriesdados:
        if country == paisSelecionado:
            dados = pd.read_csv(caminho_arquivo)

            print(dados.head())

            pais = dados[dados['country'] == country]

            pais['date'] = pd.to_datetime(pais['date'])
            
            # Cria o gráfico
            plt.figure(figsize=(10, 6))
            plt.bar(pais['date'], pais['daily_new_cases'], color='b', alpha=0.7)

            # Adiciona rótulos e título
            plt.xlabel('Data')
            plt.ylabel('Novos Casos Diarios')
            plt.title('Novos Casos Diarios no '+ country +' ao longo do tempo')

            # Rotaciona as datas para melhor legibilidade
            plt.xticks(rotation=45)

            # Exibe o gráfico
            plt.show()

            # salva os graficos em uma pasta img
            # plt.savefig('img/'+country+'-grafico.png')
