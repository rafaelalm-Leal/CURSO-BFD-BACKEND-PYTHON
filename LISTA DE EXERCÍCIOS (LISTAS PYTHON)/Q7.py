"""Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada
informação na sua respectiva lista. Imprima a idade da pessoa que possui maior altura."""
idade=[]
altura=[]
for i in range(10):
    idd=int(input('Digite sua idade: '))
    idade.append(idd)
    alt=float(input('Digite sua altura: '))
    altura.append(alt)
m_altura=max(altura)
indice = altura.index(m_altura)
# idade correspondente
print('A maior altura é:', m_altura)
print('A idade da pessoa mais alta é:', idade[indice])