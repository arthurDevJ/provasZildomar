'''
Crie um programa em python que ajude o usuario a gerenciar as compras do mês em um dicionário
chamado ComprasMensal (ComprasMensal ={}). As informações das compras são: Código, Descrição e valor. O programa deve ter as seguintes funcionalidades:

I. Adicionar item: O usuário insere uma compra na base de dados (ComprasMensal);
II. Exibir todas as compras: O programa exibe todos os itens de compra do mês;
III. Remover item: O usuário escolhe um item para remover.'''

def adicionar_item(compras_mensal):
    codigo = input("Digite o código do item: ")
    descricao = input("Digite a descrição do item: ")
    valor = float(input("Digite o valor do item: "))
    compras_mensal[codigo] = {'descricao': descricao, 'valor': valor}
    print("Item adicionado com sucesso!")

def exibir_todas_compras(compras_mensal):
    if compras_mensal:
        print("Lista de compras do mês:")
        for codigo, compra in compras_mensal.items():
            print(f"Código: {codigo}, Descrição: {compra['descricao']}, Valor: R${compra['valor']:.2f}")
    else:
        print("Não há compras cadastradas para este mês.")

def remover_item(compras_mensal):
    codigo = input("Digite o código do item que deseja remover: ")
    if codigo in compras_mensal:
        del compras_mensal[codigo]
        print("Item removido com sucesso!")
    else:
        print("O código digitado não corresponde a nenhum item na lista de compras.")

# Dicionário para armazenar as compras do mês
ComprasMensal = {}

while True:
    print("\nMENU:")
    print("1. Adicionar item")
    print("2. Exibir todas as compras")
    print("3. Remover item")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_item(ComprasMensal)
    elif opcao == '2':
        exibir_todas_compras(ComprasMensal)
    elif opcao == '3':
        remover_item(ComprasMensal)
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
