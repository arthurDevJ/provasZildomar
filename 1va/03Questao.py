'''Uma Empresa de vendas de softwares paga a seu vendedor um fixo de R$ 800,00 por mês, mais uma
comissão de 25% pelo seu valor total de vendas no mês. Faça um programa em Python que leia o valor
total das vendas e determine o salário total do funcionário. Mostre as informações sobre o salário do
vendedor. O programa deve ser capaz de calcular o salário de no minimo 100 vendedores da empresa.'''

def calcular_salario_total(vendas):
    salario_fixo = 800.00
    comissao = vendas * 0.25
    salario_total = salario_fixo + comissao
    return salario_total

def main():
    num_vendedores = 100

    for i in range(num_vendedores):
        vendas = float(input(f"Digite o valor total das vendas do vendedor {i+1}: R$ "))
        salario_total = calcular_salario_total(vendas)
        print(f"Salário total do vendedor {i+1}: R$ {salario_total:.2f}")


main()
