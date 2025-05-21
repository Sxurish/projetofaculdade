import mysql.connector
from rich import print as rprint
from time import sleep

def inputint(msg):
    while True:
        numero = input(msg)
        if numero.isnumeric():
            return int(numero)
        rprint('[bold red]Digite o número correspondente a opção![/]')
def mensagem(msg):
    tamanho = len(msg) + 6
    print('='* tamanho)
    print(f'{msg:^{tamanho}}')
    print('='* tamanho)
    
cliente = False
funcionario = False
acesso_gestor = False
try:
    #conexao = mysql.connector.connect(
    #    host='localhost',
    #    user='root',
    #    password='',
    #    database='projeto_final_bd'
    #)
    #cursor = conexao.cursor()

    while True:
        mensagem('DARCAN - MATERIAIS DE CONSTRUÇÃO')
        print('Menu:' \
        '\n[ 1 ] - Login' \
        '\n[ 2 ] - Consultar Produto' \
        '\n[ 3 ] - Fazer Pedido')
        if funcionario == True:
            print('[ 4 ] - Estoque' \
            '\n[ 5 ] - Relatório de Vendas')
            if acesso_gestor == True:
                print('[ 6 ] - Cadastros')
        print('[ 0 ] - Sair do Programa')
        menu = inputint('Opção: ')

        if menu == 1: #Login
            while True:
                mensagem('LOGIN')
                print('menu:' \
                '\n[ 1 ] - Cliente' \
                '\n[ 2 ] - Funcionario' \
                '\n[ 0 ] - Voltar')
                login = inputint('Opção: ')
                if login == 1:
                    cliente = True
                    funcionario = False
                    acesso_gestor = False
                    rprint('[green]Login como cliente realizado com sucesso![/]')
                    sleep(1)
                elif login == 2:
                    cliente = False
                    funcionario = True
                    acesso_gestor = False
                    rprint('[green]Login como funcionário realizado com sucesso![/]')
                    sleep(1)
                elif login == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)

        elif menu == 2: #Consultar Produto
            while True:
                mensagem('CONSULTAR PRODUTO')
                print('menu:' \
                '\n[ 1 ] - Pesquisa por nome' \
                '\n[ 2 ] - Pesquisa por categoria' \
                '\n[ 0 ] - Voltar')
                consultar = inputint('Opção: ')
                if consultar == 1:
                    print('=' * 29)
                    nome = input('Digite o nome do Produto: ')
                elif consultar == 2:
                    print('=' * 29)
                    #Mostrar as Categorias e seus ids.
                    categ = inputint('Numero da Categoria: ')
                elif consultar == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)

        elif menu == 3: #Fazer Pedido
            if funcionario or not cliente:
                rprint("[bold red]Faça Login como Cliente![/]")
            elif cliente:
                lista_pedido = 0
                while True:
                    mensagem('FAÇA SEU PEDIDO!')
                    print('menu:' \
                    '\n[ 1 ] - Pesquisar Produto' \
                    '\n[ 2 ] - Adicionar ao Pedido')
                    if lista_pedido > 0:
                        print('[ 3 ] - Ver o pedido' \
                        '\n[ 4 ] - Cancelar Pedido' \
                        '\n[ 5 ] - Fechar Pedido')
                    elif lista_pedido == 0:
                        print('[ 0 ] - Voltar')
                    pedido_opc = inputint('Opção: ')

                    if pedido_opc == 1:
                        #Pesquisar pedido
                        pass
                    elif pedido_opc == 2:
                        #Adicionado ao pedido
                        lista_pedido += 1
                    elif pedido_opc == 3 and lista_pedido > 0:
                        #Ver o pedido
                        pass
                    elif pedido_opc == 4 and lista_pedido > 0:
                        print('Pedido Cancelado!')
                        print('Voltando ao menu...')
                        sleep(1)
                        break
                    elif pedido_opc == 5 and lista_pedido > 0:
                        #Finalizar Pedido
                        pass
                    elif pedido_opc == 0 and lista_pedido == 0:
                        print('Voltando ao menu...')
                        sleep(1)
                        break
                    else:
                        rprint('[bold red]Opção Inválida![/]')
                        sleep(1)
                
        elif menu == 4 and funcionario: #Estoque
            while True:
                mensagem('ESTOQUE')
                print('menu: ' \
                '\n[ 1 ] - Pesquisar Produto' \
                '\n[ 2 ] - Produtos com Estoque Baixo' \
                '\n[ 3 ] - Lançar Entrada de Produto' \
                '\n[ 4 ] - Adicionar Novo Produto' \
                '\n[ 5 ] - Lançar Quebra ou Perda de Produto' \
                '\n[ 0 ] - Voltar')
                estoque = inputint('Opção: ')
                
                if estoque == 1:
                    #Pesquisar Produto
                    pass
                elif estoque == 2:
                    #Produtos com Estoque Baixo
                    pass
                elif estoque == 3:
                    #Lançar Entrada de Produto
                    pass
                elif estoque == 4:
                    #Adicionar Novo Produto
                    pass
                elif estoque == 5:
                    #Lançar Quebra ou Perda de Produto
                    pass
                elif estoque == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)
                
        elif menu == 5 and funcionario: #Relatório de Vendas
            while True:
                mensagem('RELATÓRIO DE VENDAS')
                print('menu:' \
                '\n[ 1 ] - Ver Pedidos Realizados' \
                '\n[ 2 ] - Ver Produtos Vendidos' \
                '\n[ 0 ] - Voltar')
                vendas = inputint('Opção: ')

                if vendas == 1: #Pedidos Realizados
                    while True:
                        mensagem('PEDIDOS REALIZADOS')
                        print('menu:' \
                        '\n[ 1 ] - Por Cliente' \
                        '\n[ 2 ] - Por Data' \
                        '\n[ 0 ] - Voltar')
                        realizados = inputint('Opção: ')

                        if realizados == 1:
                            #Por Cliente
                            pass
                        elif realizados == 2:
                            #Por Data
                            pass
                        elif realizados == 0:
                            print('Voltando ao relatório de vendas...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                
                elif vendas == 2: #Produtos Vendidos
                    while True:
                        mensagem('PRODUTOS VENDIDOS')
                        print('menu:' \
                        '\n[ 1 ] - Por Quantidade' \
                        '\n[ 2 ] - Por Valor' \
                        '\n[ 0 ] - Voltar')
                        prodvend = inputint('Opção: ')
                        
                        if prodvend == 1: #Por Quantidade
                            mensagem('Por Quantidade')
                            print('menu:' \
                            '\n[ 1 ] - 5 Mais Vendidos' \
                            '\n[ 2 ] - 5 Menos Vendidos' \
                            '\n[ 0 ] - Voltar')
                            prodquant = inputint('Opção: ')
                            
                            if prodquant == 1:
                                #5 Mais Vendidos
                                pass
                            elif prodquant == 2:    
                                #5 Menos Vendidos
                                pass
                            elif prodquant == 0:
                                print('Voltando ao relatório de vendas...')
                                sleep(1)
                                break
                            else:
                                rprint('[bold red]Opção Inválida![/]')
                                sleep(1)

                        elif prodvend == 2: #Por Valor
                            mensagem('Por Valor')
                            print('menu:' \
                            '\n[ 1 ] - 5 Mais Vendidos' \
                            '\n[ 2 ] - 5 Menos Vendidos' \
                            '\n[ 0 ] - Voltar')
                            prodvalor = inputint('Opção: ')

                            if prodvalor == 1:
                                #5 Mais Vendidos
                                pass
                            elif prodvalor == 2:    
                                #5 Menos Vendidos
                                pass
                            elif prodvalor == 0:
                                print('Voltando ao relatório de vendas...')
                                sleep(1)
                                break
                            else:
                                rprint('[bold red]Opção Inválida![/]')
                                sleep(1)

                        elif prodvend == 0:
                            print('Voltando ao relatório de vendas...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                elif vendas == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)
                
        elif menu == 6 and funcionario and acesso_gestor: #Cadastros
            while True:
                mensagem('CADASTRADOS')
                print('menu: ' \
                '\n[ 1 ] - Ver Cadastros Clientes' \
                '\n[ 2 ] - Funcionários' \
                '\n[ 0 ] - Voltar')
                cadastro = inputint('Opção: ')
                
                if cadastro == 1:
                    #Mostrar os clientes cadastrados
                    pass
                elif cadastro == 2:
                    #Mostrar os funcionarios cadastrados
                    pass
                elif cadastro == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)

        elif menu == 0:
            mensagem('OBRIGADO! VOLTE SEMPRE!')
            break
        else:
            rprint('[bold red]Opção Inválida![/]')
            sleep(1)
            
except Exception as err:
    print(f'Erro: {err.__class__}')

#finally:
    #if conexao.is_connected:
    #    cursor.close()
    #     conexao.close()
print('Fim do Programa.')
