'''Crie um programa que permita cadastrar informações de produtos(nome, preço, quantidade) em uma lista chamada baseProdutos (Lista de lista). 
O programa deve ter as seguintes funcionalidades: 
I. Cadastrar produto: O usuário insere as informações de um novo produto. 
II.Exibir produtos: O programa deve listar os produtos. 
III. Calcular total: O programa a calcula o valor total dos produtos em estoque(preço * quantidade) e exibe resultado.' 
*Obs.:* Para cada funcionalidade deve ser implementado uma função.'''

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quant = int(input("Digite a quantidade em estoque: "))
    return [nome, preco, quant]

def exibir_produtos(baseProdutos):
    print("Lista de Produtos:")
    for produto in baseProdutos:
        print(f"Nome: {produto[0]}, Preço: R${produto[1]:.2f}, Quantidade: {produto[2]}")

def calcular_total(baseProdutos):
    total = 0
    for produto in baseProdutos:
        total += produto[1] * produto[2]
    print(f"O valor total dos produtos em estoque é: R${total:.2f}")

baseProdutos = []

while True:
    print("\n1. Cadastrar produto\n2. Exibir produtos\n3. Calcular total\n4. Sair")
    '''print("2. Exibir produtos")
    print("3. Calcular total")
    print("4. Sair")'''

    op = int(input("Escolha uma opção: "))

    if op == 1:
        produto = cadastrar_produto()
        baseProdutos.append(produto)
        print("Produto cadastrado com sucesso!")
    elif op == 2:
        exibir_produtos(baseProdutos)
    elif op == 3:
        calcular_total(baseProdutos)
    elif op == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
