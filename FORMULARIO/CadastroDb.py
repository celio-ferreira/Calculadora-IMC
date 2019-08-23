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

#EXECUTANDO OS COMANDOS
#cursor.execute("CREATE DATABASE if not exists formulário")
cursor.execute("CREATE TABLE if not exists telefone(Cpf varchar(15) NOT NULL, Tel int(12) not null)")