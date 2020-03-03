import sqlite3
conexao = sqlite3.connect('bancoDeDados.py')
cursor = conexao.cursor()

def inserir(nome, idade, cpf):
  sql = f""" 
  INSERT INTO pessoa (campo_nome, campo_idade, campo_cpf)
  VALUES ('{nome}', {idade}, '{cpf}')
  """
  cursor.execute(sql)
  conexao.commit()

def atualizar (cpf, novoNome):
  sql = f'''
  UPDATE tb_pessoa SET campo_nome = '{novoNome}' WHERE campo_cpf = '{cpf}'
  '''
  cursor.execute(sql)
  conexao.commit()

def excluir(cpf):
  sql = f'''
  DELETE FROM tb_pessoa WHERE campo_cpf = '{cpf}'
  '''
  cursor.execute(sql)
  conexao.commit()

def getPessoa(cpf):
  sql = f'''
  SELECT * FROM tb_pessoa WHERE campo_cpf = '{cpf}'
  '''
  cursor.execute(sql)
  pessoa = cursor.fetchone()
  conexao.commit()
  return pessoa

print(getPessoa('121.252.230-20'))
excluir('112.232.232-29')
#atualizar('112.232.232.29', '38')
#inserir('Juvenita', 23, '704.927')
conexao.close()