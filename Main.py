import Model
import tkinter
from tkinter.constants import *
lista='10 11 13 13 14 16 16 17 17 19 20 20 21 21 22 23 23 23 24 25 25 26 27 27 28 29 30 30 31 32 32 32 33 33 34 ' \
      '35 36 38 38 39 40 41 43 44 45 45 46 48 49 50 52 53 53 54 58 62 63 65 70 78'
r = Model.rol(lista)
aux = len(r)
jan1=tkinter.Tk()
jan1.title("Distribuição Nominal")
jan1lbn = tkinter.Label(jan1,text='N',font=('comic sans',40))
jan1lbk = tkinter.Label(jan1,text='K')
jan1lbp = tkinter.Label(jan1,text='P')
jan1lbq = tkinter.Label(jan1,text='Q')

jan1.mainloop()

