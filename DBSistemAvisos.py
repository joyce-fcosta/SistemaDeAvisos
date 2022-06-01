import sqlite3
from sqlite3 import Error

#Funcao para fazer conexao
def conexaoDB():
    # Caminho do local do Banco de Dados
    caminho = "C:\\Users\\Íris\\OneDrive\\Área de Trabalho\\Aula e TDS\\TEC DESENVOLVIMENTO DE SISTEMAS\\Sistema de Avisos\\SistemaDeAvisos.db"
    #Começar a conexao garantindo que nao tem valor na variavel conexao
    con = None

    try:
        #Aplicando a conexao com o caminho passado
        con=sqlite3.connect(caminho)

    except Error as ex:
        #Caso ocarra um erro, mensagem padrao
        print(ex)
    return con  

#Funcao inserindo os dados e usando o caminho do DB
def inserir(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido!")
    except Error as ex:
        print(ex)



print("Cadastro")
Login = input("Login: ")
Senha = input("Senha: ")


vcon = conexaoDB()
vsql = "INSERT INTO User (Login,Senha)VALUES('"+Login+"','"+Senha+"')"
inserir(vcon, vsql)