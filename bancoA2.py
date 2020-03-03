import sqlite3

#conexao com o banco de dados
conexao = sqlite3.connect('bancoA2.db')
cursor = conexao.cursor()


#Criar a tabela/Criar string para comandar os atributos para a tabela
sql = '''
CREATE TABLE pessoa (
id INTEGER PRIMARY KEY AUTOINCREMENT,
campo_nome TEXT NOT NULL, 
campo_idade INTEGER NOT NULL, 
campo_cpf TEXT NOT NULL) 
'''
cursor.execute(sql)
conexao.commit()
conexao.close()