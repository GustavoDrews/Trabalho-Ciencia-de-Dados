import tkinter as tk
import graficosParaBotoes as gpbtn

def grafico_por_pais():
    paisInformado = entry.get()
    gpbtn.casosDiariosPaises(paisInformado)

# Crie a janela principal
window = tk.Tk()
window.title("Janela Principal")

# Defina a geometria da janela principal (largura x altura)
window.geometry("400x200")

# Crie um widget Entry para a entrada de texto
entry = tk.Entry(window, width=30)
entry.pack(side=tk.TOP, pady=20)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Crie um botão para abrir uma nova janela
open_button = tk.Button(window, text="Gráfico por País", command=grafico_por_pais)
open_button.pack(side=tk.TOP, pady=10)  # Use side=tk.TOP para alinhar ao topo e adicione pady para espaçamento

# Execute o loop de eventos do Tkinter
window.mainloop()
