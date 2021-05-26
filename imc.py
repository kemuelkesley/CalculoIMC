# IMC
# Calcular o Indice de Massa Corporea.
import os
def Tabela():
    print('-'*30)
    print('1 Menor que [16] > Magreza grave.')
    print('-'*30)
    print('2 Menor que [17] > Magreza Moderada.')
    print('-'*30)
    print('3 Menor que [18.5] > Magreza Leve.')
    print('-'*30)
    print('4 Menor que [25] > Saudavel.')
    print('-'*30)
    print('5 Menor que [30] > Sobrepeso.')
    print('-'*30)
    print('6 Menor que [35:] > Obesidade Grau I.')
    print('-'*30)
    print('7 Menor que [40] Obesidade Grau II.')
    print('-'*30)
  

Tabela()

nome = input('Informe seu nome:')
altura = float(input('Digite sua altura em metros:'))
peso = float(input('Digite seu Peso em KG:'))
imc = peso / (altura * 2)
print('IMC = {}'.format(imc))


if imc < 16:
    print('Seu IMC é: {}'.format(imc))
    print('%s, você está com Magreza grave' %nome)
elif imc < 17:
    print('Seu IMC é: {}'.format(imc))
    print('%s, você está com Magreza Moderada'%nome)   
elif imc < 18:
    print('Seu IMC é: {}'.format(imc))
    print('%s, você está com Magreza Leve'%nome)    
elif imc < 25:
    print('Seu IMC é: {}'.format(imc))
    print('%s, você está Saudavel, PARABÉNS.'%nome)    
elif imc < 30:
    print('Seu IMC é: {}'.format(imc))
    print('%s, você está com Sobrepeso'%nome)
elif imc < 35:
    print('Seu IMC é: {}'.format(imc))
    print('%s você está com Obesidade Grau I'%nome)
elif imc < 40:    
    print('Seu IMC é: {}'.format(imc))
    print('%s, você está com Obesidade Grau II'%nome)        

os.system("pause")
