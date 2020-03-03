import sqlite3

conexao = sqlite3.connect('dataBase.db')
cursor = conexao.cursor()

sql = '''
CREATE TABLE usuario (
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT UNIQUE NOT NULL,
senha TEXT NOT NULL)
'''

cursor.execute(sql)
conexao.commit()
conexao.close()