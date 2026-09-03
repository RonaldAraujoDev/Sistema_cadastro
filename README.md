Sistema de Cadastro de Usuários

Sistema de cadastro de usuários desenvolvido em Python, com armazenamento dos dados em arquivo JSON.

Funcionalidades
Cadastrar usuário
Listar usuários
Buscar usuário por ID, nome ou e-mail
Editar usuário
Excluir usuário
Validação de idade
Validação básica de e-mail
Impedimento de usuários duplicados
Impedimento de e-mails duplicados
Persistência dos dados em arquivo JSON


Tecnologias utilizadas
Python 3
JSON
Git
GitHub


Estrutura do projeto
Sistema_cadastro/
│
├── main.py          # Menu principal e execução do sistema
├── usuarios.py      # Funções e regras dos usuários
├── usuarios.json    # Armazenamento dos dados
└── README.md        # Documentação do projeto


Como executar
1- Clone este repositório.
2 - Abra a pasta do projeto no VS Code ou no terminal.
3 - Execute:

python main.py

O sistema será iniciado diretamente no terminal.

Exemplo
==================================================
           SISTEMA DE CADASTRO
==================================================

┌──────────────────────────────────────────────┐
│                  MENU PRINCIPAL              │
├──────────────────────────────────────────────┤
│  1 - Cadastrar usuário                       │
│  2 - Listar usuários                         │
│  3 - Buscar usuário                          │
│  4 - Editar usuário                          │
│  5 - Excluir usuário                         │
│  0 - Sair                                    │
└──────────────────────────────────────────────┘