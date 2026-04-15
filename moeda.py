from moedas import moeda1

n = float(input('Digite o preço: R$'))
print(f'A metade de {n} é {(moeda1.metade(n, True))}\n'
      f'O dobro de {n} é {(moeda1.dobro(n))}\n'
      f'Aumento 10%, temos {(moeda1.au10(n))}\n'
      f'Reduzindo 13%, temos {(moeda1.re13(n))}\n')
