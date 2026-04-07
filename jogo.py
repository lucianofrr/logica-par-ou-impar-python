#criando variaveis para o jogo

#operadores matematicos
#somar + ex: 1+1 = 2
#incrementar +=  ex: idade += 1
#subtracao - ex: 3-2 = 1
#descremento -= ex: idade -= 1
#multiplicacao *
#divisao /

jogador1 = int(input('Informe um número'))
jogador2 = int(input('Informe um número'))

numero = jogador1 + jogador2

if numero % 2 != 0:
    print('Impar ganhou')
else print('Par ganhou')