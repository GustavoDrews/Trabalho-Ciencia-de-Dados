import csv

def getDados():
    arq = (open('covid.csv'))
    dados = csv.reader(arq)
    return(dados) 