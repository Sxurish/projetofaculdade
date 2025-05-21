import mysql.connector
from funcoes.conexaomysql import *
from funcoes.formatacao import *
from funcoes.validacao import *
from rich import print as rprint
from time import sleep

cliente = False
funcionario = True
acesso_gestor = True
id_cliente = 1
nome_cliente = ''
id_funcionario = 1
nome_funcionario = ''

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='22222121',
        database='projeto_final_bd'
    )
    cursor = conexao.cursor()

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
                    nome_produto = input('Digite o nome do Produto: ').strip()
                    produto_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'nome_produto', nome_produto, retornar_colunas='id_produto, nome_produto, desc_produto, qtd_produto, valor_produto', usar_like=True)
                    if not produto_procurado:
                        rprint('[bold red]Produto não encontrado![/]')
                        sleep(1)
                        continue
                    mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Quantidade', 'Valor')

                elif consultar == 2:
                    categorias = select_tabela(conexao, cursor, 'tbl_categorias')
                    mostrar_tabela(categorias, 'Categorias', 'ID', 'Nome')       
                    categ = inputint('ID da Categoria: ')
                    nome_categ = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_categorias', 'id_categoria', categ, 'nome_categoria', descompactar=True)
                    if not nome_categ:
                        rprint('[bold red]Categoria não encontrada![/]')
                        sleep(1)
                        continue
                    result_categ = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.valor_produto', ['tbl_estoque_produtos', 'tbl_categorias'], 'tbl_categorias.id_categoria',
                        str(categ), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria'])
                    mostrar_tabela(result_categ, *nome_categ, 'ID', 'Nome', 'Descrição', 'Quantidade', 'Valor')

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
                '\n[ 2 ] - Produtos Para Repor' \
                '\n[ 3 ] - Produtos com Estoque Zerado' \
                '\n[ 4 ] - Lançar Entrada de Produto' \
                '\n[ 5 ] - Lançar Quebra ou Perda de Produto' \
                '\n[ 6 ] - Editar Dados do Produto' \
                '\n[ 7 ] - Adicionar Novo Produto' \
                '\n[ 0 ] - Voltar')
                estoque = inputint('Opção: ')
                
                if estoque == 1: #Pesquisar Produto
                    while True:
                        mensagem('PESQUISAR PRODUTO')
                        print('menu:' \
                        '\n[ 1 ] - Por Nome' \
                        '\n[ 2 ] - Por Categoria' \
                        '\n[ 3 ] - Por ID do Produto' \
                        '\n[ 0 ] - Voltar')
                        pesquisar = inputint('Opção: ')
                        
                        if pesquisar == 1:
                            #Por Nome
                            nome_produto = input('Digite o nome do Produto: ').strip()
                            produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor, retornar_colunas='tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias', 'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.nome_produto', dado_procurado=nome_produto, joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'], usar_like=True)
                            if not produto_procurado:
                                rprint('[bold red]Produto não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)

                        elif pesquisar == 2:
                            #Por Categoria
                            categorias = select_tabela(conexao, cursor, 'tbl_categorias')
                            mostrar_tabela(categorias, 'Categorias', 'ID', 'Nome')
                            categ = inputint('ID da Categoria: ')
                            nome_categoria = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_categorias', 'id_categoria', categ, 'nome_categoria',
                                                                         descompactar=True)
                            print(nome_categoria)
                            if not nome_categoria:
                                rprint('[bold red]Categoria não encontrada![/]')
                                sleep(1)
                                continue
                            result_categ = procurar_na_tabela_com_condicao_joins(conexao, cursor,
                            retornar_colunas='tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], onde_procurar='tbl_categorias.id_categoria', dado_procurado=str(categ), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                            mostrar_tabela(result_categ, *nome_categoria, 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)

                        elif pesquisar == 3:
                            #Por ID do Produto
                            id_produto = inputint('ID do Produto: ')
                            produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor,
                            retornar_colunas='tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.id_produto', dado_procurado=str(id_produto), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                            print('Foi')
                            if not produto_procurado:
                                rprint('[bold red]Produto não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)

                        elif pesquisar == 0:
                            print('Voltando ao estoque...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                    
                elif estoque == 2: #Produtos com Estoque Baixo
                   est_abaixo = procurar_na_tabela_com_condicao_joins(conexao, cursor, 'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.qtd_produto', dado_procurado='tbl_estoque_produtos.qtd_minima_produto', joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'], operador='<', comparar_colunas=True, And='tbl_estoque_produtos.qtd_produto <> 0')
                   if not est_abaixo:
                       rprint('[bold red]Não há produtos com estoque abaixo do mínimo e acima de zero![/]')
                       sleep(1)
                       continue
                   mostrar_tabela(est_abaixo, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                   
                elif estoque == 3: #Produtos com Estoque Zerado
                    est_zero = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.qtd_produto', dado_procurado=0, joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                    if not est_zero:
                        rprint('[bold red]Não há produtos com estoque zerado![/]')
                        sleep(1)
                        continue
                    mostrar_tabela(est_zero, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)

                elif estoque == 4: #Lançar Entrada de Produto
                    while True:
                        mensagem('LANÇAR ENTRADA DE PRDUTO')
                        id_produto = inputint('ID do Produto [digite 0 para voltar]: ')
                        if id_produto == 0:
                            print('Voltando ao estoque...')
                            sleep(1)
                            break
                        produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias', 'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.id_produto', dado_procurado=str(id_produto), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                        if not produto_procurado:
                            rprint('[bold red]Produto não encontrado![/]')
                            sleep(1)
                            continue
                        nome_produto = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'nome_produto', descompactar=True)
                        mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                        qtd_produto = inputint('Quantidade a ser adicionada: ')
                        if qtd_produto <0:
                            rprint('[bold red]Quantidade inválida![/]')
                            sleep(1)
                            continue
                        confirmar = inputint(f'Deseja adicionar {qtd_produto} unidades do produto {nome_produto[0]} [1 - Sim / 2 - Não]: ')
                        if confirmar == 1:
                            #Atualizar a quantidade do produto
                            qtd_atual = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'qtd_produto', descompactar=True)
                            nova_qtd = int(*qtd_atual) + qtd_produto
                            atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['qtd_produto'], (str(nova_qtd),), 'id_produto', str(id_produto))
                            rprint(f'[green]Entrada de {qtd_produto} unidades do produto {nome_produto[0]} lançada com sucesso![/]')  
                            sleep(1) 
                        else:
                            rprint('[bold red]Operação cancelada![/]')
                            sleep(1)
                            continue

                elif estoque == 5: #Lançar Quebra ou Perda de Produto
                    while True:
                        mensagem('LANÇAR QUEBRA OU PERDA DE PRODUTO')
                        id_produto = inputint('ID do Produto [digite 0 para voltar]: ')
                        if id_produto == 0:
                            print('Voltando ao estoque...')
                            sleep(1)
                            break
                        produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias', 'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.id_produto', dado_procurado=str(id_produto), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                        if not produto_procurado:
                            rprint('[bold red]Produto não encontrado![/]')
                            sleep(1)
                            continue
                        nome_produto = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'nome_produto', descompactar=True)
                        mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                        qtd_produto = inputint('Quantidade a ser retirada: ')
                        if qtd_produto <0:
                            rprint('[bold red]Quantidade inválida![/]')
                            sleep(1)
                            continue 
                        confirmar = inputint(f'Deseja retirar {qtd_produto} unidades do produto {nome_produto[0]} [1 - Sim / 2 - Não]: ')
                        if confirmar == 1:
                            #Atualizar a quantidade do produto
                            qtd_atual = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'qtd_produto', descompactar=True)
                            nova_qtd = int(*qtd_atual) - qtd_produto
                            if nova_qtd < 0:
                                rprint('[bold red]Quantidade inválida![/]')
                                sleep(1)
                                continue
                            atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['qtd_produto'], (str(nova_qtd),), 'id_produto', str(id_produto))
                            rprint(f'[green]Quebra ou perda de {qtd_produto} unidades do produto {nome_produto[0]} lançada com sucesso![/]')  
                            sleep(1)
                        else:
                            rprint('[bold red]Operação cancelada![/]')
                            sleep(1)
                            continue

                elif estoque == 6: #Editar Dados do Produto 
                    while True:
                        mensagem('EDITAR DADOS DO PRODUTO')
                        id_produto = inputint('ID do Produto [digite 0 para voltar]: ')
                        if id_produto == 0:
                            print('Voltando ao estoque...')
                            sleep(1)
                            break
                        produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias', 'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.id_produto', dado_procurado=str(id_produto), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                        if not produto_procurado:
                            rprint('[bold red]Produto não encontrado![/]')
                            sleep(1)
                            continue
                        nome_produto = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'nome_produto', descompactar=True)
                        mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                        #Editar os dados do produto
                        print('menu:' \
                        '\n[ 1 ] - Nome' \
                        '\n[ 2 ] - Descrição' \
                        '\n[ 3 ] - Categoria' \
                        '\n[ 4 ] - Quantidade Mínima' \
                        '\n[ 5 ] - Valor' \
                        '\n[ 0 ] - Voltar')
                        editar = inputint('Opção: ')

                        if editar == 1:
                            novo_nome = input('Novo Nome: ')
                            confirmar = inputint(f'Deseja alterar o nome do produto {nome_produto[0]} para {novo_nome} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['nome_produto'], (novo_nome,), 'id_produto', str(id_produto))
                                rprint(f'[green]Nome do produto {nome_produto[0]} alterado para {novo_nome} com sucesso![/]')  
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                                continue
                        elif editar == 2:
                            novo_desc = input('Nova Descrição: ')
                            confirmar = inputint(f'Deseja alterar a descrição do produto {nome_produto[0]} para {novo_desc} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['desc_produto'], (novo_desc,), 'id_produto', str(id_produto))
                                rprint(f'[green]Descrição do produto {nome_produto[0]} alterada para {novo_desc} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        elif editar == 3:   
                            #Mostrar as categorias cadastradas
                            categorias = select_tabela(conexao, cursor, 'tbl_categorias')
                            mostrar_tabela(categorias, 'Categorias', 'ID', 'Nome')
                            nova_categoria = inputint('ID da Nova Categoria: ')
                            nome_categoria = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_categorias', 'id_categoria', str(nova_categoria), 'nome_categoria', descompactar=True)
                            if not nome_categoria:
                                rprint('[bold red]Categoria não encontrada![/]')
                                sleep(1)
                                continue
                            confirmar = inputint(f'Deseja alterar a categoria do produto {nome_produto[0]} para {nome_categoria[0]} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['fk_tbl_categorias_id_categoria'], (str(nova_categoria),), 'id_produto', str(id_produto))
                                rprint(f'[green]Categoria do produto {nome_produto[0]} alterada para {nome_categoria[0]} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1) 
                        elif editar == 4:
                            nova_qtd_minima = inputint('Nova Quantidade Mínima: ')
                            confirmar = inputint(f'Deseja alterar a quantidade mínima do produto {nome_produto[0]} para {nova_qtd_minima} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['qtd_minima_produto'], (str(nova_qtd_minima),), 'id_produto', str(id_produto))
                                rprint(f'[green]Quantidade mínima do produto {nome_produto[0]} alterada para {nova_qtd_minima} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        elif editar == 5:
                            novo_valor = inputfloat('Novo Valor: ')
                            confirmar = inputint(f'Deseja alterar o valor do produto {nome_produto[0]} para {novo_valor} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['valor_produto'], (str(novo_valor),), 'id_produto', str(id_produto))
                                rprint(f'[green]Valor do produto {nome_produto[0]} alterado para {novo_valor} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        elif editar == 0:
                            print('Voltando ao estoque...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)

                elif estoque == 7: #Adicionar Novo Produto
                    while True:
                        mensagem('ADICIONAR NOVO PRODUTO')
                        nome_produto = inputstr('Nome do Produto: ').strip()
                        desc_produto = inputstr('Descrição do Produto: ').strip()
                        #Mostrar as categorias cadastradas
                        categorias = select_tabela(conexao, cursor, 'tbl_categorias')
                        mostrar_tabela(categorias, 'Categorias', 'ID', 'Nome')
                        nova_categoria = inputint('ID da Categoria: ')
                        verifica_categoria = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_categorias', 'id_categoria', str(nova_categoria), 'nome_categoria', descompactar=True)
                        if not verifica_categoria:
                            rprint('[bold red]Categoria não encontrada![/]')
                            sleep(1)
                            continue
                        nova_qtd = inputint('Quantidade do Produto: ')
                        nova_qtd_minima = inputint('Quantidade Mínima do Produto: ')
                        novo_valor = inputfloat('Valor do Produto: ')
                        confirmar = inputint(f'Deseja adicionar o produto {nome_produto} [1 - Sim / 2 - Não]: ')
                        if confirmar == 1:
                            #inserir o produto na tabela
                            inserir_registro(conexao, cursor, 'tbl_estoque_produtos', ['nome_produto', 'desc_produto', 'fk_tbl_categorias_id_categoria', 'qtd_produto', 'qtd_minima_produto', 'valor_produto', 'fk_tbl_funcionarios_id_funcionario'], (nome_produto, desc_produto, str(nova_categoria), str(nova_qtd), str(nova_qtd_minima), str(novo_valor), str(id_funcionario)))
                            rprint(f'[green]Produto {nome_produto} adicionado com sucesso![/]')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Operação cancelada![/]')
                            sleep(1)
                            break

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
                '\n[ 1 ] - Pesquisar Clientes' \
                '\n[ 2 ] - Editar Dados de Cliente' \
                '\n[ 3 ] - Pesquisar Funcionários' \
                '\n[ 4 ] - Editar Dados de Funcionário' \
                '\n[ 0 ] - Voltar')
                cadastro = inputint('Opção: ')
                
                if cadastro == 1: #Mostrar os clientes cadastrados
                    while True:
                        mensagem('PESQUISAR CLIENTE')
                        print('menu:' \
                        '\n[ 1 ] - Por Nome' \
                        '\n[ 2 ] - Por CPF' \
                        '\n[ 3 ] - Por ID do Cliente' \
                        '\n[ 0 ] - Voltar')
                        pesquisar = inputint('Opção: ')
                        
                        if pesquisar == 1: #Por Nome
                            nome_cliente = inputstr('Digite o nome do Cliente: ').strip()
                            cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'nome_cliente', nome_cliente, usar_like=True)
                            if not cliente_procurado:
                                rprint('[bold red]Cliente não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(cliente_procurado, 'Cliente', 'ID', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')

                        elif pesquisar == 2: #Por CPF
                            cpf_cliente = input('Digite o CPF do Cliente: ').strip()
                            cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', cpf_cliente)
                            if not cliente_procurado:
                                rprint('[bold red]Cliente não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(cliente_procurado, 'Cliente', 'ID', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')

                        elif pesquisar == 3: #Por ID do Cliente
                            id_cliente = inputint('ID do Cliente: ')
                            cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'id_cliente', str(id_cliente))
                            if not cliente_procurado:
                                rprint('[bold red]Cliente não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(cliente_procurado, 'Cliente', 'ID', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')

                        elif pesquisar == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                    
                elif cadastro == 2: #Editar os dados do cliente
                    while True:
                        mensagem('EDITAR DADOS DO CLIENTE')
                        id_cliente = inputint('ID do Cliente [digite 0 para voltar]: ')
                        if id_cliente == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'id_cliente', str(id_cliente))
                        if not cliente_procurado:
                            rprint('[bold red]Cliente não encontrado![/]')
                            sleep(1)
                            continue
                        nome_cliente = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'id_cliente', str(id_cliente), 'nome_cliente', descompactar=True)
                        mostrar_tabela(cliente_procurado, 'Cliente', 'ID', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')
                        #Editar os dados do cliente
                        print('menu:' \
                        '\n[ 1 ] - Nome' \
                        '\n[ 2 ] - CPF' \
                        '\n[ 3 ] - Telefone' \
                        '\n[ 4 ] - E-mail' \
                        '\n[ 5 ] - Senha' \
                        '\n[ 6 ] - Endereço' \
                        '\n[ 0 ] - Voltar')
                        editar = inputint('Opção: ')
                        
                        if editar == 1: #Nome
                            novo_nome = inputstr('Novo Nome: ').strip()
                            confirmar = inputint(f'Deseja alterar o nome do cliente {nome_cliente[0]} para {novo_nome} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_clientes', ['nome_cliente'], (novo_nome,), 'id_cliente', str(id_cliente))
                                rprint(f'[green]Nome do cliente {nome_cliente[0]} alterado para {novo_nome} com sucesso![/]')  
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                                continue
                        
                        elif editar == 2: #CPF
                            novo_cpf = inputstr('Novo CPF: ').strip() #Fazer a validação do CPF depois.
                            #Verifica se o CPF já existe
                            cpf_existente = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', novo_cpf)
                            if cpf_existente:
                                rprint('[bold red]CPF já cadastrado![/]')
                                sleep(1)
                                continue
                            confirmar = inputint(f'Deseja alterar o CPF do cliente {nome_cliente[0]} para {novo_cpf} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_clientes', ['cpf_cliente'], (novo_cpf,), 'id_cliente', str(id_cliente))
                                rprint(f'[green]CPF do cliente {nome_cliente[0]} alterado para {novo_cpf} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        
                        elif editar == 3: #Telefone
                            novo_telefone = inputstr('Novo Telefone: ').strip() #Fazer a validação do telefone depois.
                            confirmar = inputint(f'Deseja alterar o telefone do cliente {nome_cliente[0]} para {novo_telefone} [1 - Sim / 2 - Não]:  ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_clientes', ['telefone_cliente'], (novo_telefone,), 'id_cliente', str(id_cliente))
                                rprint(f'[green]Telefone do cliente {nome_cliente[0]} altererado para {novo_telefone} com sucesso!"[/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)          
                        
                        elif editar == 4: #E-mail
                            novo_email = inputstr('Novo E-mail: ').strip() #Validar o e-mail talvez.
                            confirmar = inputint(f'Deseja alterar o e-mail do cliente {nome_cliente[0]} para {novo_email} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_clientes', ['email_cliente'], (novo_email,), 'id_cliente', str(id_cliente))
                                rprint(f'[green]E-mail do cliente {nome_cliente[0]} alterado para {novo_email} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        
                        elif editar == 5: #Senha
                            nova_senha = inputstr('Nova Senha: ').strip() #Fazer a validação da senha depois.
                            if len(nova_senha) < 6:
                                rprint('[bold red]A senha deve ter no mínimo 6 caracteres![/]')
                                sleep(1)
                                continue
                            elif len(nova_senha) > 20:
                                rprint('[bold red]A senha deve ter no máximo 20 caracteres![/]')
                                sleep(1)
                                continue
                            confirmar = inputint(f'Deseja alterar a senha do cliente {nome_cliente[0]} para {nova_senha} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_clientes', ['senha_cliente'], (nova_senha,), 'id_cliente', str(id_cliente))
                                rprint(f'[green]Senha do cliente {nome_cliente[0]} alterada com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        
                        elif editar == 6: #Endereço
                            novo_endereco = inputstr('Novo Endereço: ').strip() #Fazer a validação de endereço depois.
                            confirmar = inputint(f'Deseja alterar o endereço do cliente {nome_cliente[0]} para {novo_endereco} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_clientes', ['endereco_cliente'], (novo_endereco,), 'id_cliente', str(id_cliente))
                                rprint(f'[green]Endereço do cliente {nome_cliente[0]} alterado para {novo_endereco} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        
                        elif editar == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)

                elif cadastro == 3: #Mostrar os funcionarios cadastrados
                    while True:
                        mensagem('PESQUISAR FUNCIONÁRIO')
                        print('menu:' \
                        '\n[ 1 ] - Por Nome' \
                        '\n[ 2 ] - Por Login' \
                        '\n[ 3 ] - Por ID do Funcionário' \
                        '\n[ 0 ] - Voltar')
                        pesquisar = inputint('Opção: ')
                        
                        if pesquisar == 1: #Por Nome
                            nome_funcionario = inputstr('Digite o nome do Funcionário: ').strip()
                            funcionario_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'nome_funcionario', nome_funcionario, 'id_funcionario, nome_funcionario, login_funcionario, senha_funcionario, acesso_gestor', usar_like=True)
                            if not funcionario_procurado:
                                rprint('[bold red]Funcionário não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(funcionario_procurado, 'Funcionário', 'ID', 'Nome', 'Login', 'Senha', 'Nivel de Acesso')
                        
                        elif pesquisar == 2: #Por Login
                            login_funcionario = inputstr('Digite o Login do Funcionário: ').strip()
                            funcionario_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', login_funcionario, 'id_funcionario, nome_funcionario, login_funcionario, senha_funcionario, acesso_gestor', usar_like=True)
                            if not funcionario_procurado:
                                rprint('[bold red]Funcionário não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(funcionario_procurado, 'Funcionário', 'ID', 'Nome', 'Login', 'Senha', 'Nivel de Acesso')
                        
                        elif pesquisar == 3: #Por ID do Funcionário
                            id_funcionario = inputint('ID do Funcionário: ')
                            funcionario_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'id_funcionario', str(id_funcionario), 'id_funcionario, nome_funcionario, login_funcionario, senha_funcionario, acesso_gestor')
                            if not funcionario_procurado:
                                rprint('[bold red]Funcionário não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(funcionario_procurado, 'Funcionário', 'ID', 'Nome', 'Login', 'Senha', 'Nivel de Acesso')
                        
                        elif pesquisar == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)

                elif cadastro == 4: #Editar os dados do funcionario
                    while True:
                        mensagem('EDITAR DADOS DO FUNCIONÁRIO')
                        id_funcionario = inputint('ID do Funcionário [digite 0 para voltar]: ')
                        if id_funcionario == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        funcionario_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'id_funcionario', str(id_funcionario), 'id_funcionario, nome_funcionario, login_funcionario, senha_funcionario, acesso_gestor')
                        if not funcionario_procurado:
                            rprint('[bold red]Funcionário não encontrado![/]')
                            sleep(1)
                            continue
                        nome_funcionario = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'id_funcionario', str(id_funcionario), 'nome_funcionario', descompactar=True)
                        mostrar_tabela(funcionario_procurado, 'Funcionário', 'ID', 'Nome', 'Login', 'Senha', 'Nivel de Acesso')
                        #Editar os dados do funcionario
                        print('menu:' \
                        '\n[ 1 ] - Nome' \
                        '\n[ 2 ] - Login' \
                        '\n[ 3 ] - Senha' \
                        '\n[ 4 ] - Nivel de Acesso' \
                        '\n[ 0 ] - Voltar')
                        editar = inputint('Opção: ')
                        
                        if editar == 1: #Nome
                            novo_nome = inputstr('Novo Nome: ').strip()
                            confirmar = inputint(f'Deseja alterar o nome do funcionário {nome_funcionario[0]} para {novo_nome} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_funcionarios', ['nome_funcionario'], (novo_nome,), 'id_funcionario', str(id_funcionario))
                                rprint(f'[green]Nome do funcionário {nome_funcionario[0]} alterado para {novo_nome} com sucesso![/]')  
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                                continue

                        elif editar == 2: #Login
                            novo_login = inputstr('Novo Login: ').strip() #Fazer a validação do login depois.
                            #Verifica se o Login já existe
                            login_existente = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', novo_login)
                            if login_existente:
                                rprint('[bold red]Login já cadastrado![/]')
                                sleep(1)
                                continue
                            confirmar = inputint(f'Deseja alterar o login do funcionário {nome_funcionario[0]} para {novo_login} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_funcionarios', ['login_funcionario'], (novo_login,), 'id_funcionario', str(id_funcionario))
                                rprint(f'[green]Login do funcionário {nome_funcionario[0]} alterado para {novo_login} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)

                        elif editar == 3: #Senha
                            nova_senha = inputstr('Nova Senha: ').strip() #Fazer a validação da senha depois.
                            if len(nova_senha) < 6:
                                rprint('[bold red]A senha deve ter no mínimo 6 caracteres![/]')
                                sleep(1)
                                continue
                            elif len(nova_senha) > 20:
                                rprint('[bold red]A senha deve ter no máximo 20 caracteres![/]')
                                sleep(1)
                                continue
                            confirmar = inputint(f'Deseja alterar a senha do funcionário {nome_funcionario[0]} para {nova_senha} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_funcionarios', ['senha_funcionario'], (nova_senha,), 'id_funcionario', str(id_funcionario))
                                rprint(f'[green]Senha do funcionário {nome_funcionario[0]} alterada com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        
                        elif editar == 4: #Nivel de Acesso
                            nivel_acesso = inputint('Novo Nivel de Acesso [1 - Funcionario / 2 - Gestor]: ')
                            if nivel_acesso == 1:
                                cargo = 'Funcionario'
                                novo_acesso = 0
                            elif nivel_acesso == 2:
                                cargo = 'Gestor'
                                novo_acesso = 1
                            else:
                                rprint('[bold red]Opção Inválida![/]')
                                sleep(1)
                                continue
                            confirmar = inputint(f'Deseja alterar o nivel de acesso do funcionário {nome_funcionario[0]} para {cargo} [1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                atualizar_registro(conexao, cursor, 'tbl_funcionarios', ['acesso_gestor'], (str(novo_acesso),), 'id_funcionario', str(id_funcionario))
                                rprint(f'[green]Nivel de acesso do funcionário {nome_funcionario[0]} alterado para {cargo} com sucesso![/]')
                                sleep(1)
                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)
                        
                        elif editar == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)

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

finally:
    if conexao.is_connected:
        cursor.close()
        conexao.close()
print('Fim do Programa.')
