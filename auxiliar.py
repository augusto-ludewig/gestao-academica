# Menu principal
def print_menu_principal():
    print('****** MENU PRINCIPAL ******\n')
    print('(1) Gerenciar estudantes')
    print('(2) Gerenciar disciplinas')
    print('(3) Gerenciar professores')
    print('(4) Gerenciar turmas')
    print('(5) Gerenciar matriculas')
    print('(0) Sair')
    categoria = str(input('\nInforme a opção desejada: '))  # Entrada de dados para seleção
    return categoria

# Sub menu - Funcionalidades
def print_menu_funcionalidades(categoria):
    print('\n***** [' + categoria.upper() + '] MENU DE OPERAÇÕES *****')
    print('(1) Incluir')
    print('(2) Listar')
    print('(3) Excluir')
    print('(4) Alterar')
    print('(0) Voltar ao menu principal')
    funcionalidade = input('\nInforma a ação desejada: ').lower()
    return funcionalidade

# Listagem
def listar(categoria, lista):
    print('\n' + categoria + ':')
    for key, item in lista.items():
        print(key, item)