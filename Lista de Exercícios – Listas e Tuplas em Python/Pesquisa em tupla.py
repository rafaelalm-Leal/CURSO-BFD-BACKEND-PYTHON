#Crie uma tupla com números e verifique se um número digitado pelo usuário está dentro da tupla.
tupla=(1,5,11,14,18,6,8)
num=int(input('Digite um número: '))
if num in tupla:
    print('O número que você escolheu está na tupla')
else:
    print('O número que você escolheu não está na tupla')