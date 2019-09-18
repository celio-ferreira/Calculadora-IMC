from tkinter import *


def abrir():
    abre = open('SistemaDeCadastro.py')
    return abre


master = Tk()
master.title("CADASTRO")
master.geometry("1920x1080")
master.iconbitmap(default="icons/cad.ico")



menu = Menu(master)
master.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="CADASTRO", menu=submenu)
submenu.add_command(label="NOVO CADASTRO", command=abrir)

master.mainloop()
