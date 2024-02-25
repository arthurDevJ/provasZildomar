'''Crie um programa em Python para calcular o reajuste do salário dos funcionários de uma empresa. Para
tal, crie as funções main, folha_pagamento e reajuste_funcionario. A função main é responsável por
criar uma estrutura de menu para chamar a função folha_pagamento. Já a função folha_pagamento e
responsável por cadastrar as informações do funcionário da empresa, ou seja, nome, salário e o número
de filhos de um grupo indeterminado de funcionários. Para calcular o aumento dos funcionários, a função
folha_pagamento usa a função reajuste funcionario que tem como entrada o salário e o número de
filhos, a função reajuste_funcionario calcula e exibe o novo salário e a diferença salarial (o salário antigo
subtraído do novo salário)
O cálculo do novo salário é feito de acordo com as seguintes regras: a) acréscimo do salário baseado na
tabela abaixo, e b) adicional do salário-família, no qual o funcionário recebe R$ 25,00 por filho.'''


def reajuste_funcionario(salario, num_filhos):
    if salario <= 500:
        aumento = salario * 0.30
    elif salario <= 1000:
        aumento = salario * 0.20
    else:
        aumento = salario * 0.10

    adicional_salario_familia = 25 * num_filhos

    novo_salario = salario + aumento + adicional_salario_familia
    diferenca_salarial = novo_salario - salario

    return novo_salario, diferenca_salarial

def folha_pagamento():
    funcionarios = []
    while True:
        nome = input("Digite o nome do funcionário (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        salario = float(input("Digite o salário do funcionário: "))
        if salario < 0:
            print("Salário negativo inserido. Encerrando o programa...")
            return
        num_filhos = int(input("Digite o número de filhos do funcionário: "))
        funcionarios.append((nome, salario, num_filhos))

    print("\nFolha de Pagamento:")
    for nome, salario, num_filhos in funcionarios:
        novo_salario, diferenca_salarial = reajuste_funcionario(salario, num_filhos)
        print(f"Nome: {nome}, Salário Antigo: R${salario:.2f}, Novo Salário: R${novo_salario:.2f}, Diferença Salarial: R${diferenca_salarial:.2f}")

def main():
    print("Bem-vindo ao Sistema de Folha de Pagamento")
    while True:
        print("\nMENU:")
        print("1. Calcular Folha de Pagamento")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            folha_pagamento()
        elif opcao == '2':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")


main()
