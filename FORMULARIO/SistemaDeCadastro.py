from tkinter import *
from tkinter import ttk
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
    CompEntry.delete(first=0, last=100)
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
    MsgLabel.delete(1.0, END)


def Armazenar():
    messagebox.askyesno(title="Armazenar", message="Deseja Armazenar as Informações?")
    LOG = LogEntry.get()
    NUM = NumEntry.get()
    COMP = CompEntry.get()
    BAI = BairroEntry.get()
    CID = CidadeEntry.get()
    CEP = CepEntry.get()
    UF = UfEntry.get()
    CadastroDb.cursor.execute("""INSERT INTO endereço(Logradouro, Num, Complemento, Bairro, Cidade, Cep, Uf, Id_End)
     VALUES(%s, %s, %s, %s, %s, %s, %s, default)""", (LOG, NUM, COMP, BAI, CID, CEP, UF))
    CadastroDb.conn.commit()
    NOME = NomeEntry.get()
    RG = RgEntry.get()
    CPF = CpfEntry.get()
    NASC = NascEntry.get()
    EMAIL = EmailEntry.get()
    TEL = TelEntry.get()
    CEL = CelEntry.get()
    MSG = MsgLabel.get(1.0, END)
    IDEND = CadastroDb.cursor.lastrowid
    CadastroDb.cursor.execute("""insert into cadastro(Id, Nome, Rg, Cpf, Nasc, Email, Telefone, Celular, Observações, Id_End)
     values(default, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (NOME, RG, CPF, NASC, EMAIL, TEL, CEL, MSG, IDEND))
    CadastroDb.conn.commit()
    messagebox.showinfo(title="Registro de Informações", message="Informações Cadastradas Com Sucesso!")
    limpar(limpar)


#FRAMES
TopFrame1 = Frame(master, width=1920, height=70, bd=1, relief="solid", bg='#4682B4')
TopFrame1.pack(side=TOP)
TopFrame2 = Frame(master, width=1920, height=10)
TopFrame2.pack(side=TOP)
TopFrame3 = Frame(master, width=1200, height=705, bd=1, relief="solid", bg='#4682B4')
TopFrame3.pack(side=TOP)

#LABEL TÍTULO PRINCIPAL
TextTitle = Label(TopFrame1, text='CADASTRO', font=("Arial", 20, "bold"), bg="#4682B4", fg="white")
TextTitle.place(x=650, y=25)

#WIDGETS LABELS
NomeLabel = Label(TopFrame3, text="NOME", font=("times", 14, "bold"))
NomeLabel.place(x=10, y=15)
LogLabel = Label(TopFrame3, text="LOGRADOURO", font=("times", 14, "bold"))
LogLabel.place(x=10, y=55)
NumLabel = Label(TopFrame3, text="Nº", font=("times", 14, "bold"))
NumLabel.place(x=1090, y=55)
CompLabel = Label(TopFrame3, text="COMPLEMENTO", font=("times", 14, "bold"))
CompLabel.place(x=10, y=95)
BairroLabel = Label(TopFrame3, text="BAIRRO", font=("times", 14, "bold"))
BairroLabel.place(x=625, y=95)
CidadeLabel = Label(TopFrame3, text="CIDADE", font=("times", 14, "bold"))
CidadeLabel.place(x=10, y=135)
CepLabel = Label(TopFrame3, text="CEP", font=("times", 14, "bold"))
CepLabel.place(x=910, y=135)
UfLabel = Label(TopFrame3, text="UF", font=("times", 14, "bold"))
UfLabel.place(x=1070, y=135)
CpfLabel = Label(TopFrame3, text="CPF", font=("times", 14, "bold"))
CpfLabel.place(x=10, y=175)
RgLabel = Label(TopFrame3, text="RG.",  font=("times", 14, "bold"))
RgLabel.place(x=210, y=175)
NascLabel = Label(TopFrame3, text="DATA NASC.",  font=("times", 14, "bold"))
NascLabel.place(x=415, y=175)
EmailLabel = Label(TopFrame3, text="E-MAIL", font=("times", 14, "bold"))
EmailLabel.place(x=650, y=175)
TelLabel = Label(TopFrame3, text="TELEFONE", font=("times", 14, "bold"))
TelLabel.place(x=10, y=215)
CelLabel = Label(TopFrame3, text="CELULAR", font=("times", 14, "bold"))
CelLabel.place(x=290, y=215)
ObsLabel = Label(TopFrame3, text="Observações")
ObsLabel.place(x=10, y=260)


#WIDGETS ENTRADAS
NomeEntry = ttk.Entry(TopFrame3, width=110, font=("times", 15))
NomeEntry.place(x=80, y=15)
NomeEntry.focus()
LogEntry = ttk.Entry(TopFrame3, width=92, font=("times", 15))
LogEntry.place(x=160, y=55)
NumEntry = ttk.Entry(TopFrame3, width=6, font=("times", 15))
NumEntry.place(x=1120, y=55)
CompEntry = ttk.Entry(TopFrame3, width=44, font=("times", 15))
CompEntry.place(x=175, y=95)
BairroEntry = ttk.Entry(TopFrame3, width=47, font=("times", 15))
BairroEntry.place(x=710, y=95)
CidadeEntry = ttk.Entry(TopFrame3, width=80, font=("times", 15))
CidadeEntry.place(x=95, y=135)
CepEntry = ttk.Entry(TopFrame3, width=10, font=("times", 15))
CepEntry.place(x=960, y=135)
UfEntry = ttk.Entry(TopFrame3, width=3, font=("times", 15))
UfEntry.place(x=1105, y=135)
CpfEntry = ttk.Entry(TopFrame3, width=14, font=("times", 15))
CpfEntry.place(x=58, y=175)
RgEntry = ttk.Entry(TopFrame3, width=15, font=("times", 15))
RgEntry.place(x=255, y=175)
NascEntry = ttk.Entry(TopFrame3, width=10, font=("times", 15))
NascEntry.place(x=540, y=175)
EmailEntry = ttk.Entry(TopFrame3, width=45, font=("times", 15))
EmailEntry.place(x=730, y=175)
TelEntry = ttk.Entry(TopFrame3, width=15, font=("times", 15))
TelEntry.place(x=125, y=215)
CelEntry = ttk.Entry(TopFrame3, width=15, font=("times", 15))
CelEntry.place(x=390, y=215)
MsgLabel = Text(TopFrame3, width=117, height=15, bd=1, relief='solid', font=("times", 15))
MsgLabel.place(x=10, y=285)

#BOTÕES
BtCadastra = ttk.Button(TopFrame3, text="CADASTRAR", width=25, command=Armazenar)
BtCadastra.place(x=370, y=650)

BtLimpar = ttk.Button(TopFrame3, text="LIMPAR", width=25)
BtLimpar.bind("<Return>", limpar)
BtLimpar.bind("<Button -1>", limpar)
BtLimpar.place(x=550, y=650)

master.mainloop()