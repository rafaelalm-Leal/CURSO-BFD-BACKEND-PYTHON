"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0."""
medias = []

# Loop para 10 alunos
for aluno in range(10):
    notas = []  # reinicia a lista de notas para cada aluno
    for nota in range(4):
        n = float(input(f'Digite a nota {nota+1} do aluno {aluno+1}: '))
        notas.append(n)
    media = sum(notas) / 4
    medias.append(media)

# Conta quantos alunos tiveram média >= 7
aprovados = 0
for m in medias:
    if m >= 7.0:
        aprovados += 1

print(f'Total de alunos com média maior ou igual a 7.0: {aprovados}')
