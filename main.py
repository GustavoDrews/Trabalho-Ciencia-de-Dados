import tkinter as tk
import graficosParaBotoes as gpbtn

def grafico_casos_diarios():
    paisInformado = entry.get()

    if paisInformado == '':
        print('Informe um país válido (em inglês) no campo texto')
    else:
        gpbtn.casosDiariosPaises(paisInformado)

def grafico_mortes_diarias():
    paisInformado = entry.get()

    if paisInformado == '':
        print('Informe um país válido (em inglês) no campo texto')
    else:
        gpbtn.mortesDiariasPaises(paisInformado)

def grafico_mapa_mortes():
    gpbtn.mapaPaises('mortes')

def grafico_mapa_casos():
    gpbtn.mapaPaises('casos')

def grafico_pizza_casos():
    numeroPaisesInformado = entry.get()
    if numeroPaisesInformado == '':
        numeroPaisesInformado = 0
    else:
        numeroPaisesInformado = int(numeroPaisesInformado)

    if numeroPaisesInformado <= 0:
        print('É necessário informar o número de países a serem listados no campo')
    else:   
        gpbtn.pizzaNovosCasos(numeroPaisesInformado)

def grafico_pizza_mortes():    
    numeroPaisesInformado = entry.get()

    if numeroPaisesInformado == '':
        numeroPaisesInformado = 0
    else:
        numeroPaisesInformado = int(numeroPaisesInformado)

    if numeroPaisesInformado <= 0:
        print('É necessário informar o número de países a serem listados no campo')
    else:  
        gpbtn.pizzaNovasMortes(numeroPaisesInformado)


# Crie a janela principal
window = tk.Tk()
window.title("Janela Principal")

# Defina a geometria da janela principal (largura x altura)
window.geometry("400x400")

# Crie um widget Entry para a entrada de texto
entry = tk.Entry(window, width=30)
entry.pack(side=tk.TOP, pady=20)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela com casos diários
open_button_casos_diarios = tk.Button(window, text="Casos Diários por País", command=grafico_casos_diarios)
open_button_casos_diarios.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela com mortes diárias
open_button_mortes_diarias = tk.Button(window, text="Mortes Diárias por País", command=grafico_mortes_diarias)
open_button_mortes_diarias.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela com o mapa de mortes
open_button_mapa_mortes = tk.Button(window, text="Mapa de Mortes", command=grafico_mapa_mortes)
open_button_mapa_mortes.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela com o mapa de mortes
open_button_mapa_casos = tk.Button(window, text="Mapa de Casos", command=grafico_mapa_casos)
open_button_mapa_casos.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela com o mapa de mortes
open_button_pizza_casos = tk.Button(window, text="Gráfico de Pizza de Casos", command=grafico_pizza_casos)
open_button_pizza_casos.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela com o mapa de mortes
open_button_pizza_mortes = tk.Button(window, text="Gráfico de Pizza de Mortes", command=grafico_pizza_mortes)
open_button_pizza_mortes.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Execute o loop de eventos do Tkinter
window.mainloop()
