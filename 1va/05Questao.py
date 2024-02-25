'''Crie um programa em Python para calcular o reajuste do salário dos funcionários de uma empresa. Para
tal, crie as funções main, folha_pagamento e reajuste_funcionario. A função main é responsável por
criar uma estrutura de menu para chamar a função folha_pagamento. Já a função folha_pagamento é
responsável por cadastrar as informações do funcionário da empresa, ou seja, nome, salário e o número
de filhos de um grupo indeterminado de funcionários. Para calcular o aumento dos funcionários, a função
folha_pagamento usa a função reajuste_funcionario que tem como entrada o salário e o número de
filhos, a função reajuste_funcionario calcula e exibe o novo salário e a diferença salarial (o salário antigo
subtraido do novo salário)
O cálculo do novo salário é feito de acordo com as seguintes regras: a) acréscimo do salário baseado na
tabela abaixo, e b) adicional do salário-familia, no qual o funcionário recebe R$ 25,00 por filho. 


salário 0,00 a 500,00 aumento 30%
salário 500,01 a 1000 aumento 20%
salário acima de 1000 aumento 10%

O programa encerra as atividades quando o usuário do sistema digitar um valor negativo para o salário do funcionário
'''

def reajuste_funcionario(salario, num_filhos):
    if salario <= 500:
        aumento_percentual = 0.30
    elif salario <= 1000:
        aumento_percentual = 0.20
    else:
        aumento_percentual = 0.10
    
    novo_salario = salario * (1 + aumento_percentual)
    salario_familia = num_filhos * 25.00
    novo_salario += salario_familia
    
    diferenca_salarial = novo_salario - salario
    
    return novo_salario, diferenca_salarial

def folha_pagamento():
    while True:
        nome = input("Digite o nome do funcionário (ou digite 'fim' para encerrar): ")
        if nome.lower() == 'fim':
            break
        
        salario = float(input("Digite o salário do funcionário: "))
        if salario < 0:
            print("Valor de salário inválido. Encerrando o programa.")
            return
        
        num_filhos = int(input("Digite o número de filhos do funcionário: "))
        
        novo_salario, diferenca_salarial = reajuste_funcionario(salario, num_filhos)
        print(f"Novo salário de {nome}: R$ {novo_salario:.2f}")
        print(f"Diferença salarial: R$ {diferenca_salarial:.2f}")

def main():
    print("Sistema de Folha de Pagamento")
    folha_pagamento()


main()
