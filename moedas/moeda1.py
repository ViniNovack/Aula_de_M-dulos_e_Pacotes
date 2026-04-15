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

def au10(n, f=True):
    x = n * 1.1
    if f == True:
        return f'{x:.2f}'.replace('.', ',')
    else:
        return x

def re13(n, f=True):
    x = n * 0.87
    if f == True:
        return f'{x:.2f}'.replace('.', ',')
    else:
        return x
