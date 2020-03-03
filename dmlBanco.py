import sqlite3
conexao = sqlite3.connect('Banco.db')
cursor = conexao.cursor()


def inserir(nome, idade, cpf):
    sql = f"""
    INSERT INTO pessoa (nome, idade, cpf)
    VALUES ('{nome}', {idade}, '{cpf}')
    """
    cursor.execute(sql)
    conexao.commit()

def atualizar (cpf, novoNome):
    sql = f'''
    UPDATE tb_pessoa SET nome = '{novoNome}' WHERE cpf = '{cpf}' 
    '''
    cursor.execute(sql)
    conexao.commit()

def excluir (cpf):
    sql = f'''
    DELETE FROM tb_pessoa WHERE cpf = '{cpf}'
    '''
    cursor.execute(sql)
    conexao.commit()

def getPessoa(cpf):
    sql = f'''
    SELECT * FROM tb_pessoa WHERE cpf = '{cpf}'
    '''
    cursor.execute(sql)
    pessoa = cursor.fetchone()
    conexao.commit()
    return pessoa

conexao.close()
