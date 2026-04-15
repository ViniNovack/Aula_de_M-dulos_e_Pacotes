def metade(n, f=True):
    x = n / 2
    if f == True: 
        return f'{x:.2f}'.replace('.', ',')
    else:
        return x

def dobro(n, f=True):
    x = n * 2
    if f == True:
        return f'{x:.2f}'.replace('.', ',')
    else:
        return x

def au10(n, a, f=True):
    a +=100
    a /=100
    x = n * a
    if f == True:
        return f'{x:.2f}'.replace('.', ',')
    else:
        return x

def re13(n, r,  f=True):
    r = 100 - r
    r /=100
    x = n * r
    if f == True:
        return f'{x:.2f}'.replace('.', ',')
    else:
        return x

def resumo(p, a, r):
    print('-'*45)
    print('RESUMO DO VALOR'.center(45))
    print('-'*45)
    print('Preço analisado:'.center(10),
          f'R${metade(p, True)}'.center(37))
    print('Dobro do preço:'.center(10),
          f'R${dobro(p, True)}'.center(42))
    print(f'{a:.0f}% de aumento:'.center(10),
          f'R${au10(p, a, True)}'.center(40))
    print(f'{r:.0f}% de redução:'.center(10),
          f'R${re13(p, r, True)}'.center(40))
