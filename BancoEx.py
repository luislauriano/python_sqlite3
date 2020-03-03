import sqlite3

conexao = sqlite3.connect('dataBase2.db')
cursor = conexao.cursor()

sql = ''' 
CREATE TABLE pessoa (
nome TEXT NOT NULL,
idade INTEGER NOT NULL, 
cpf TEXT NOT NULL)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()