'''A empresa Nosso Sertão Quente decidiu conceder um aumento de salário aos seus funcionários de
acordo com a tabela abaixo: 

até 1200 - 25%
de 1201 até 3000 - 15%
acima de 3000 - 10%

Crie um algontmo em Python que lé para cada funcionário o o seu salário atual. Após
receber este dado, o algoritmo calcula o novo salário e escreve na tela o novo salário do
funcionário.'''

def calcular_aumento(salario_atual):
    if salario_atual <= 1200:
        aumento = salario_atual * 0.25
    elif salario_atual <= 3000:
        aumento = salario_atual * 0.15
    else:
        aumento = salario_atual * 0.10
    
    novo_salario = salario_atual + aumento
    return novo_salario

def main():
    salario_atual = float(input("Digite o salário atual do funcionário: "))
    novo_salario = calcular_aumento(salario_atual)
    print("Novo salário do funcionário: R$", novo_salario)

main()
