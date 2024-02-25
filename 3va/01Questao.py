'''Escreva um programa em Python que define uma função que recebe uma lista de alunos (estrutura de
dados lista) como parâmetro e retorna duas novas listas, uma contendo os alunos aprovados e outra
com os reprovados. Além disso, a função calcula e exibe uma mensagem informando quantos alunos
possui idade superior 22 anos.'''



def separar_alunos(lista_alunos):
    alunos_aprovados = []
    alunos_reprovados = []
    contador_idade_superior_22 = 0
    
    for aluno in lista_alunos:
        if aluno['nota'] >= 6.0:
            alunos_aprovados.append(aluno)
        else:
            alunos_reprovados.append(aluno)
        
        if aluno['idade'] > 22:
            contador_idade_superior_22 += 1
    
    print(f"O número de alunos com idade superior a 22 anos é: {contador_idade_superior_22}")
    
    return alunos_aprovados, alunos_reprovados

# Exemplo de uso
lista_alunos = [
    {'nome': 'João', 'idade': 20, 'nota': 7.5},
    {'nome': 'Maria', 'idade': 25, 'nota': 5.0},
    {'nome': 'Pedro', 'idade': 22, 'nota': 6.8},
    {'nome': 'Ana', 'idade': 23, 'nota': 4.3}
]

aprovados, reprovados = separar_alunos(lista_alunos)

print("Alunos aprovados:")
for aluno in aprovados:
    print(aluno)

print("\nAlunos reprovados:")
for aluno in reprovados:
    print(aluno)
