
from tkinter import *

janela = Tk()
janela.title("Conversor de Dólar")
janela.geometry("300x500")
janela.resizable(False, False)
janela.config(background='#4ed08d')

def converter():
    dolar = float(text_dolar.get())
    real = dolar * 5
    text_real.insert(0, real)

def limpar():
    text_dolar.delete(0, END)    
    text_real.delete(0, END)

frame_dolar = Frame(janela, borderwidth=2, relief='solid')
label_dolar = Label(janela, text="Dólar")
text_dolar = Entry(frame_dolar, width=38)

frame_real = Frame(janela, borderwidth=2, relief='solid')
label_real = Label(janela, text="Real")
text_real = Entry(frame_real, width=38)
botao_converter = Button(janela, text="Converter", command=converter)
apagar = Button(janela, text="Limpar", command=limpar)

frame_dolar.place(x=23, y=165, width=250, height=40)
label_dolar.place(x=23, y=160)
text_dolar.place(x=5, y=10)

frame_real.place(x=23, y=235, width=250, height=40)
label_real.place(x=23, y=225)
text_real.place(x=5, y=10)

botao_converter.place(x=115, y=290)
apagar.place(x=120, y=320)


janela.mainloop()