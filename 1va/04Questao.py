'''Escreva uma função chamada calcula_hora_extra para calcular e retornar o valor que deverá ser pago
ao empregado no final do mês em horas extras. Para fazer esse cálculo, basta dividir o salário mensal do
empregado pelo número de horas trabalhadas (horas trabalhadas no mês). Multiplique esse valor por 1,5
e terá o valor da hora extra '''

def calcula_hora_extra(salario_mensal, horas_trabalhadas):
    valor_hora = salario_mensal / horas_trabalhadas
    valor_hora_extra = valor_hora * 1.5
    return valor_hora_extra

def main():
    salario_mensal = float(input("Digite o salário mensal do empregado: R$ "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    valor_hora_extra = calcula_hora_extra(salario_mensal, horas_trabalhadas)
    print(f"O valor da hora extra é: R$ {valor_hora_extra:.2f}")

main()