def leiaDinheiro(texto):
    while True:
        n = str(input(texto)).strip()
        if n.isnumeric():
            break
        else:
            print(f'ERRO: {n} é inválido!')
            continue
    n = int(n)
    return n
