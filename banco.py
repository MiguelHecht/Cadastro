# sistema_cadastro_v2.py

import json
import os

ARQUIVO = "usuarios.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def menu():
    print("\n--- Sistema de Cadastro (Versão 2) ---")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Remover usuário")
    print("5 - Sair")

def cadastrar(usuarios):
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    usuarios.append({"nome": nome, "idade": idade})
    salvar_dados(usuarios)
    print("✅ Usuário cadastrado com sucesso!")

def listar(usuarios):
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for u in usuarios:
        print(f"Nome: {u['nome']} | Idade: {u['idade']}")

def buscar(usuarios):
    nome = input("Digite o nome para buscar: ")
    encontrados = [u for u in usuarios if u["nome"].lower() == nome.lower()]
    if encontrados:
        for u in encontrados:
            print(f"✅ Encontrado: Nome: {u['nome']} | Idade: {u['idade']}")
    else:
        print("Usuário não encontrado.")

def remover(usuarios):
    nome = input("Digite o nome do usuário a remover: ")
    usuarios_filtrados = [u for u in usuarios if u["nome"].lower() != nome.lower()]
    if len(usuarios) != len(usuarios_filtrados):
        salvar_dados(usuarios_filtrados)
        print("🗑️ Usuário removido com sucesso!")
        return usuarios_filtrados
    else:
        print("Usuário não encontrado.")
        return usuarios

def main():
    usuarios = carregar_dados()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar(usuarios)
            usuarios = carregar_dados()
        elif opcao == "2":
            listar(usuarios)
        elif opcao == "3":
            buscar(usuarios)
        elif opcao == "4":
            usuarios = remover(usuarios)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()