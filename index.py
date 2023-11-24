import csv

def getDados():
    arq = (open('covid.csv'))
    dados = csv.reader(arq)
    return(dados) 

def getCountries():
    dados = getDados()

    countries = []
    for item in dados:
        if not item[1] in countries:
            countries.append(item[1])
    return(countries)