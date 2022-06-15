from doctest import testfile
from unicodedata import name
from colorama import Cursor
import mysql.connector
from sqlalchemy import column, table


Database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='qweasdzxc',
    database='',
)

def create_db(database_name):
    Cursor = Database.cursor()
    Cursor.execute(f"CREATE DATABASE {database_name}")
    print(f'Database {database_name} criada')

def create_table(table_name):
    Database = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='qweasdzxc',
        database='faculdade',
    )
    
    Cursor = Database.cursor()
    comando_createtable = f"CREATE TABLE {table_name}(\nid INT(6) NOT NULL AUTO_INCREMENT,\nnome VARCHAR(50),\ncargo VARCHAR(50),\nsetor VARCHAR(50),\nemail VARCHAR(50),\ncpf VARCHAR(50),\nPRIMARY KEY(id)\n);"
    print(comando_createtable)
    Cursor.execute(comando_createtable)
    Database.commit()

def select_table(column_name, table_name, database_name):
    Cursor = Database.cursor()
    Cursor.execute(f"USE {database_name}")
    Cursor.execute(f"SELECT {column_name} FROM {table_name}")
    Cursor_Result = Cursor.fetchall()
    print(Cursor_Result)

create_db(
    database_name = 'faculdade'
)

create_table (
    table_name = 'alunos'
)

def menu():
    print ("1 - mostrar componentes da tabela")
    opcao = int(input("Digite a sua opção"))

    if opcao == 1:
        column_op = str(input("Coluna a ser consultada"))
        table_op = str(input("tabela a ser consultada"))
        database_op = str(input("Selecione a database para consulta"))
        select_table(
            column_name = column_op,
            table_name = table_op,
            database_name= database_op
        )

menu()