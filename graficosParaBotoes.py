import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import index
from matplotlib.colors import LinearSegmentedColormap

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


def mortesDiariasPaises(paisSelecionado):
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
            plt.bar(pais['date'], pais['daily_new_deaths'], color='red', alpha=0.7)

            # Adiciona rótulos e título
            plt.xlabel('Data')
            plt.ylabel('Mortes diarias')
            plt.title('Novas Mortes Diarias no '+ country +' ao longo do tempo')

            # Rotaciona as datas para melhor legibilidade
            plt.xticks(rotation=45)

            # Exibe o gráfico
            plt.show()

            # salva os graficos em uma pasta img
            # plt.savefig('img/'+country+'-grafico.png')

def mapaPaises(info):
    # Carrega os dados do arquivo CSV
    caminho_arquivo = 'covid.csv'
    dados = pd.read_csv(caminho_arquivo)

    if info == 'mortes':
        coluna = 'cumulative_total_deaths'
    else:
        coluna = 'cumulative_total_cases'

    # Agrupa os dados por país e calcula o total acumulado de mortes ou casos
    total = dados.groupby('country')[coluna].max().reset_index()

    # Carrega um shapefile do mundo usando geopandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge dos dados do mundo com os dados do total
    world = world.merge(total, how='left', left_on='name', right_on='country')

    # Define os países com menor e maior
    min = world[coluna].min()
    max = world[coluna].max()

    # Cria uma escala de cores personalizada de azul claro a vermelho forte
    cmap = LinearSegmentedColormap.from_list('custom_map', ['lightblue', 'darkred'], N=256)
    norm = plt.Normalize(vmin=min, vmax=max)

    # Plota o mapa-múndi com a escala de cores personalizada
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax)
    if info == 'mortes':
        world.plot(column=coluna, ax=ax, legend=True, legend_kwds={'label': 'Total de Mortes'}, cmap=cmap, norm=norm)

        plt.title('Total de Mortes por País')
    else:
        world.plot(column=coluna, ax=ax, legend=True, legend_kwds={'label': 'Total de Casos'}, cmap=cmap, norm=norm)
    
        plt.title('Total de Casos por País')       
    
    plt.show()