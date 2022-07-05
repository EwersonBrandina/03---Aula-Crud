#AULA CRUD
# 1º Inserção, 2º Leitura, 3º Atualização, 4º Apagar (1º Insert, 2º Read, 3º Update, 4º Delete)
import mysql.connector
#Criando a conecção com o banco de dados, com informações do banco de dados
class CRUD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='aula_crud'
            )
        #Criar objeto para manipular o mysql
        self.meu_cursor = self.conexao.cursor()
    def create(self):
        #CREATE
        self.meu_cursor.execute(
        'insert into pessoas' 
        '(nome, dataNasc)'
        'value '
        '("Ewerson Ribeiro Brandina", "1993-03-17")'
        )
        #Edita o banco de dados
        self.conexao.commit() 
    def read(self):
        #Métdo execute serve para executar comandos SQL
        self.meu_cursor.execute('select * from pessoas')
        #Esse método, fetchall, é como se fosse um replace, serve para organizar as informações
        lista = self.meu_cursor.fetchall()
        #Para imprimir linha a linha
        for i in lista:
            print(i)
    def update(self):
        comando_sql = 'update pessoas set nome  = "Bruna Bianca Coelho Lopes" where id = 2'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit() 
    def delete(self):
        self.read()
        valor=input('Insira o ID\n : ')
        comando_sql = f'delete from pessoas where id = {valor}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

objeto = CRUD()
objeto.delete()
