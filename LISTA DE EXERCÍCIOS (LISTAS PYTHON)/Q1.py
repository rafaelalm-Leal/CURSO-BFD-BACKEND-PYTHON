#Faça um Programa que leia 5 números inteiros, armazene-os em uma lista.
lista=[]
for i in range(5):
    num=int(input('Digite um número: '))
    lista.append(num)
print('Os números da lista são:',lista)
