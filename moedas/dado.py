def leiaDinheiro(texto):
    while True:
        n = str(input(texto)).strip()
        if ',' in n:
            n = n.replace(',','.')
        
        try:
            if '.' in n:
                n = float(n)
                break
            else:
                n = int(n)
                break
        except:
            print(f'ERRO: "{n}" é invalido.')
            continue
    return n
