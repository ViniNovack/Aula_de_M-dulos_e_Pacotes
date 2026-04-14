import moeda1

n = float(input('Digite o preço: R$'))
print(f'A metade de {n} é {(moeda1.metade(n)):.2f}\n'
      f'O dobro de {n} é {(moeda1.dobro(n)):.2f}\n'
      f'Aumento 10%, temos {(moeda1.au10(n)):.2f}\n'
      f'Reduzindo 13%, temos {(moeda1.re13(n)):.2f}\n')
