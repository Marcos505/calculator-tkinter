import tkinter as tk
from tkinter import messagebox
import base64

class Tela():
    def __init__(self,master):
        self.janela = master
        self.janela.title("Calculadora")
        self.janela.iconbitmap("calculator-icon.ico")
        self.janela.geometry("220x220+750+200")

        #FRAMES
        self.frm_resultado = tk.Frame(self.janela)
        self.frm_resultado.pack()
        self.frm_botoes = tk.Frame(self.janela)
        self.frm_botoes.pack()
        self.frm_footer = tk.Frame(self.janela)
        self.frm_footer.pack()
        

        # ENTRY ONDE SE MOSTRA AS OPERAÇÕES
        self.ent_resultado = tk.Entry(self.frm_resultado, width=34)
        self.ent_resultado.grid(row=0, column=0, pady=10)

        #CRIANDO E IMPLEMENTANDO OS BOTÕES DE 0 A 9
        self.btn = tk.Button(self.frm_botoes, width=5, text=1, relief="groove", command=lambda:self.clique(1))
        self.btn.grid(row=0, column=0, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=2, relief="groove", command=lambda:self.clique(2))
        self.btn.grid(row=0, column=1, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=3, relief="groove", command=lambda:self.clique(3))
        self.btn.grid(row=0, column=2, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=4, relief="groove", command=lambda:self.clique(4))
        self.btn.grid(row=1, column=0, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=5, relief="groove", command=lambda:self.clique(5))
        self.btn.grid(row=1, column=1, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=6, relief="groove", command=lambda:self.clique(6))
        self.btn.grid(row=1, column=2, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=7, relief="groove", command=lambda:self.clique(7))
        self.btn.grid(row=2, column=0, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=8, relief="groove", command=lambda:self.clique(8))
        self.btn.grid(row=2, column=1, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=9, relief="groove", command=lambda:self.clique(9))
        self.btn.grid(row=2, column=2, pady=5, padx=5)
        self.btn = tk.Button(self.frm_botoes, width=5, text=0, relief="groove", command=lambda:self.clique(0))
        self.btn.grid(row=3, column=1)
    
        #CRIANDO E IMPLEMENTANDO OS  BOTÕES DOS OPERADORES
        self.btn_soma = tk.Button(self.frm_botoes, width=5, text="+", command=self.soma, relief="groove")
        self.btn_soma.grid(row=0, column=3, padx=5)

        self.btn_sub = tk.Button(self.frm_botoes, width=5, text="-", command=self.sub, relief="groove")
        self.btn_sub.grid(row=1, column=3, padx=5)

        self.btn_mult = tk.Button(self.frm_botoes, width=5, text="x", command=self.mult, relief="groove")
        self.btn_mult.grid(row=2, column=3, padx=5)

        self.btn_div = tk.Button(self.frm_botoes, width=5, text="÷", command=self.div, relief="groove")
        self.btn_div.grid(row=3, column=3, padx=5)

        self.btn_apagar = tk.Button(self.frm_botoes, width=5, text="C", command=self.deletar, relief="groove")
        self.btn_apagar.grid(row=3, column=0, padx=5)

        self.btn_reslt = tk.Button(self.frm_botoes, width=5, text="=", command=self.resul, relief="groove")
        self.btn_reslt.grid(row=3, column=2, padx=5)

        #CRIANDO UM FOOTER
        self.lbl_footer = tk.Label(self.frm_footer, text="by MARCOS G. S. ROCHA")
        self.lbl_footer.grid(row=0, column=0, pady=25)

    #FUNÇÕES
    def clique(self, clicado):
        atual = self.ent_resultado.get()
        self.ent_resultado.delete(0, tk.END)
        self.ent_resultado.insert(0, str(atual) + str(clicado))
        return
    
    def deletar(self):
        self.ent_resultado.delete(0, tk.END)
        return
    
    def soma(self):
        self.atual = self.ent_resultado.get()
        self.numero1 = 0
        self.operacao = "soma"
        self.numero1 = int(self.atual)
        self.ent_resultado.delete(0, tk.END)

    def mult(self):
        self.atual = self.ent_resultado.get()
        self.numero1 = 0
        self.operacao = "mult"
        self.numero1 = int(self.atual)
        self.ent_resultado.delete(0, tk.END)

    def div(self):
        self.atual = self.ent_resultado.get()
        self.numero1 = 0
        self.operacao = "div"
        self.numero1 = int(self.atual)
        self.ent_resultado.delete(0, tk.END)

    def sub(self):
        self.atual = self.ent_resultado.get()
        self.numero1 = 0
        self.operacao = "sub"
        self.numero1 = int(self.atual)
        self.ent_resultado.delete(0, tk.END)

    def resul(self):
        self.atual = self.ent_resultado.get()
        self.ent_resultado.delete(0, tk.END)
        if self.operacao == "soma":
            self.ent_resultado.insert(0, self.numero1 + int(self.atual))  # type: ignore
        elif self.operacao == "div":
            if self.numero1 == 0:
                messagebox.showerror('Aviso', 'Não é possível dividir por zero.')
            self.ent_resultado.insert(0, self.numero1 / int(self.atual))  # type: ignore
            print(self.atual)
        elif self.operacao == "sub":
            self.ent_resultado.insert(0, self.numero1 - int(self.atual))  # type: ignore
        elif self.operacao == "mult":
            self.ent_resultado.insert(0, self.numero1 * int(self.atual))  # type: ignore

# Tratar para resolver o erro que acontece quando se aperta o "=".