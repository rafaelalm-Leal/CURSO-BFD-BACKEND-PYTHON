#Calculadora Simples
print('Calculadora de operações simples')
num1=float(input('Digite um número'))
num2=float(input('Digite um número'))
#Operações matemáticas
print('Operações disponíveis')
print('1-Adição(+)')
print('2-Subtração(-)')
print('3-Multiplicação(*)')
print('4-Divisão(/)')
operacao=input('Escolha a operação')
#Realizando a operação matemática
if operacao=='1':
    resultado=num1+num2
elif operacao=='2':
    resultado=num1-num2
elif operacao=='3':
    resultado=num1*num2
elif operacao=='4':
    resultado=num1/num2
else:resultado='Opção inválida'
print('O resultado é:',resultado)