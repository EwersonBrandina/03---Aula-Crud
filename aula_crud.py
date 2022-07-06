import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='aula_crud'
        )
        self.meu_cursor = self.conexao.cursor()

    # CRUD
    # C
    def create(self):
        nome = input('Informe o nome: ')
        data = input('Informa a data de Nascimento AAAA-MM-DD: ')
        sql = f'insert into pessoas (nome, dataNasc) value ("{nome}", "{data}")'
        self.meu_cursor.execute(sql)
        self.conexao.commit()

    # R
    def read(self):
        self.meu_cursor.execute('select * from pessoas')
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    # U
    def update(self):
        cod = int(input('Informe o id da pessoa: '))
        nome = input('Informe o novo nome: ')
        sql = f'update pessoas set nome = "{nome}" where id = {cod}'
        self.meu_cursor.execute(sql)
        self.conexao.commit()

    # D
    def delete(self):
        cod = int(input('Infome o id da pessoa: '))
        sql = f'delete from pessoas where id = {cod}'
        self.meu_cursor.execute(sql)
        self.conexao.commit()


obj_db = BancoDeDados()

obj_db.read()