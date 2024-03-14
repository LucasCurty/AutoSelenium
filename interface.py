import tkinter as tk
from tkinter import filedialog, Button

janela = tk.Tk()
janela.title("Bem vindo!")
janela.geometry("500x250+300+250")

#Definindo função de abertura de pasta
def OpenFolder():
    resp = filedialog.askdirectory()
    print(resp)

label = tk.Label(janela, text="Teste de janelas", font=('Arial Bold',12))
label.grid(column=0, row=0)

Button(janela, text='Pasta', command=OpenFolder).grid(column=0, row=1)



janela.mainloop()

