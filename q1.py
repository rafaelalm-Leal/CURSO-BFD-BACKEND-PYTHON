#1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros=['Dom Casmurro','O Pequeno Príncipe','A Metamorfose']
print(livros)

#2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
print(livros[0])
print(livros[2])

#3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append('O Diário de um banana')
livros.append('Harry Potter')
print(livros)

#4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1,'Duna')
print(livros)

#5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("Livro removido com sucesso!")
else:
    print("Livro não encontrado")

#6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
numeros = [1, 2, 3, 2, 4, 2, 5]
qtd = numeros.count(2)
print(f"O número 2 aparece {qtd} vezes na lista.")

#7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for livro in livros:
    print(f'O livro {livro} é interessante')

#8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(idade)

#9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma = 0 
for v in valores:
    soma = soma + v 
print("A soma é:", soma)

#10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
#notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
notas = []  # lista principal que vai armazenar as notas dos alunos
for i in range(2):  
    aluno = []  
    print(f"\nDigite as 3 notas do aluno {i+1}:")
    for j in range(3):  
        nota = float(input(f"Nota {j+1}: "))
        aluno.append(nota)  
    notas.append(aluno)  
print("\nMédias dos alunos:")
for i in range(2):
    media = sum(notas[i]) / 3
    print(f"Aluno {i+1}: média = {media:.2f}")

'''11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
[ ] - para posições vazias
tor - para a torre
cav - para o cavalo
bis - para o bispo
rai - para a rainha
rei - para o rei
pea - para o peão
Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)'''
# Criando o tabuleiro vazio com list comprehension
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

# Peças principais (linha inicial)
pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

# Colocando peças brancas
tabuleiro[0] = pecas[:]   # linha 0
tabuleiro[1] = ["pea"] * 8  # linha 1

# Colocando peças pretas
tabuleiro[6] = ["pea"] * 8  # linha 6
tabuleiro[7] = pecas[:]   # linha 7

# Exibindo o tabuleiro
print("Tabuleiro de Xadrez:\n")
for linha in tabuleiro:
    print(" ".join(linha))
