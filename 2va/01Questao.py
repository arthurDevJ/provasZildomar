'''1 - Escreva uma função chamada separa_positivos_negativos que receba uma 
lista de números inteiros como parâmetro e retorne duas listas: 
uma contendo os números positivos e outra contendo os números negativos.'''

def separa_positivos_negativos(lista):
    positivos = []
    negativos = []
    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)
    return positivos, negativos

# Exemplo de uso:
numeros = [1, -2, 3, -4, 5, -6]
positivos, negativos = separa_positivos_negativos(numeros)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
