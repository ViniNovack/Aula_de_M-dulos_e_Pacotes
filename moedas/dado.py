def leiaDinheiro(texto):
    while True:
        n = str(input(texto)).strip()
        if ',' in n:
            n = n.replace(',','1')
        
        if n.isnumeric():
            break
        else:
            print(f'ERRO: {n} é inválido!')
            continue
    n = n.replace('1', '.')
    if '.' in n:
        n = float(n)
    else:
        n = int(n)
    return n

x = leiaDinheiro('Digite: ')
print(x)



def leiaDinheiro(texto):
    while True:
        # Lemos a entrada, limpamos espaços e trocamos a vírgula pelo ponto
        entrada = str(input(texto)).strip().replace(',', '.')

        # Validamos se a string resultante pode ser convertida para float
        if entrada.replace('.', '', 1).isdigit() and entrada != '':
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')

