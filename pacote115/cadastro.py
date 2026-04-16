def lerArquivo():
    with open('cadastros.txt', 'r') as arquivos:
        c = arquivos.read()
        print(c)

def adicionar():
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    with open('cadastros.txt', 'a') as arquivo:
        arquivo.write(f'{nome}______{idade}\n')
