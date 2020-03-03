from dmlBanco import inserir, atualizar, excluir

def menu():
      menu = int(input("""
      1 - inserir
      2 - ler
      3 - atualizar
      4 - excluir
      5 - sair
      """))
      print(menu)

def titulo():
      print(10 * '-' + 'Programa de Banco de Dados' + 10 * '-')
