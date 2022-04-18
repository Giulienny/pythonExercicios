real = float(input('Quanto de dinheiro você tem na carteira: R$ '))
dolar = real/3.27
libra = real/5.70
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, libra))

