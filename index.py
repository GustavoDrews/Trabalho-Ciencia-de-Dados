import csv

arq = (open('../covid.csv'))
dados = csv.reader(arq)
print(dados)
print(type(dados))
print()

for item in dados:
    print(item)
    print(type(item))