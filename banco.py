# sistema_cadastro_v1.py

def menu():
    print("\n--- Sistema de Cadastro (Versão 1) ---")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

def cadastrar():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    with open("usuarios.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome},{idade}\n")
    print("✅ Usuário cadastrado com sucesso!")

def listar():
    print("\n--- Lista de Usuários ---")
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linha in f:
                nome, idade = linha.strip().split(",")
                print(f"Nome: {nome} | Idade: {idade}")
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()