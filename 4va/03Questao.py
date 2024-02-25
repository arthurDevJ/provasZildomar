'''Construa um programa em Python que cria uma Lista para armazenar (Lista de lista) os livros de uma
biblioteca pessoal de um profissional de Sistemas de Informação. Use as informações presentes na
Tabela 01 para criar os elementos da lista. O programa deve implementar as seguintes funcionalidades
(utilizando funções): (3,0 Pontos)
a) Cadastrar todos os livros;
b) Mostrar todos os livros de uma determinada área;
c) Calcular o total gasto para adquirir o acervo (todos os livros).'''

def cadastrar_livro(lista_livros):
    codigo = input("Digite o código do livro: ")
    produto = input("Digite o nome do livro: ")
    area = input("Digite a área do livro: ")
    valor = float(input("Digite o valor do livro: "))
    lista_livros.append([codigo, produto, area, valor])
    print("Livro cadastrado com sucesso!")

def mostrar_livros_por_area(lista_livros, area_desejada):
    livros_encontrados = [livro for livro in lista_livros if livro[2] == area_desejada]
    if livros_encontrados:
        print(f"Livros da área de {area_desejada}:")
        for livro in livros_encontrados:
            print(f"Código: {livro[0]}, Livro: {livro[1]}, Valor: R${livro[3]:.2f}")
    else:
        print(f"Não há livros cadastrados na área de {area_desejada}.")

def calcular_total_gasto(lista_livros):
    total_gasto = sum(livro[3] for livro in lista_livros)
    print(f"O total gasto para adquirir o acervo é: R${total_gasto:.2f}")

# Criando uma lista para armazenar os livros
biblioteca_pessoal = []

while True:
    print("\nMENU:")
    print("1. Cadastrar livro")
    print("2. Mostrar livros por área")
    print("3. Calcular total gasto para adquirir o acervo")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_livro(biblioteca_pessoal)
    elif opcao == 2:
        area_desejada = input("Digite a área desejada: ")
        mostrar_livros_por_area(biblioteca_pessoal, area_desejada)
    elif opcao == 3:
        calcular_total_gasto(biblioteca_pessoal)
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
