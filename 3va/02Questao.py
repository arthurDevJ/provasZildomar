'''Crie um programa em Python que chama uma função que recebe três listas como parâmetro. O
primeiro parâmetro é uma lista de números inteiros, o segundo uma lista de números reais e o terceiro
uma lista caracteres. A função deve mostras as seguintes informações:
I . A soma dos valores inteiros entre 10 e 40;
II. Quantas vogal "a" estão presente na lista; e
III. A média dos valores reais;'''


def mostrar_informacoes(lista_inteiros, lista_reais, lista_caracteres):
    # I. Soma dos valores inteiros entre 10 e 40
    soma_inteiros = sum(numero for numero in lista_inteiros if 10 <= numero <= 40)
    print("I. A soma dos valores inteiros entre 10 e 40 é:", soma_inteiros)

    # II. Quantidade de vogais 'a' na lista de caracteres
    vogais_a = sum(1 for caractere in lista_caracteres if caractere.lower() == 'a')
    print("II. Quantidade de vogais 'a' na lista de caracteres é:", vogais_a)

    # III. Média dos valores reais
    if lista_reais:
        media_reais = sum(lista_reais) / len(lista_reais)
        print("III. A média dos valores reais é:", media_reais)
    else:
        print("III. A lista de números reais está vazia.")


# Exemplo de uso
lista_inteiros = [5, 15, 25, 35, 45, 10, 20]
lista_reais = [3.5, 7.2, 5.8, 9.1]
lista_caracteres = ['a', 'b', 'c', 'd', 'e', 'a', 'f', 'g']

mostrar_informacoes(lista_inteiros, lista_reais, lista_caracteres)
