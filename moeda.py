from moedas import moeda1, dado

n = dado.leiaDinheiro('Digite o preço: R$')
a = dado.leiaDinheiro('Digite o aumento: ')
r = dado.leiaDinheiro('Digite a redução: ')
moeda1.resumo(n, a, r)
