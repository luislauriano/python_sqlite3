import sqlite3

conexao = sqlite3.connect('dataBase.db')
cursor = conexao.cursor()

def inserir(email, senha):
    sql = f'''
    INSERT INTO usuario(email, senha)
    VALUES ('{email}', '{senha}')
    '''
    cursor.execute(sql)
    conexao.commit()
def atualizar(email, NovaSenha):
    sql = f'''
    UPDATE usuario SET senha = {NovaSenha} WHERE email = '{email}'
    '''
email = input('email: ')
senha = input('senha: ')

atualizar(email, senha)


conexao.close()
