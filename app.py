import os

restaurantes = [{
    'name': 'Pizzaria do Zé',
    'category': 'Pizzaria',
    'active': False
    },{
    'name': 'Mike Bomba',
    'category': 'Lanche',
    'active': True
    },{
    'name': 'Feijuca do Porcão',
    'category': 'Comida',
    'active': False
    }]

def exibir_nome_do_programa():
    '''Função para exibir o nome do programa'''
    print("""░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)
    
def exibir_opcoes():
    '''Função para exibir opções'''
    print('1- Cadastrar Restaurante')
    print('2- Listar Restaurantes')
    print('3- Ativar/Desativar Restaurante')
    print('4- Sair\n')
    
def exibir_subtitulo(text):
    '''Função para exibir subtítulo em cada opção do menu'''
    os.system('cls')
    linha = '*' * (len(text))
    print(linha)
    print(text)
    print(linha)
    print()
    
def voltar_ao_menu_principal():
    '''Função para exibir mensagem de retorno ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def cadastrar():
    '''
    Função para cadastrar novo restaurante
    
    Inputs:
    - Nome do Restaurante
    - Categoria do Restaurante
    
    Outputs:
    - Adiciona o restaurante à uma lista de restaurantes
    '''
    exibir_subtitulo('Cadastrar Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Qual a categoria do restaurante {nome_do_restaurante}? ')
    dados_do_restaurante = {'name': nome_do_restaurante, 'category': categoria_do_restaurante, 'active': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar():
    '''Função para listar os restaurantes, exibindo nome, categoria e seu estado (ativo/inativo)'''
    exibir_subtitulo('Listar Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(28)} | {'Categoria'.ljust(20)} | Status')
    for indice, restaurante in enumerate(restaurantes):
            nome_restaurante = restaurante['name']
            categoria_restaurante = restaurante['category']
            ativo_restaurante = restaurante['active']
            print(f'{indice + 1}- {nome_restaurante.ljust(25)} | {categoria_restaurante.ljust(20)} | {'Ativo' if ativo_restaurante else 'Inativo'}')
    voltar_ao_menu_principal()

def alternar_estado():
    '''
    Função para alternar estado do restaurante
    
    Inputs:
    - Nome do restaurante
    
    Outputs:
    - Alterna o estado do restaurante (ativo/inativo)
    
    '''
    exibir_subtitulo('Alternar Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado (ativo/inativo): ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['name']:
            restaurante_encontrado = True
            restaurante['active'] = not restaurante['active']
            mensagem = f'O restaurante {nome_restaurante} agora está ATIVO!' if restaurante['active'] else f'O restaurante {nome_restaurante} agora está INATIVO!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal() 
    
def finalizar():
    '''Função que exibe mensagem de encerramento do programa'''
    exibir_subtitulo('Encerrando o programa... \nObrigado por utilizar nosso serviço.\n')

def opcao_invalida():
    '''Função que exibe opção inválida'''
    print('Opção inválida.\nFavor inserir opção válida.\n')
    voltar_ao_menu_principal() 

def escolher_opcoes():
    '''Função para escolher uma opção do Menu'''
    try:
        opcao_escolhida = int(input('Digite uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar()
        elif opcao_escolhida == 2:
            listar()
        elif opcao_escolhida == 3:
            alternar_estado()
        elif opcao_escolhida == 4:
            finalizar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    '''Função principal, para iniciar o programa e exibir nome do programa, menu de opções e função para escolher'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()