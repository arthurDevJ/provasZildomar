'''Crie um aplicativo para gerenciar downloads. Os usuários podem
adicionar novos downloads, visualizar a lista de downloads,
atualizar informações e remover downloads concluídos.'''

import json

def carregar_arq(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_arq(dicionario, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo, indent = 4)

def adc_download(dicionario, donwload):
    dicionario.update(donwload)

def excluir_download(dicionario, num_esc):
    if num_esc in dicionario:
        dicionario.pop(num_esc)
        print("Removido com sucesso! ")
    else:
        print("\nINFORMAÇÃO NÃO ENCONTRADA ")
        return dicionario

def main():
    arquivo_downloads = "downloads.json"
    downloads = carregar_arq(arquivo_downloads)
    
    while True:
        print("----MENU----")
        print("GERENCIADOR DE DOWNLOADS")
        print("[1]- Adicionar novo download")
        print("[2]- Visulizar lista de downloads")
        print("[3]- Atualizar lista de downloads")
        print("[4]- Remover downloads concluídos")
        print("[5]- Sair")

        op = int(input("Digite sua escolha: "))

        if op == 1:
            cod = int(input("Digite o código do download: "))
            nome = input("Nome do download: ").capitalize()
            tamanho = input("Tamanho do download: ").capitalize()
            tipo_arq = (input("Tipo do arquivo: ")).lower()
            novo_download = {cod : {"nome": nome, "tamanho": tamanho, "tipo_arq": tipo_arq}}
            adc_download(downloads, novo_download)
            salvar_arq(downloads, arquivo_downloads)
            print("Download adicionado com sucesso.")
        elif op == 2:
            for i in downloads:
                print(f'Cod: {i}, Nome: {downloads[i]["nome"]}, Tamanho: {downloads[i]["tamanho"]}, Tipo arquivo {downloads[i]["tipo_arq"]}')
        elif op == 3:
            novo_cod = str(input("Digite qual código do download: "))
            while novo_cod not in downloads:
                print("Código não encontrado!")
                novo_cod = str(input("Digite qual código do download: "))
            novo_nome = input("Novo nome do download: ").capitalize()
            novo_tamanho = input("Novo tamanho do download: ").capitalize()
            novo_tipo_arq = (input("Novo tipo do arquivo: ")).lower()
            downloads[novo_cod] = {'nome': novo_nome, 'tamanho': novo_tamanho, 'tipo_arq': novo_tipo_arq}
            downloads.update(downloads)
            salvar_arq(downloads, arquivo_downloads)
        elif op == 4:
            num_esc = str(input("Número do download escolhido para remoção: "))
            excluir_download(downloads, num_esc)
            salvar_arq(downloads, arquivo_downloads)
        else:
            downloads.update(downloads)
            salvar_arq(downloads, arquivo_downloads)
            print("Saindo...")
            break
main()