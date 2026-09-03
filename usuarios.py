import json
import os


PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_USUARIOS = os.path.join(PASTA_PROJETO, "usuarios.json")


usuarios = []
proximo_id = 1


def validar_email(email):
    if "@" not in email:
        return False

    if "." not in email:
        return False

    if email.startswith("@"):
        return False

    if email.endswith("@"):
        return False

    parte_usuario, parte_dominio = email.split("@", 1)

    if not parte_usuario:
        return False

    if not parte_dominio:
        return False

    if parte_dominio.startswith("."):
        return False

    if parte_dominio.endswith("."):
        return False

    return True


def salvar_usuarios():
    dados = {
        "proximo_id": proximo_id,
        "usuarios": usuarios
    }

    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_usuarios():
    global usuarios
    global proximo_id

    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, dict):
            print("\nErro: formato do arquivo usuarios.json inválido.")
            usuarios = []
            proximo_id = 1
            return

        usuarios = dados.get("usuarios", [])
        proximo_id = dados.get("proximo_id", 1)

        if not isinstance(usuarios, list):
            print("\nErro: lista de usuários inválida.")
            usuarios = []
            proximo_id = 1
            return

        if not isinstance(proximo_id, int):
            proximo_id = 1

    except FileNotFoundError:
        usuarios = []
        proximo_id = 1

    except json.JSONDecodeError:
        print("\nErro: o arquivo usuarios.json está corrompido ou vazio.")
        usuarios = []
        proximo_id = 1

    except PermissionError:
        print("\nErro: não foi possível acessar o arquivo usuarios.json.")
        usuarios = []
        proximo_id = 1

    except OSError as erro:
        print(f"\nErro ao acessar o arquivo: {erro}")
        usuarios = []
        proximo_id = 1


def cadastrar_usuario():
    global proximo_id

    nome = input("Nome: ").strip()

    if not nome:
        print("\nO nome não pode ficar vazio!")
        return

    idade = input("Idade: ")

    if not idade.isdigit():
        print("\nDigite uma idade válida!")
        return

    idade = int(idade)

    if idade < 1 or idade > 120:
        print("\nDigite uma idade entre 1 e 120 anos!")
        return

    email = input("Email: ").strip().lower()

    if not validar_email(email):
        print("\nDigite um email válido!")
        return

    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            print("\nEsse usuário já está cadastrado!")
            return

    for usuario in usuarios:
        if usuario["email"].lower() == email:
            print("\nEsse email já está cadastrado!")
            return

    usuario = {
        "id": proximo_id,
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)

    proximo_id += 1

    salvar_usuarios()

    print(f"\nUsuário cadastrado com sucesso! ID: {usuario['id']}")

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return

    print("\n===== USUÁRIOS CADASTRADOS =====")

    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}")
        print(f"ID: {usuario['id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")

def mostrar_usuario(usuario):
    print("\n===== USUÁRIO ENCONTRADO =====")
    print(f"ID: {usuario['id']}")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Email: {usuario['email']}")

def buscar_usuario():
    print("\n===== BUSCAR USUÁRIO =====")
    print("1 - Buscar por ID")
    print("2 - Buscar por nome")
    print("3 - Buscar por email")
    print("0 - Voltar")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "0":
        return

    if opcao == "1":
        id_busca = input("Digite o ID do usuário: ").strip()

        if not id_busca.isdigit():
            print("\nDigite um ID válido!")
            return

        id_busca = int(id_busca)

        for usuario in usuarios:
            if usuario["id"] == id_busca:
                mostrar_usuario(usuario)
                return

        print("\nUsuário não encontrado.")

    elif opcao == "2":
        nome_busca = input("Digite o nome do usuário: ").strip().lower()

        for usuario in usuarios:
            if usuario["nome"].lower() == nome_busca:
                mostrar_usuario(usuario)
                return

        print("\nUsuário não encontrado.")

    elif opcao == "3":
        email_busca = input("Digite o email do usuário: ").strip().lower()

        for usuario in usuarios:
            if usuario["email"].lower() == email_busca:
                mostrar_usuario(usuario)
                return

        print("\nUsuário não encontrado.")

    else:
        print("\nOpção inválida!")

def editar_usuario():
    id_busca = input("Digite o ID do usuário que deseja editar: ")

    if not id_busca.isdigit():
        print("\nDigite um ID válido!")
        return

    id_busca = int(id_busca)

    for usuario in usuarios:
        if usuario["id"] == id_busca:
            print("\n===== USUÁRIO ENCONTRADO =====")
            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Email: {usuario['email']}")

            print("\nPressione Enter para manter o valor atual.")

            novo_nome = input(f"Novo nome [{usuario['nome']}]: ").strip()        

            if novo_nome:
                usuario["nome"] = novo_nome

            nova_idade =input(f"Nova idade [{usuario['idade']}]: ").strip()

            if nova_idade:
                if not nova_idade.isdigit():
                    print("\nDigite uma idade válida!")
                    return

                nova_idade = int(nova_idade)

                if nova_idade < 1 or nova_idade > 120:
                    print("\nDigite uma idade entre 1 e 120 anos!")
                    return

                usuario["idade"] = (nova_idade)

            novo_email = input(f"Novo email [{usuario['email']}]: ").strip().lower()

            if novo_email:
                if not validar_email(novo_email):
                    print("\nDigite um email válido!")
                    return

                for outro_usuario in usuarios:
                    if outro_usuario["id"] != usuario["id"]:
                        if outro_usuario["email"].lower() == novo_email:
                            print("\nEsse email ja está cadastrado!")
                            return

                usuario["email"] = novo_email

            salvar_usuarios()

            print("\nUsuário atualizado com sucesso!")
            return

    print("\nUsuário não encontrado.")


def excluir_usuario():
    id_busca = input("Digite o ID do usuário que deseja excluir: ")

    if not id_busca.isdigit():
        print("\nDigite um ID válido!")
        return

    id_busca = int(id_busca)

    for usuario in usuarios:
        if usuario["id"] == id_busca:
            print(f"\nUsuário: {usuario['nome']}")

            confirmacao = input("Tem certeza que deseja excluir? s/n: ")

            if confirmacao.lower() == "s":
                usuarios.remove(usuario)
                salvar_usuarios()
                print("\nUsuário excluído com sucesso!")
                return
            else:
                print("\nExclusão cancelada!")
                return

    print("\nUsuário não encontrado.")