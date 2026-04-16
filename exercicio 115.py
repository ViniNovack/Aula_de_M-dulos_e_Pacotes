from pacote115 import cadastro

while True:
      print('-'*50)
      print('MENU PRINCIPAL'.center(50))
      print('-'*50)
      print('1 - Ver pessoas cadastradas\n'
            '2 - Cadastrar nova Pessoa\n'
            '3 - Sair do Sistema'.center(10))
      print('-'*50)

      op = int(input('Sua Opção: '))
      print('-'*50)

      if op == 1:
            cadastro.lerArquivo()
            continue
      elif op == 2:
            cadastro.adicionar()
            continue
      elif op == 3:
            break
print('=-'*30)
print('FIM')
