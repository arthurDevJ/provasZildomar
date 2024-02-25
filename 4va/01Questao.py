'''Escreva um programa em Python que cadastra as seguintes informações de 1000 funcionarios de uma
empresa: salário fixo, vendas mensal, região de vendas (1-Norte, 2-Nordeste). O programa deve mostrar
o salário final do funcionário, sendo o salário final calculado a partir do próprio salário fixo mais 22% do
valor das vendas do mês. Além disso, o programa deve mostrar ao final quantos vendedores são da
região Norte e quantos são da região Nordeste. Por fim, o programa também deve mostrar a média de
vendas da região Nordeste.'''

total_norte = 0
total_nordeste = 0
total_vendas_nordeste = 0

def calcular_salario_final(salario_fixo, vendas_mensal):
    return salario_fixo + 0.22 * vendas_mensal

funcionarios = []

while True:
    continuar = input("Deseja cadastrar um funcionário? (s/n): ").lower()
    if continuar != 's':
        break

    salario_fixo = float(input("Digite o salário fixo do funcionário: "))
    vendas_mensal = float(input("Digite o valor das vendas mensais do funcionário: "))
    regiao = int(input("Digite a região de vendas (1-Norte, 2-Nordeste): "))

    salario_final = calcular_salario_final(salario_fixo, vendas_mensal)
    funcionarios.append((salario_fixo, vendas_mensal, salario_final, regiao))

    if regiao == 1:
        total_norte += 1
    elif regiao == 2:
        total_nordeste += 1
        total_vendas_nordeste += vendas_mensal

print("\nSalário final de cada funcionário:")
for salario_fixo, vendas_mensal, salario_final, _ in funcionarios:
    print(f"Salário Fixo: {salario_fixo}, Vendas Mensais: {vendas_mensal}, Salário Final: {salario_final:.2f}")

print("\nQuantidade de vendedores por região:")
print(f"Total de vendedores da região Norte: {total_norte}")
print(f"Total de vendedores da região Nordeste: {total_nordeste}")

if total_nordeste > 0:
    media_vendas_nordeste = total_vendas_nordeste / total_nordeste
    print(f"Média de vendas da região Nordeste: {media_vendas_nordeste:.2f}")
else:
    print("Não há funcionários da região Nordeste.")
