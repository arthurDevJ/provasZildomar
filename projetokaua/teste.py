import json

def carregar_arq(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_arq(carros, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(carros, arquivo, indent = 4)

def adc_download(lista, donwload):
    lista.append(donwload)

def excluir_download(lista, num_esc):
    if num_esc in lista:
        lista.pop(num_esc)
        print("Removido com sucesso! ")
    else:
        print("\nINFORMAÇÃO NÃO ENCONTRADA ")
        return lista

