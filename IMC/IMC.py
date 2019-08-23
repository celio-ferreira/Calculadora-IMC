from tkinter import *
from tkinter import ttk


#JANELA PRINCIPAL
jan = Tk()
jan.geometry("270x270+550+250")
jan.title("IMC")
jan.resizable(width="false", height="false")
jan.iconbitmap(default="icons/imc.ico")
jan.configure(background="#00FF7F")

#FRAMES
TopFrame = Frame(jan, width=270, height=110, bg="#98FB98", borderwidth=1, relief="solid")
TopFrame.pack(side=TOP)
BottomFrame = Frame(jan, width=270, height=155, bg="#98FB98", borderwidth=1, relief="solid")
BottomFrame.pack(side=BOTTOM)

#LABELS
PesoLabel = Label(TopFrame, text="PESO", bg="#98FB98", font=("century gothic, bold", 13))
PesoLabel.place(x=10, y=15)
KgLabel = Label(TopFrame, text="Kg", bg="#98FB98", font=("century gothic, bold", 9))
KgLabel.place(x=215, y=13)
AlturaLabel = Label(TopFrame, text="ALTURA", bg="#98FB98", font=("century gothic, bold", 13))
AlturaLabel.place(x=10, y=45)
ImcLabel = Label(BottomFrame, text="IMC =", bg="#98FB98", font=("century gothic, bold", 13))
ImcLabel.place(x=20, y=10)
ImcResult = Label(BottomFrame, width=8, height=1, font=("bold", 15), bg="#98FB98")
ImcResult.place(x=105, y=8)
AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid")
AvaliaLabel.place(x=10, y=40)

#ENTRADAS DE DADOS
PesoEntry = ttk.Entry(TopFrame, width=12, font=("bold"))
PesoEntry.place(x=100, y=15)
PesoEntry.focus()
AlturaEntry = ttk.Entry(TopFrame, width=12, font=("bold"))
AlturaEntry.place(x=100, y=45)

#FUNÇÕES
def calcular(event):
    peso = PesoEntry.get()
    altura = AlturaEntry.get()
    resp = float(peso) / (float(altura) * float(altura))
    ImcResult["text"] = (f'{resp:.1f}')
    if resp < 17:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="#FF7F50")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("ATENÇÃO!\nPESO MUITO ABAIXO DO NORMAL!")
    elif resp <= 18.49:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="yellow")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("VOCÊ ESTÁ ABAIXO DO PESO!")
    elif resp <= 24.9:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="#00FF7F")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("PARABÉNS!\nSEU PESO ESTÁ DENTRO DO RECOMENDADO!")
    elif resp <= 29.9:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="yellow")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("VOCÊ ESTÁ ACIMA DO PESO!\nPRATIQUE EXERCÍCIOS FÍSICOS.")
    elif resp <= 34.9:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="#FF7F50")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("ATENÇÃO!\nVOCÊ ESTÁ COM OBESIDADE\nNÍVEL I.\nPROCURE UM MÉDICO!")
    elif resp <= 39.9:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="#FF7F50")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("ATENÇÃO!\nVOCÊ ESTÁ COM OBESIDADE\nNÍVEL II SEVERA!\nPROCURE UM ESPECIALISA!")
    elif resp >= 40:
        AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="#FF7F50")
        AvaliaLabel.place(x=10, y=40)
        AvaliaLabel["text"] = ("ATENÇÃO!\nVOCÊ ESTÁ COM OBESIDADE MÓRBIDA\nNÍVEL III\nPROCURE UM ESPECIALISA!")
def clear(event):
    PesoEntry.delete(first=0, last=10)
    AlturaEntry.delete(first=0, last=10)
    ImcResult["text"] = ("")
    AvaliaLabel = Label(BottomFrame, width=35, height=6, borderwidth=1, relief="solid", bg="white")
    AvaliaLabel.place(x=10, y=40)
    AvaliaLabel["text"] = (f'{" "}')

#BOTÕES
CalcButton = ttk.Button(TopFrame, text="CALCULAR")
CalcButton.bind("<Return>", calcular)
CalcButton.bind("<Button -1>", calcular)
CalcButton.place(x=90, y=80)

LimpaButton = ttk.Button(TopFrame, text="LIMPAR")
LimpaButton.bind("<Return>", clear)
LimpaButton.bind("<Button -1>", clear)
LimpaButton.place(x=170, y=80)

jan.mainloop()


