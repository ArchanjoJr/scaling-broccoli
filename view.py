from tkinter import *
from Model import *


def dist():
    lbl_title.config(text='Distribuiçao')

def p():
    lbl_title.config(text='Probababilidade')


master = Tk()
master.title('Estatistica !')
master.geometry('400x400')
menu=Menu(master)
master.config(menu=menu)
menu.add_command(label='Distr. Nominal', command=dist)
menu.add_command(label='Probabilidade',command=p)
lbl_title = Label(master, text='', font=('italic', 20), justify=CENTER)
lbl_title.pack()
'''
btn_top = Button(master, text='PROBABILIDADE', padx=10, pady=15, command=p)
btn_top.pack(side=LEFT,anchor=N)
btn_top = Button(master, text='DISTR. NOMINAL', padx=10, pady=15, command=dist)
btn_top.pack(side=LEFT,anchor=NE)
lbl_title = Label(master, text='', font=('italic', 20), justify=CENTER)
lbl_title.pack()
btn_close=Button(master,text='Close',command=master.quit)
btn_close.pack(side=BOTTOM)
'''
master.mainloop()

'''
princ.title('Dealing with Buttons Now !')
princ.config(bg='red')
texto= StringVar()
texto.set('damn Daniel')
Message(princ,text='U KNOW WHAT THEY SAY ABOUT THE CRAZIES ONE !',relief='ridge',justify='center',bg='green',font=('times',20),bd=20,textvariable=texto).pack()
Button(princ,text='Close',command=princ.destroy).pack()
princ.mainloop()
'''
'''
princ.title('Dealing with Buttons Now !')
bt_print= Button(princ,padx=15,text='PRESS ME',fg='yellow',bg='green',command=prin,width=10)
bt_print.pack(side='right')
bt_close= Button(princ,padx=10,text='Close Me',fg='white',bg='red',command=princ.destroy,width=25)
bt_close.pack(side='left')
princ.mainloop()
'''
'''
princ.title('Dealing with Radion Buttons now !')
v= IntVar()
def showv():
    print(v.get())
Label(princ,text='HELLO DARKNESS MY OLD FRIEND',justify='center').pack()
answers = [
    ("I've Come To Talk with You Again",1),
    ("I Like to Talk with you Again",2),
    ("I Would love to Eat With You Again",3),
    ("I Hope To Never See You Again",4),
    ("SHALA LALA LALA",5)
]
for text,value in answers:
    Radiobutton(princ,text=text,value=value,variable=v,justify='left',padx=20).pack(anchor='w')

Button(princ,text='Exit', fg='White',bg='red',command=princ.destroy,padx=15,width=15).pack(side='right')
Button(princ,text='print', bg='green',command=showv,padx=15,width=15).pack(side='left')                
princ.mainloop()
'''
'''
princ.title('Dealing with entries/FORM')
def somar():
    c.insert(0,(str(int(a.get())+int(b.get()))))
def valores():
    print(int(a.get())+int(b.get()))
    a.delete(0,END),b.delete(0,END)
Label(princ,text='A=',pady=4).grid(row=0)
a = Entry(princ)
a.grid(row=0,column=1)
Label(princ,text='B=',pady=4).grid(row=1)
b = Entry(princ)
b.grid(row=1,column=1)
Label(princ,text='SOMA=',pady=4).grid(row=4)
c = Entry(princ)
a.insert(10,'23')
b.insert(10,'43')
c.grid(row=4,column=1)
Button(princ,bg='red',text='close',command=princ.destroy).grid(row=3,column=1)
Button(princ,bg='GREEN',text='Somar',command=somar).grid(row=3,column=0)
princ.mainloop()
'''
'''
princ.title('Dealing with sliders')
scl_1 = Scale(princ,from_=0,to=20)
scl_1.pack()
scl_2 = Scale(princ,from_=0, to=120,orient=HORIZONTAL)
scl_2.pack()
princ.mainloop()
'''
'''
princ.title('Dealing with Menus')
def dist_nominal():
    print('Distribuicao Nominal')
def Proba():
    print('Tela de Probabilidades')
menu_main= Menu(princ)
princ.config(menu=menu_main)
file_menu= Menu(menu_main)
menu_main.add_cascade(label='file',menu=file_menu)
file_menu.add_command(label='exit',command=princ.destroy)
princ.mainloop()
'''
