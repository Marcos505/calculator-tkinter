import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title('Calculadora')
        self.janela.geometry('300x600')

        #Adicionado os botões numericos
        self.bnt_1 = tk.Button(self.janela, text='7', width=8, height=4)
        self.bnt_1.grid(row=1, column=0)
        self.bnt_2 = tk.Button(self.janela, text='8', width=8, height=4)
        self.bnt_2.grid(row=1, column=1)
        self.bnt_3 = tk.Button(self.janela, text='9', width=8, height=4)
        self.bnt_3.grid(row=1, column=2)
        self.bnt_4 = tk.Button(self.janela, text='4', width=8, height=4)
        self.bnt_4.grid(row=2, column=0)
        self.bnt_5 = tk.Button(self.janela, text='5', width=8, height=4)
        self.bnt_5.grid(row=2, column=1)
        self.bnt_6 = tk.Button(self.janela, text='6', width=8, height=4)
        self.bnt_6.grid(row=2, column=2)
        self.bnt_7 = tk.Button(self.janela, text='1', width=8, height=4)
        self.bnt_7.grid(row=3, column=0)
        self.bnt_8 = tk.Button(self.janela, text='2', width=8, height=4)
        self.bnt_8.grid(row=3, column=1)
        self.bnt_9 = tk.Button(self.janela, text='7', width=8, height=4)
        self.bnt_9.grid(row=3, column=2)
        self.bnt_10 = tk.Button(self.janela, text='0', width=18, height=4)
        self.bnt_10.grid(row=4,columnspan=2, column=0)

        #Adicionando botões de operações e resultado
        self.bnt_div = tk.Button(self.janela, text='/', width=18, height=4)
        self.bnt_div.grid(row=0,columnspan=2, column=0)
        self.bnt_mult = tk.Button(self.janela, text='*', width=18, height=4)
        self.bnt_mult.grid(row=0,columnspan=3, column=2)
        self.bnt_sub = tk.Button(self.janela, text='-', width=8, height=9)
        self.bnt_sub.grid(row=1,rowspan=2, column=4)
        self.bnt_adc = tk.Button(self.janela, text='+', width=8, height=9)
        self.bnt_adc.grid(row=3,rowspan=2, column=4)
        self.bnt_result = tk.Button(self.janela, text='=', width=8, height=4)
        self.bnt_result.grid(row=4, column=2)
   

calculadora = tk.Tk()
Tela(calculadora)
calculadora.mainloop()