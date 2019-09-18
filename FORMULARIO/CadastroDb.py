#IMPORTANDO A BIBLIOTECA
import pymysql

#CONEXÃO AO BANCO DE DADOS
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd="",
    database='formulário'
)
#INSTANCIANDO O MÉTODO CURSOR
cursor = conn.cursor()
#para executar comandos: Digitar aqui: cursor.execute("")

print("Conectado ao Banco de dados!")
