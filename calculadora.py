import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title('Calculadora')
        self.janela.geometry('300x600')


calculadora = tk.Tk()
Tela(calculadora)
calculadora.mainloop()