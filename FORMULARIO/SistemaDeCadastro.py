from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import CadastroDb



#JANELA PRINCIPAL
master = Tk()
master.title("CADASTRO")
master.geometry("1920x1080")
master.iconbitmap(default="icons/cad.ico")

#FUNÇÕES:
def limpar(event):
    NomeEntry.delete(first=0, last=100)
    LogEntry.delete(first=0, last=100)
    NumEntry.delete(first=0, last=100)
    BairroEntry.delete(first=0, last=100)
    CepEntry.delete(first=0, last=100)
    CidadeEntry.delete(first=0, last=100)
    UfEntry.delete(first=0, last=100)
    CpfEntry.delete(first=0, last=100)
    RgEntry.delete(first=0, last=100)
    NascEntry.delete(first=0, last=100)
    EmailEntry.delete(first=0, last=100)
    TelEntry.delete(first=0, last=100)
    CelEntry.delete(first=0, last=100)


def Armazenar():
    NOME = NomeEntry.get()
    LOG = LogEntry.get()
    NUM = NumEntry.get()
    BAI = BairroEntry.get()
    CEP = CepEntry.get()
    CID = CidadeEntry.get()
    UF = UfEntry.get()
    CPF = CpfEntry.get()
    RG = RgEntry.get()
    NASC = NascEntry.get()
    EMAIL = EmailEntry.get()
    TEL = TelEntry.get()
    CEL = CelEntry.get()
    CadastroDb.cursor.execute("INSERT INTO cadastro (Cpf, Nome, Rg, Nasc, Email) VALUES(%s, %s, %s, %s, %s)", (CPF, NOME, RG, NASC, EMAIL))
    CadastroDb.conn.commit()
    CadastroDb.cursor.execute("INSERT INTO telefone(CPF, Tel, Cel) VALUES (%s, %s, %s)", (CPF, TEL, CEL))
    CadastroDb.conn.commit()
    messagebox.showinfo(title="Registro de Informações", message="Informações Cadastradas Com Sucesso!")

#FRAMES
TopFrame = Frame(master, width=1920, height=80, bg='grey')
TopFrame.pack(side=TOP)
BottomFrame = Frame(master, width=1200, height=750, bg='grey')
BottomFrame.pack(side=BOTTOM)

#LABEL TÍTULO PRINCIPAL
TextTitle = Label(TopFrame, text='CADASTRO', font=("Arial", 20, "bold"), bg="grey", fg="white")
TextTitle.place(x=650, y=25)

#WIDGETS LABELS

NomeLabel = Label(BottomFrame, text="NOME", font=("times", 14, "bold"))
NomeLabel.place(x=10, y=15)
LogLabel = Label(BottomFrame, text="LOGRADOURO", font=("times", 14, "bold"))
LogLabel.place(x=10, y=55)
NumLabel = Label(BottomFrame, text="Nº", font=("times", 14, "bold"))
NumLabel.place(x=1090, y=55)
BairroLabel = Label(BottomFrame, text="BAIRRO", font=("times", 14, "bold"))
BairroLabel.place(x=10, y=95)
CepLabel = Label(BottomFrame, text="CEP", font=("times", 14, "bold"))
CepLabel.place(x=910, y=95)
CidadeLabel = Label(BottomFrame, text="CIDADE", font=("times", 14, "bold"))
CidadeLabel.place(x=10, y=135)
UfLabel = Label(BottomFrame, text="UF", font=("times", 14, "bold"))
UfLabel.place(x=910, y=135)
CpfLabel = Label(BottomFrame, text="CPF", font=("times", 14, "bold"))
CpfLabel.place(x=10, y=175)
RgLabel = Label(BottomFrame, text="RG.",  font=("times", 14, "bold"))
RgLabel.place(x=210, y=175)
NascLabel = Label(BottomFrame, text="DATA NASC.",  font=("times", 14, "bold"))
NascLabel.place(x=415, y=175)
EmailLabel = Label(BottomFrame, text="E-MAIL", font=("times", 14, "bold"))
EmailLabel.place(x=650, y=175)
TelLabel = Label(BottomFrame, text="TELEFONE", font=("times", 14, "bold"))
TelLabel.place(x=10, y=215)
CelLabel = Label(BottomFrame, text="CELULAR", font=("times", 14, "bold"))
CelLabel.place(x=290, y=215)
ObsLabel = Label(BottomFrame, text="Observações")
ObsLabel.place(x=10, y=260)
MsgLabel = scrolledtext.ScrolledText(BottomFrame, width=83, height=10, font=("times", 20))
MsgLabel.place(x=10, y=285)

#WIDGETS ENTRADAS
NomeEntry = ttk.Entry(BottomFrame, width=100, font=("times", 15))
NomeEntry.place(x=80, y=15)
NomeEntry.focus()
LogEntry = ttk.Entry(BottomFrame, width=92, font=("times", 15))
LogEntry.place(x=160, y=55)
NumEntry = ttk.Entry(BottomFrame, width=6, font=("times", 15))
NumEntry.place(x=1120, y=55)
BairroEntry = ttk.Entry(BottomFrame, width=80, font=("times", 15))
BairroEntry.place(x=95, y=95)
CepEntry = ttk.Entry(BottomFrame, width=10, font=("times", 15))
CepEntry.place(x=960, y=95)
CidadeEntry = ttk.Entry(BottomFrame, width=80, font=("times", 15))
CidadeEntry.place(x=95, y=135)
UfEntry = ttk.Entry(BottomFrame, width=3, font=("times", 15))
UfEntry.place(x=945, y=135)
CpfEntry = ttk.Entry(BottomFrame, width=14, font=("times", 15))
CpfEntry.place(x=58, y=175)
RgEntry = ttk.Entry(BottomFrame, width=15, font=("times", 15))
RgEntry.place(x=255, y=175)
NascEntry = ttk.Entry(BottomFrame, width=10, font=("times", 15))
NascEntry.place(x=540, y=175)
EmailEntry = ttk.Entry(BottomFrame, width=45, font=("times", 15))
EmailEntry.place(x=730, y=175)
TelEntry = ttk.Entry(BottomFrame, width=15, font=("times", 15))
TelEntry.place(x=125, y=215)
CelEntry = ttk.Entry(BottomFrame, width=15, font=("times", 15))
CelEntry.place(x=390, y=215)

#BOTÕES
BtCadastra = ttk.Button(BottomFrame, text="CADASTRAR", width=25, command=Armazenar)
BtCadastra.bind("<Return>", limpar)
BtCadastra.bind("<Button -1>", limpar)
BtCadastra.place(x=370, y=650)

BtLimpar = ttk.Button(BottomFrame, text="LIMPAR", width=25)
BtLimpar.bind("<Return>", limpar)
BtLimpar.bind("<Button -1>", limpar)
BtLimpar.place(x=550, y=650)

master.mainloop()
