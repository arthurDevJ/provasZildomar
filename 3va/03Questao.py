'''Construa um programa em Python que cria uma Lista Animais - (Lista de lista). O animal possui as
informações presentes na Tabela 01. O programa deve implementar as seguintes funcionalidades:
1. Cadastrar os animais;
2. Mostrar todos os animais de uma determinada raça;
3. Calcular a média de peso dos animais de uma determinada raça e um determinado tipo de
raça.'''


def cadastrar_animal(lista_animais):
    codigo = input("Digite o código do animal: ")
    raca = input("Digite a raça do animal: ")
    peso = float(input("Digite o peso do animal em KG: "))
    tipo_raca = input("Digite o tipo de raça do animal: ")
    lista_animais.append({'codigo': codigo, 'raca': raca, 'peso': peso, 'tipo_raca': tipo_raca})
    print("Animal cadastrado com sucesso!")

def mostrar_animais_por_raca(lista_animais):
    raca = input("Digite a raça para listar os animais: ")
    animais_raca = [animal for animal in lista_animais if animal['raca'] == raca]
    if animais_raca:
        print(f"Animais da raça {raca}:")
        for animal in animais_raca:
            print(f"Código: {animal['codigo']}, Peso: {animal['peso']} KG")
    else:
        print(f"Não há animais cadastrados da raça {raca}.")

def calcular_media_peso_por_raca(lista_animais):
    raca = input("Digite a raça para calcular a média de peso: ")
    animais_raca = [animal for animal in lista_animais if animal['raca'] == raca]
    if animais_raca:
        pesos = [animal['peso'] for animal in animais_raca]
        media_peso = sum(pesos) / len(pesos)
        print(f"Média de peso dos animais da raça {raca}: {media_peso:.2f} KG")
    else:
        print(f"Não há animais cadastrados da raça {raca}.")

def calcular_media_peso_por_tipo_raca(lista_animais):
    tipo_raca = input("Digite o tipo de raça para calcular a média de peso: ")
    animais_tipo_raca = [animal for animal in lista_animais if animal['tipo_raca'] == tipo_raca]
    if animais_tipo_raca:
        pesos = [animal['peso'] for animal in animais_tipo_raca]
        media_peso = sum(pesos) / len(pesos)
        print(f"Média de peso dos animais do tipo de raça {tipo_raca}: {media_peso:.2f} KG")
    else:
        print(f"Não há animais cadastrados do tipo de raça {tipo_raca}.")

lista_animais = []

while True:
    print("\nMENU:")
    print("1. Cadastrar animal")
    print("2. Mostrar animais por raça")
    print("3. Calcular média de peso por raça")
    print("4. Calcular média de peso por tipo de raça")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_animal(lista_animais)
    elif opcao == '2':
        mostrar_animais_por_raca(lista_animais)
    elif opcao == '3':
        calcular_media_peso_por_raca(lista_animais)
    elif opcao == '4':
        calcular_media_peso_por_tipo_raca(lista_animais)
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")