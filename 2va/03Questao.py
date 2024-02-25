'''3 - Crie um programa em Python que ajude o usuário a gerenciar sua lista de compras em um dicionário chamado Compras (Compras = {}). 
O programa deve ter as seguintes funcionalidades:
I. Adicionar item: O usuário insere um item na lista de compras.
II. Exibir lista: O programa exibe todos os itens da lista de compras.
III. Remover item: O usuário escolhe um item para remover da lista.
Obs: Para cada funcionalidade deve ser implementado uma função.'''

def adicionar_item(compras):
    item = input("Digite o item que deseja adicionar à lista de compras: ")
    quantidade = int(input("Digite a quantidade desejada: "))
    compras[item] = quantidade
    print(f"Item '{item}' adicionado à lista de compras com quantidade {quantidade}.")

def exibir_lista(compras):
    if not compras:
        print("A lista de compras está vazia.")
    else:
        print("Lista de Compras:")
        for item, quantidade in compras.items():
            print(f"{item}: {quantidade}")

def remover_item(compras):
    item = input("Digite o item que deseja remover da lista de compras: ")
    if item in compras:
        del compras[item]
        print(f"Item '{item}' removido da lista de compras.")
    else:
        print(f"O item '{item}' não está na lista de compras.")

compras = {}

while True:
    print("\n1. Adicionar item")
    print("2. Exibir lista")
    print("3. Remover item")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_item(compras)
    elif opcao == 2:
        exibir_lista(compras)
    elif opcao == 3:
        remover_item(compras)
    elif opcao == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")