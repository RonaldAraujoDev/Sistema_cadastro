from usuarios import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    editar_usuario,
    excluir_usuario,
    carregar_usuarios
)


def exibir_cabecalho():
    print("\n" + "=" * 50)
    print("           SISTEMA DE CADASTRO")
    print("=" * 50)


def exibir_menu():
    print("\n┌──────────────────────────────────────────────┐")
    print("│                  MENU PRINCIPAL              │")
    print("├──────────────────────────────────────────────┤")
    print("│  1 - Cadastrar usuário                       │")
    print("│  2 - Listar usuários                         │")
    print("│  3 - Buscar usuário                          │")
    print("│  4 - Editar usuário                          │")
    print("│  5 - Excluir usuário                         │")
    print("│  0 - Sair                                    │")
    print("└──────────────────────────────────────────────┘")


def menu():
    carregar_usuarios()

    while True:
        exibir_cabecalho()
        exibir_menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            buscar_usuario()

        elif opcao == "4":
            editar_usuario()

        elif opcao == "5":
            excluir_usuario()

        elif opcao == "0":
            print("\nPrograma encerrado!")
            break

        else:
            print("\nOpção inválida!")


menu()