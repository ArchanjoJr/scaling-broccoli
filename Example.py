from tkinter import*
import statistics

janela1 = Tk()
j1n = DoubleVar(janela1)
j1xy = DoubleVar(janela1)
j1ex = DoubleVar(janela1)
j1ey = DoubleVar(janela1)
j1ex2 = DoubleVar(janela1)
j1resultado = DoubleVar(janela1)

def Regressao_linearA(e):
    a = j1n.get() * j1xy.get()
    b = j1ex.get() * j1ey.get()
    c = j1n.get() * j1ex2.get()
    d = j1ex.get() * j1ex.get()
    j1resultado.set((a-b)/(c-d))

j1lb1 = Label(janela1, text = "N: ",font = ("helvetica",20))
j1lb2 = Label(janela1, text = "∑XY: ",font = ("helvetica",20))
j1lb3 = Label(janela1, text = "∑X: ",font = ("helvetica",20))
j1lb4 = Label(janela1, text = "∑Y: ",font = ("helvetica",20))
j1lb5 = Label(janela1, text = "∑X²: ",font = ("helvetica",20))
j1lb6 = Label(janela1, text = "RESULTADO =(A): ",font = ("helvetica",20))

j1eb1 = Entry(textvar = j1n,font = ("helvetica",20))
j1eb2 = Entry(textvar = j1xy,font = ("helvetica",20))
j1eb3 = Entry(textvar = j1ex,font = ("helvetica",20))
j1eb4 = Entry(textvar = j1ey,font = ("helvetica",20))
j1eb5 = Entry(textvar = j1ex2,font = ("helvetica",20))
j1eb6 = Label(textvar = j1resultado,font = ("helvetica",20))

j1bt1 = Button(text = "CALCULAR",font = ("helvetica",20))
j1bt1.bind("<Button-1>",Regressao_linearA)
j1bt2 = Button(janela1, text = "LIMPAR")

j1lb1.grid(row=0, column=0)
j1lb2.grid(row=1, column=0)
j1lb3.grid(row=2, column=0)
j1lb4.grid(row=3, column=0)
j1lb5.grid(row=4, column=0)
j1lb6.grid(row=5, column=0)

j1eb1.grid(row=0, column=1)
j1eb2.grid(row=1, column=1)
j1eb3.grid(row=2, column=1)
j1eb4.grid(row=3, column=1)
j1eb5.grid(row=4, column=1)
j1eb6.grid(row=5, column=1)

j1bt1.grid(row=6, column=1)
#j1bt2.grid(row=6, column=1)

janela1.geometry("600x330+50+165")
janela1.mainloop()


janela2 = Tk()
j2y = DoubleVar(janela2)
j2A = DoubleVar(janela2)
j2x = DoubleVar(janela2)
j2n = DoubleVar(janela2)
j2resultado = DoubleVar(janela2)

def Regressao_linearB(e):
    a = j2y.get()
    b = j2A.get() * j2x.get()
    c = j2n.get()
    j2resultado.set((a - b)/c)

j2lb1 = Label(janela2, text = "∑Y: ",font = ("helvetica",20))
j2lb2 = Label(janela2, text = "valor de A: ",font = ("helvetica",20))
j2lb3 = Label(janela2, text = "∑X: ",font = ("helvetica",20))
j2lb4 = Label(janela2, text = "N: ",font = ("helvetica",20))
j2lb6 = Label(janela2, text = "RESULTADO =(B): ",font = ("helvetica",20))


j2eb1 = Entry(textvar = j2y,font = ("helvetica",20))
j2eb2 = Entry(textvar = j2A,font = ("helvetica",20))
j2eb3 = Entry(textvar = j2x,font = ("helvetica",20))
j2eb4 = Entry(textvar = j2n,font = ("helvetica",20))
j2eb6 = Label(textvar = j2resultado,font = ("helvetica",20))

j2bt1 = Button(text = "CALCULAR",font = ("helvetica",20))
j2bt1.bind("<Button-1>",Regressao_linearB)
j2bt2 = Button(janela2, text = "LIMPAR")

j2lb1.grid(row=0, column=0)
j2lb2.grid(row=1, column=0)
j2lb3.grid(row=2, column=0)
j2lb4.grid(row=3, column=0)
j2lb6.grid(row=5, column=0)


j2eb1.grid(row=0, column=1)
j2eb2.grid(row=1, column=1)
j2eb3.grid(row=2, column=1)
j2eb4.grid(row=3, column=1)
j2eb6.grid(row=5, column=1)

j2bt1.grid(row=6, column=1)

janela2.geometry("600x330+50+165")
janela2.mainloop()


janela3 = Tk()
j3y = DoubleVar(janela3)
j3B = DoubleVar(janela3)
j3ey = DoubleVar(janela3)
j3A = DoubleVar(janela3)
j3exy = DoubleVar(janela3)
j3n = DoubleVar(janela3)
j3resultado = DoubleVar(janela3)

def Erro_padrao(e):
    a = j3y.get()
    b = j3B.get()* j3ey.get()
    c = j3A.get()* j3exy.get()
    d = j3n.get()
    f = ((a-b-c)/(d-2))
    g = (f ** (1/2))
    j3resultado.set(g)

j3lb1 = Label(janela3, text = "∑Y²: ",font = ("helvetica",20))
j3lb2 = Label(janela3, text = "valor de B: ",font = ("helvetica",20))
j3lb3 = Label(janela3, text = "∑Y: ",font = ("helvetica",20))
j3lb4 = Label(janela3, text = "valor de A: ",font = ("helvetica",20))
j3lb5 = Label(janela3, text = "∑XY: ",font = ("helvetica",20))
j3lb6 = Label(janela3, text = "N: ",font = ("helvetica",20))
j3lb7 = Label(janela3, text = "RESULTADO ERRO PADRÃO: ",font = ("helvetica",20))

j3eb1 = Entry(textvar = j3y,font = ("helvetica",20))
j3eb2 = Entry(textvar = j3B,font = ("helvetica",20))
j3eb3 = Entry(textvar = j3ey,font = ("helvetica",20))
j3eb4 = Entry(textvar = j3A,font = ("helvetica",20))
j3eb5 = Entry(textvar = j3exy,font = ("helvetica",20))
j3eb6 = Entry(textvar = j3n,font = ("helvetica",20))
j3eb7 = Label(textvar = j3resultado,font = ("helvetica",20))

j3bt1 = Button(text = "CALCULAR",font = ("helvetica",20))
j3bt1.bind("<Button-1>",Erro_padrao)
j3bt2 = Button(janela3, text = "LIMPAR")

j3lb1.grid(row=0, column=0)
j3lb2.grid(row=1, column=0)
j3lb3.grid(row=2, column=0)
j3lb4.grid(row=3, column=0)
j3lb5.grid(row=4, column=0)
j3lb6.grid(row=5, column=0)
j3lb7.grid(row=6, column=0)

j3eb1.grid(row=0, column=1)
j3eb2.grid(row=1, column=1)
j3eb3.grid(row=2, column=1)
j3eb4.grid(row=3, column=1)
j3eb5.grid(row=4, column=1)
j3eb6.grid(row=5, column=1)
j3eb7.grid(row=6, column=1)

j3bt1.grid(row=7, column=1)

lb1 = Label(janela3,text = "Y= ",font = ("helvetica",40))
lb2 = Label(janela3,text = "X +",font = ("helvetica",40))
lb3 = Label(textvar = j3A,font = ("helvetica",40))
lb4 = Label(textvar = j3B,font = ("helvetica",40))

lb1.grid(row=8, column=0)
lb2.grid(row=8, column=2)
lb3.grid(row=8, column=1)
lb4.grid(row=8, column=3)

janela3.geometry("900x450+50+165")
janela3.mainloop()


