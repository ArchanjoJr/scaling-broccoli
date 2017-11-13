from tkinter import *


def env_dist():
    print('enviar resposta aqui')


def dist():
    lbl_title.config(text='Distribuiçao Nominal')
    texto = ['N = ', 'K = ', 'P = ', 'Q = ']
    lbl_e.place_forget()
    for x in range(4):
        obj[x].set(texto[x])
    Button(master, text='Calcular', command=env_dist, width=12).place(x=190, y=430)




master = Tk()
master.title('Estatistica !')
master.geometry('500x500')
menu = Menu(master)
master.config(menu=menu)
menu.add_command(label='Distr. Nominal', command=dist)
lbl_title = Label(master, text='', font=('italic', 20), justify=CENTER)
lbl_title.place(x=138)
text_a = StringVar();text_b = StringVar();text_c = StringVar();text_d = StringVar();text_e = StringVar()
obj = [text_a, text_b, text_c, text_d, text_e]
lbl_a = Label(master, textvariable=text_a, font=('helvetica', 22, 'bold'))
lbl_a.place(x=10, y=50)
lbl_b = Label(master, textvariable=text_b, font=('helvetica', 22, 'bold'))
lbl_b.place(x=10, y=130)
lbl_c = Label(master, textvariable=text_c, font=('helvetica', 22, 'bold'))
lbl_c.place(x=10, y=210)
lbl_d = Label(master, textvariable=text_d, font=('helvetica', 22, 'bold'))
lbl_d.place(x=10, y=300)
lbl_e = Label(master, textvariable=text_e, font=('helvetica', 22, 'bold'))
lbl_e.place(x=10, y=380)
btn_close = Button(master, text='Close', command=master.quit)
btn_close.place(y=473, x=220)
master.mainloop()