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

altura = float(input('Digite sua altura em metros:'))
peso = float(input('Digite seu Peso em KG:'))
imc = peso / (altura * 2)
print('IMC = {}'.format(imc))


if imc < 16:
    print('Magreza grave')
elif imc < 17:
    print('Magreza Moderada')   
elif imc < 18.8:
    print('Magreza Leve')     
elif imc < 25:
    print('Saudavel')    
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    
    print('Obesidade Grau II')        

os.system("pause")
