import index as idx
import matplotlib.pyplot as plt

dados = idx.getDados()

mortesDia = []
cont = 0
for item in dados:
    if item[1] == 'Brazil' and item[6]:
        mortesDia.append(item[6].split('.')[0])
        cont += 1

eixoX = []
cont += 1
for i in range(1, cont):
    eixoX.append(i)

plt.plot(eixoX, mortesDia, label="")

plt.xlabel('Dia')
plt.ylabel('Mortes')

plt.title('Grafico de Mortes por Dia no Brasil')

plt.legend()
plt.show()