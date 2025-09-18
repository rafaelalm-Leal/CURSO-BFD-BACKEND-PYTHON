#Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a multiplicação e os números.
lista = []
for i in range(5):
    nums = int(input('Digite um número: '))
    lista.append(nums)

# soma
print('A soma dos números é:', sum(lista))

# multiplicação
multiplicacao = 1
for num in lista:
    multiplicacao *= num
print('A multiplicação dos números é:', multiplicacao)

# mostrar números
print('Os números são:', lista)
