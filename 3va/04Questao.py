'''Crie um dicionário vazio rebanho = {}. O dicionário deverá armazenar dados sobre o rebanho da
fazenda Esperança conforme mostra a Tabela 01. Crie um programa em Python para produzir as
seguintes funcionalidades: 

I. Cadastrar os animais do rebanho;
II. Listar todas os animais de tipo de raça Leite;
III. Mostrar a média de peso dos animais de corte.

Obs: Para cada funcionalidade deve ser implementado uma funcão'''

def cadastrar_animal(rebanho):
    codigo = input("Digite o código do animal: ")
    if codigo in rebanho:
        print("Já existe um animal cadastrado com este código.")
        return
    
    raca = input("Digite a raça do animal: ")
    peso = float(input("Digite o peso do animal em KG: "))
    tipo_raca = input("Digite o tipo de raça do animal: ")
    rebanho[codigo] = {'raca': raca, 'peso': peso, 'tipo_raca': tipo_raca}
    print(f"Animal com código {codigo} cadastrado com sucesso!")

def listar_animais_leite(rebanho):
    animais_leite = [animal for animal in rebanho.values() if animal['tipo_raca'] == 'leite']
    if animais_leite:
        print("Animais de tipo de raça Leite:")
        for codigo, animal in rebanho.items():
            if animal['tipo_raca'] == 'leite':
                print(f"Código: {codigo}, Raça: {animal['raca']}, Peso: {animal['peso']} KG")
    else:
        print("Não há animais de tipo de raça Leite cadastrados.")

def calcular_media_peso_corte(rebanho):
    pesos_corte = [animal['peso'] for animal in rebanho.values() if animal['tipo_raca'] == 'corte']
    if pesos_corte:
        media_peso = sum(pesos_corte) / len(pesos_corte)
        print(f"A média de peso dos animais de corte é: {media_peso:.2f} KG")
    else:
        print("Não há animais de tipo de raça Corte cadastrados.")

# Dicionário vazio para armazenar o rebanho
rebanho = {}

while True:
    print("\nMENU:")
    print("1. Cadastrar animal")
    print("2. Listar animais de tipo de raça Leite")
    print("3. Calcular média de peso dos animais de tipo de raça Corte")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_animal(rebanho)
    elif opcao == 2:
        listar_animais_leite(rebanho)
    elif opcao == 3:
        calcular_media_peso_corte(rebanho)
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
