#Tela de início
print('----------------------------------')                                           
print('            Bem-vindo!' )
print('                À')
print('    Sua melhor locadora de filmes' )
print('----------------------------------')
input('Tecle enter para acessar o menu')

# Listas de filmes disponíveis
filmes_comedia = ['Se beber não case', 'O mentiroso']
filmes_acao = ['Velozes e Furiosos', 'Missão Impossível']
filmes_romance = ['Titanic', 'O amor está no ar']

# Listas de filmes alugados (guardando filme + índice original)
alugados_comedia = []
alugados_acao = []
alugados_romance = []

# Menu de escolhas
while True:
    print('=================')
    print('MENU')
    print('1-Lista de filmes')
    print('2-Alugar um filme')
    print('3-Devolver um filme')
    print('4-Sair do menu')

    opcao = int(input('Escolha uma opção: '))

    # LISTA DE FILMES
    if opcao == 1:
        while True:
            print('============')
            print("COMÉDIA:", filmes_comedia)
            print("AÇÃO:", filmes_acao)
            print("ROMANCE:", filmes_romance)
            input("Aperte Enter para voltar ao menu.")
            break

    # ALUGAR FILME
    elif opcao == 2:
        while True:
            print('============')
            print('1-Comédia')
            print('2-Ação')
            print('3-Romance')
            print('4-Voltar')
            genero = int(input('Escolha o gênero do seu filme: '))
            print('============')

            if genero == 1:
                print('FILMES DISPONÍVEIS')
                print(filmes_comedia)
                aluguel = int(input('Escolha o filme que você quer (0 ou 1): '))
                if 0 <= aluguel < len(filmes_comedia):
                    alugado = filmes_comedia.pop(aluguel)
                    alugados_comedia.append((alugado, aluguel))  # salva filme + índice
                    print(f'Boa escolha! O filme "{alugado}" foi alugado com sucesso!')
            elif genero == 2:
                print('FILMES DISPONÍVEIS')
                print(filmes_acao)
                aluguel = int(input('Escolha o filme que você quer (0 ou 1): '))
                if 0 <= aluguel < len(filmes_acao):
                    alugado = filmes_acao.pop(aluguel)
                    alugados_acao.append((alugado, aluguel))
                    print(f'Boa escolha! O filme "{alugado}" foi alugado com sucesso!')
            elif genero == 3:
                print('FILMES DISPONÍVEIS')
                print(filmes_romance)
                aluguel = int(input('Escolha o filme que você quer (0 ou 1): '))
                if 0 <= aluguel < len(filmes_romance):
                    alugado = filmes_romance.pop(aluguel)
                    alugados_romance.append((alugado, aluguel))
                    print(f'Boa escolha! O filme "{alugado}" foi alugado com sucesso!')
            elif genero == 4:
                break
            else:
                print('Opção inválida')

    # DEVOLVER FILME
    elif opcao == 3:
        while True:
            print('1-Comédia')
            print('2-Ação')
            print('3-Romance')
            print('4-Voltar')
            genero = int(input('Escolha o gênero do filme que você vai devolver: '))
            print('===============')

            if genero == 1:
                print(f'Seus filmes alugados: {alugados_comedia}')
                devolv = int(input('Qual o índice do filme que você quer devolver? '))
                if 0 <= devolv < len(alugados_comedia):
                    filme, indice = alugados_comedia.pop(devolv)
                    filmes_comedia.insert(indice, filme)  # devolve no lugar original
                    print(f'O filme "{filme}" foi devolvido com sucesso!')
            elif genero == 2:
                print(f'Seus filmes alugados: {alugados_acao}')
                devolv = int(input('Qual o índice do filme que você quer devolver? '))
                if 0 <= devolv < len(alugados_acao):
                    filme, indice = alugados_acao.pop(devolv)
                    filmes_acao.insert(indice, filme)
                    print(f'O filme "{filme}" foi devolvido com sucesso!')
            elif genero == 3:
                print(f'Seus filmes alugados: {alugados_romance}')
                devolv = int(input('Qual o índice do filme que você quer devolver? '))
                if 0 <= devolv < len(alugados_romance):
                    filme, indice = alugados_romance.pop(devolv)
                    filmes_romance.insert(indice, filme)
                    print(f'O filme "{filme}" foi devolvido com sucesso!')
            elif genero == 4:
                break
            else:
                print('Opção inválida')

    # SAIR DO MENU
    elif opcao == 4:
        print('Obrigado por utilizar nossos serviços, até mais!')
        break
    else:
        print('Opção inválida')