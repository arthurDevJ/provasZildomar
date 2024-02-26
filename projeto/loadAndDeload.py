import json

def carregar_carros(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_carros(carros, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(carros, arquivo, indent=4)

def adicionar_carro(carros, carro):
    carros.append(carro)

def excluir_carro(carros, indice):
    if 0 <= indice < len(carros):
        del carros[indice]
    else:
        print("Índice inválido.")

def editar_carro(carros, indice, novo_carro):
    if 0 <= indice < len(carros):
        carros[indice] = novo_carro
    else:
        print("Índice inválido.")