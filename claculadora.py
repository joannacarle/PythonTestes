num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
 divisao = num1 / num2
else:
 divisao = 'Não é possível dividir por zero'
 
 print('\nResultados\n')
 print("soma: ", soma)
 print('Subtração: ', subtracao)
 print('Multiplicação: ', multiplicacao)
 print('Divisão: ', divisao)