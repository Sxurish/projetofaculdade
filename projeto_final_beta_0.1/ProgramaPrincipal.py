import mysql.connector #instale a biblioteca: mysql-connector-python
import re
from funcoes.conexaomysql import *
from funcoes.formatacao import *
from funcoes.validacao import *
from rich import print as rprint #instale a biblioteca: rich
from datetime import date
from time import sleep
#para instalar a biblioteca vá no terminal e digite: pip intall e o nome da biblioteca
cliente = False
funcionario = True
acesso_gestor = True
id_cliente = 0
nome_cliente = ''
id_funcionario = 0
nome_funcionario = ''

try:
    conexao = mysql.connector.connect(
        host='localhost', #isso não muda se o banco de dados, já está no seu pc.
        user='root', #altere o usuario se o seu for diferente.
        password='22222121', #altere a senha se a sua for diferente.
        database='projeto_final_bd' #confira se o banco de dados já está na seu mysql.
    )
    cursor = conexao.cursor()

    while True:
        mensagem('DARCAN - MATERIAIS DE CONSTRUÇÃO', cor='[cyan]')
        rprint('Menu:' \
        '\n[ 1 ] - Login' \
        '\n[ 2 ] - Consultar Produto' \
        '\n[ 3 ] - Fazer Pedido')
        if funcionario == True:
            rprint('[ 4 ] - Estoque' \
            '\n[ 5 ] - Relatório de Vendas')
            if acesso_gestor == True:
                rprint('[ 6 ] - Cadastros')
        rprint('[red][ 0 ][/] - Sair do Programa')
        menu = inputint('Opção: ')

        if menu == 1: #Login
            retorna_menu = id_cliente
            while True:
                if retorna_menu != id_cliente:
                    break
                mensagem('LOGIN', cor='[gold1]')
                print('menu:' \
                '\n[ 1 ] - Cliente' \
                '\n[ 2 ] - Funcionario' \
                '\n[ 0 ] - Voltar')
                login = inputint('Opção: ')

                if login == 1: #Cliente
                    while True:
                        mensagem('Login Cliente', cor='[gold1]')
                        print('menu:'
                        '\n[ 1 ] - Fazer o login' \
                        '\n[ 2 ] - Fazer o cadastro' \
                        '\n[ 0 ] - Voltar')
                        menu_cliente = inputint('Opção: ')

                        if menu_cliente == 1: #Login
                            mensagem('Faça o seu Login de Cliente!', cor='[gold1]')
                            cpf_cliente = inputstr('Digite o seu cpf(com o ponto e traço): ').strip()#valida o cpf aqui?
                            senha_cliente = inputstr('Digite sua senha: ').strip()
                            nome = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', cpf_cliente, 'nome_cliente', descompactar=True)
                            if nome:
                                senha = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', cpf_cliente,                   'senha_cliente', descompactar=True)[0]
                                if senha_cliente == senha:
                                    id_login = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', cpf_cliente, 'id_cliente', descompactar=True)[0]
                                    id_cliente = id_login 
                                    nome_cliente = nome[0]
                                    cliente = True
                                    funcionario = False                               
                                    acesso_gestor = False
                                    rprint('[green]Login como cliente realizado com sucesso![/]')
                                    sleep(1)
                                    rprint(f'[green]Seja bem vindo(a), {nome_cliente}![/]')
                                    sleep(1)
                                    break
                                else:
                                    rprint('[bold red]login e/ou senha incorretos![/]')
                            else:
                                rprint('[bold red]Login e/ou senha incorretos![/]')
                            
                        elif menu_cliente == 2: #Cadastro
                            mensagem('Faça o seu Cadastro!', cor='[gold1]')
                            novo_nome = inputstr('Digite o seu Nome(Somente Nome e Sobrenome): ').strip()
                            def validar_cpf(cpf):
                                return re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}',cpf)
                            while True:
                                novo_cpf = inputstr('Digite o seu CPF(com ponto e traço): ').strip() #Fazer a validação do CPF depois.
                                if validar_cpf(novo_cpf):
                                    break
                                else:
                                    rprint('[bold red]Incorreto! Tente XXX.XXX.XXX-XX[/]')
                                    continue
                            #Verifica se o CPF já existe
                            cpf_existente = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', novo_cpf)
                            if cpf_existente:
                                rprint('[bold red]CPF já cadastrado![/]')
                                sleep(1)
                                continue
                            def validar_telefone(telefone):
                                return re.fullmatch(r"\(\d{2}\)\d{5}-\d{4}", telefone)
                            while True:
                                novo_telefone = inputstr('Digite o seu Telefone (com o DDD): ').strip() #Fazer a validação do telefone depois.
                                if validar_telefone(novo_telefone):
                                    break
                                else:
                                    rprint('[bold red]Incorreto! Tente (XX)XXXXX-XXXX[/]')
                            novo_email = inputstr('Digite o seu E-mail: ').strip() #Validar o e-mail talvez.
                            #SP, Taboão da Serra, Rua das Palmeiras, 27 = Modelo de endereço.
                            estado = inputstr('Digite a UF do seu Estado: ').strip()#Validar o Estado!
                            municipio = inputstr('Digito o nome do seu Município: ').strip()#Validar o Municipio?
                            rua = inputstr('Digite o nome da sua rua: ').strip()#Validar a Rua?
                            numero = inputstr('Digite o número da casa ou prédio: ').strip()#Validar o numero!
                            endereco = ', '.join([estado, municipio, rua, str(numero)])
                            while True:
                                nova_senha = inputstr('Digite a sua senha: ').strip() #Fazer a validação da senha depois.
                                if len(nova_senha) < 6:
                                    rprint('[bold red]A senha deve ter no mínimo 6 caracteres![/]')
                                    sleep(1)
                                    continue
                                elif len(nova_senha) > 20:
                                    rprint('[bold red]A senha deve ter no máximo 20 caracteres![/]')
                                    sleep(1)
                                    continue
                                confirmar_senha = inputstr('Digite a senha novamente: ').strip()
                                if nova_senha == confirmar_senha:
                                    break
                                rprint('[bold red]Senhas Diferentes. Tente novamente.[/]')

                            dados_cliente = [novo_nome, novo_cpf, novo_telefone, novo_email, nova_senha, endereco]
                            mostrar_dados(dados_cliente, 'Seus Dados', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')
                            sleep(1)
                            confirmar = inputint(f'Os seus dados estão corretos? Fazer o cadastro?[1 - Sim / 2 - Não]: ')
                            if confirmar == 1:
                                inserir_registro(conexao, cursor, 'tbl_clientes', 
                                                 colunas=['nome_cliente', 'cpf_cliente', 'telefone_cliente', 'email_cliente', 'senha_cliente', 'endereco_cliente'], 
                                                 valores=(dados_cliente[0], dados_cliente[1], dados_cliente[2], dados_cliente[3], dados_cliente[4], dados_cliente[5]))
                                rprint(f'[green]Cliente {nome_cliente} registrado(a) com sucesso![/]')
                                sleep(1)

                            else:
                                rprint('[bold red]Operação cancelada![/]')
                                sleep(1)

                        elif menu_cliente == 0:
                            print('Voltando ao menu de login...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
              
                elif login == 2: #Funcionário
                    mensagem('Faça o seu Login de Funcionário!', cor='[gold1]')
                    login_func = inputstr('Digite o seu login: ').strip()
                    senha_func = inputstr('Digite sua senha: ').strip()
                    nome = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', login_func, 'nome_funcionario', descompactar=True)
                    if nome:
                        senha = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', login_func,                   'senha_funcionario', descompactar=True)[0]
                        if senha_func == senha:
                            id_login = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', login_func, 'id_funcionario', descompactar=True)[0]
                            id_funcionario = id_login
                            nome_funcionario = nome[0]
                            cliente = False
                            funcionario = True
                            acesso = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', login_func,
                            'acesso_gestor', descompactar=True)[0]
                            if acesso == 1:
                                acesso_gestor = True
                            else:
                                acesso_gestor = False
                            rprint('[green]Login como funcionário realizado com sucesso![/]')
                            sleep(1)
                            rprint(f'[green]Seja bem vindo(a), {nome_funcionario}![/]')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]login e/ou senha incorretos![/]')
                    else:
                        rprint('[bold red]Login e/ou senha incorretos![/]')
                                          
                elif login == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)

        elif menu == 2: #Consultar Produto
            while True:
                mensagem('CONSULTAR PRODUTO', cor='[dark_green]')
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
                    sleep(2)

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
                    sleep(2)

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
                adc_pedido = {} 
                lista_pedido = []
                id_produtos = []
                quant_produtos = []

                while True:
                    mensagem('FAÇA SEU PEDIDO!', cor='[green]')
                    print('menu:' \
                    '\n[ 1 ] - Pesquisar Produto' \
                    '\n[ 2 ] - Adicionar ao Pedido')
                    if lista_pedido != []:
                        print('[ 3 ] - Ver o pedido' \
                        '\n[ 4 ] - Cancelar Pedido' \
                        '\n[ 5 ] - Fechar Pedido')
                    elif lista_pedido == []:
                        print('[ 0 ] - Voltar')
                    pedido_opc = inputint('Opção: ')

                    if pedido_opc == 1: #Pesquisar Produto
                        while True:
                            mensagem('Pesquisar Produto', cor='[green]')
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
                                sleep(2)

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
                                sleep(2)

                            elif consultar == 0:
                                print('Voltando ao menu de pedido...')
                                sleep(1)
                                break
                            else:
                                rprint('[bold red]Opção Inválida![/]')
                                sleep(1)

                    elif pedido_opc == 2: #Adicionar ao Pedido
                        id_produto = inputint('Digite o ID do Produto: ')
                        result_pesquisa = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.valor_produto', ['tbl_estoque_produtos', 'tbl_categorias'], 'tbl_estoque_produtos.id_produto',
                        str(id_produto), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria'])
                        if not result_pesquisa:
                                rprint('[bold red]Produto não encontrado![/]')
                                sleep(1)
                                continue
                        nome_produto = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'nome_produto', descompactar=True)
                        valor_produto = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'valor_produto', descompactar=True)
                        mostrar_tabela(result_pesquisa, 'Produto', 'ID', 'Nome', 'Descrição', 'Quantidade', 'Valor')
                        qtd_produto = inputint('Digite a quantidade do produto você deseja levar: ')
                        confirmar = inputint(f'Deseja adicionar {qtd_produto} unidades do produto {nome_produto[0]} ao seu pedido? [1 - Sim / 2 - Não]: ')
                        if confirmar == 1:
                            qtd_atual = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(id_produto), 'qtd_produto', descompactar=True)
                            nova_qtd = int(*qtd_atual) - qtd_produto
                            if nova_qtd <= 0:
                                rprint('[bold red]Quantidade inválida![/]')
                                sleep(1)
                                continue
                            atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['qtd_produto'] , (str(nova_qtd),), 'id_produto', str(id_produto))
                            adc_pedido['id'] = id_produto
                            adc_pedido['nome'] = nome_produto[0]
                            adc_pedido['quantidade'] = qtd_produto
                            adc_pedido['valor'] = float(valor_produto[0])
                            lista_pedido.append(adc_pedido.copy())
                            rprint(f'[green]{nome_produto[0]} adicionado ao pedido com sucesso![/]')  
                            sleep(1) 
                        else:
                            rprint(f'[bold red]Operação Cancelada![/]')
                            sleep(1)
                        
                    elif pedido_opc == 3 and lista_pedido != []: #Mostrar Pedido
                        mostrar_pedido(lista_pedido, 'Seu Pedido', 'No', 'Nome do Produto', 'Quantidade', 'Valor UN', 'Valor Item', 'Valor Total')
                        sleep(2)

                    elif pedido_opc == 4 and lista_pedido != []: #Cancelar Pedido
                        confirmar = inputint(f'Deseja CANCELAR o seu pedido? [1 - Sim / 2 - Não]: ')
                        if confirmar == 1:
                            rprint('[bold red]Cancelando o pedido...[/]')
                            sleep(1)
                            cancelar_pedido(conexao, cursor, lista_pedido)
                            rprint(f'[green]Pedido cancelado com sucesso![/]')  
                            sleep(1)
                        else:
                            rprint(f'[bold red]Operação Cancelada![/]')
                            sleep(1)  
                        break

                    elif pedido_opc == 5 and lista_pedido != []: #Fechar Pedido
                        mostrar_pedido(lista_pedido, 'Seu Pedido', 'No', 'Nome do Produto', 'Quantidade', 'Valor UN', 'Valor Item', 'Valor Total')
                        confirmar = inputint(f'Deseja FINALIZAR o seu pedido? [1 - Sim / 2 - Não]: ')
                        if confirmar == 1:
                            data_atual = str(date.today())
                            valor_total = valortotal(lista_pedido) #Colocar um try except aqui!
                            id_pedido = inserir_registro(conexao, cursor, 'tbl_pedidos', 
                                             colunas=['data_pedido', 'valor_pedido', 'fk_tbl_clientes_id_cliente'], 
                                             valores=(str(data_atual), str(valor_total), str(id_cliente)),
                                             retornar_id=True)
                            for pedido in lista_pedido:
                                inserir_registro(conexao, cursor, 'tbl_itens_pedido_estoque_pedido',
                                                colunas=['qtd_item_pedido', 'preco_unitario_item_pedido', 'fk_tbl_estoque_produtos_id_produto', 'fk_tbl_pedidos_id_pedido'],
                                                valores=(str(pedido['quantidade']), str(pedido['valor']), str(pedido['id']), str(id_pedido)))
                            rprint(f'[green]Pedido feito com sucesso!' \
                                   f'\nNúmero do pedido: {id_pedido}[/]')
                            sleep(2)
                            break
                        else:
                            rprint(f'[bold red]Operação Cancelada![/]')
                            sleep(1)  

                    elif pedido_opc == 0 and lista_pedido == []:
                        print('Voltando ao menu...')
                        sleep(1)
                        break
                    else:
                        rprint('[bold red]Opção Inválida![/]')
                        sleep(1)
                
        elif menu == 4 and funcionario: #Estoque
            while True:
                mensagem('ESTOQUE', cor='[red]')
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
                        mensagem('PESQUISAR PRODUTO', cor='[red]')
                        print('menu:' \
                        '\n[ 1 ] - Por Nome' \
                        '\n[ 2 ] - Por Categoria' \
                        '\n[ 3 ] - Por ID do Produto' \
                        '\n[ 0 ] - Voltar')
                        pesquisar = inputint('Opção: ')
                        
                        if pesquisar == 1: #Por Nome
                            nome_produto = input('Digite o nome do Produto: ').strip()
                            produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor, retornar_colunas='tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias', 'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.nome_produto', dado_procurado=nome_produto, joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'], usar_like=True)
                            if not produto_procurado:
                                rprint('[bold red]Produto não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                            sleep(2)

                        elif pesquisar == 2: #Por Categoria
                            categorias = select_tabela(conexao, cursor, 'tbl_categorias')
                            mostrar_tabela(categorias, 'Categorias', 'ID', 'Nome')
                            categ = inputint('ID da Categoria: ')
                            nome_categoria = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_categorias', 'id_categoria', categ, 'nome_categoria',
                                                                         descompactar=True)
                            if not nome_categoria:
                                rprint('[bold red]Categoria não encontrada![/]')
                                sleep(1)
                                continue
                            result_categ = procurar_na_tabela_com_condicao_joins(conexao, cursor,
                            retornar_colunas='tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], onde_procurar='tbl_categorias.id_categoria', dado_procurado=str(categ), joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                            mostrar_tabela(result_categ, *nome_categoria, 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                            sleep(2)

                        elif pesquisar == 3: #Por ID do Produto
                            id_produto = inputint('ID do Produto: ')
                            produto_procurado = procurar_na_tabela_com_condicao_joins(conexao, cursor,
                            retornar_colunas='tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', 
                            tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], 
                            onde_procurar='tbl_estoque_produtos.id_produto', dado_procurado=str(id_produto), 
                            joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                            if not produto_procurado:
                                rprint('[bold red]Produto não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(produto_procurado, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                            sleep(2)

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
                   sleep(2)

                elif estoque == 3: #Produtos com Estoque Zerado
                    est_zero = procurar_na_tabela_com_condicao_joins(conexao, cursor, 
                        'tbl_estoque_produtos.id_produto, tbl_estoque_produtos.nome_produto, tbl_estoque_produtos.desc_produto,  tbl_categorias.nome_categoria, tbl_estoque_produtos.qtd_produto, tbl_estoque_produtos.qtd_minima_produto, tbl_estoque_produtos.valor_produto, tbl_funcionarios.nome_funcionario', tabelas=['tbl_estoque_produtos', 'tbl_categorias',   'tbl_funcionarios'], onde_procurar='tbl_estoque_produtos.qtd_produto', dado_procurado=0, joins=['tbl_estoque_produtos.fk_tbl_categorias_id_categoria = tbl_categorias.id_categoria', 'tbl_estoque_produtos.fk_tbl_funcionarios_id_funcionario = tbl_funcionarios.id_funcionario'])
                    if not est_zero:
                        rprint('[bold red]Não há produtos com estoque zerado![/]')
                        sleep(1)
                        continue
                    mostrar_tabela(est_zero, 'Produto', 'ID', 'Nome', 'Descrição', 'Categoria', 'Quantidade', 'Quantidade Mínima', 'Valor', 'Editado por', moeda=-2)
                    sleep(2)

                elif estoque == 4: #Lançar Entrada de Produto
                    while True:
                        mensagem('LANÇAR ENTRADA DE PRODUTO', cor='[red]')
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
                        sleep(1)
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
                        mensagem('LANÇAR QUEBRA OU PERDA DE PRODUTO', cor='[red]')
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
                        sleep(1)
                        qtd_produto = inputint('Quantidade a ser retirada: ')
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

                elif estoque == 6: #Editar Dados do Produto 
                    while True:
                        mensagem('EDITAR DADOS DO PRODUTO', cor='[red]')
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
                        sleep(1)
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
                        mensagem('ADICIONAR NOVO PRODUTO', cor='[red]')
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
                mensagem('RELATÓRIO DE VENDAS', cor='[purple]')
                print('menu:' \
                '\n[ 1 ] - Pesquisar Pedidos' \
                '\n[ 2 ] - Produtos Vendidos' \
                '\n[ 0 ] - Voltar')
                vendas = inputint('Opção: ')

                if vendas == 1: #Pedidos Realizados
                    while True:
                        mensagem('PEDIDOS REALIZADOS', cor='[purple]')
                        print('menu:' \
                        '\n[ 1 ] - Por CPF do Cliente' \
                        '\n[ 2 ] - Por ID do Pedido' \
                        '\n[ 0 ] - Voltar')
                        realizados = inputint('Opção: ')

                        if realizados == 1: #Por Cliente
                            cpf_cliente = inputstr('Digite o CPF do Cliente: ').strip()
                            cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', cpf_cliente)
                            if not cliente_procurado:
                                rprint('[bold red]Cliente não encontrado![/]')
                                sleep(1)
                                continue
                            pedidos_cliente = procurar_na_tabela_com_condicao_joins(conexao, cursor, "tbl_pedidos.id_pedido, tbl_clientes.nome_cliente, date_format(tbl_pedidos.data_pedido, '%d/%m/%Y'), tbl_pedidos.valor_pedido", ['tbl_pedidos', 'tbl_clientes'], 'tbl_clientes.cpf_cliente', cpf_cliente, joins = ['tbl_pedidos.fk_tbl_clientes_id_cliente = tbl_clientes.id_cliente'])

                            if not pedidos_cliente:
                                rprint('[bold red]O Cliente não fez nenhum pedido![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(pedidos_cliente, 'Pedidos Realizados', 'ID Pedido', 'Nome do Cliente', 'Data do Pedido', 'Valor do Pedido')
                            sleep(2)

                        elif realizados == 2:  #Por ID do Pedido
                            id_ped = inputint('Digite o ID do pedido: ')
                            pedido_cliente = procurar_na_tabela_com_condicao_joins(conexao, cursor, "tbl_pedidos.id_pedido, tbl_clientes.nome_cliente, date_format(tbl_pedidos.data_pedido, '%d/%m/%Y'), tbl_pedidos.valor_pedido", ['tbl_pedidos', 'tbl_clientes'], 'tbl_pedidos.id_pedido', str(id_ped), joins = ['tbl_pedidos.fk_tbl_clientes_id_cliente = tbl_clientes.id_cliente'])
                            if not pedido_cliente:
                                rprint('[bold red]Pedido não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(pedido_cliente, 'Resumo do Pedido', 'ID Pedido', 'Nome do Cliente', 'Data do Pedido', 'Valor do Pedido')
                            sleep(1)
                            
                            nota_cliente = procurar_na_tabela_com_condicao_joins(conexao, cursor, 'tbl_estoque_produtos.nome_produto, tbl_itens_pedido_estoque_pedido.qtd_item_pedido, tbl_itens_pedido_estoque_pedido.preco_unitario_item_pedido', [ 'tbl_itens_pedido_estoque_pedido', 'tbl_estoque_produtos', 'tbl_pedidos'], 'tbl_pedidos.id_pedido', str(id_ped), 
                            joins=['tbl_itens_pedido_estoque_pedido.fk_tbl_estoque_produtos_id_produto = tbl_estoque_produtos.id_produto', 'tbl_itens_pedido_estoque_pedido.fk_tbl_pedidos_id_pedido = tbl_pedidos.id_pedido']) 
                            nota_pedido = []
                            linha_pedido = {}
                            for linha in nota_cliente:
                                linha_pedido['nome'] = linha[0]
                                linha_pedido['quantidade'] = linha[1]
                                linha_pedido['valor'] = float(linha[2])
                                nota_pedido.append(linha_pedido.copy())
                            mostrar_pedido(nota_pedido, f'Informações do Pedido Nº{pedido_cliente[0][0]}', 'No', 'Nome do Produto', 'Quantidade', 'Valor UN', 'Valor Item', 'Valor Total')
                            sleep(2)

                        elif realizados == 0:
                            print('Voltando ao relatório de vendas...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                
                elif vendas == 2: #Produtos Vendidos
                    while True:
                        mensagem('PRODUTOS VENDIDOS', cor='[purple]')
                        print('menu:' \
                        '\n[ 1 ] - Por Quantidade' \
                        '\n[ 2 ] - Por Valor' \
                        '\n[ 3 ] - Por ID do Produto' \
                        '\n[ 0 ] - Voltar')
                        prodvend = inputint('Opção: ')
                        
                        if prodvend == 1: #Por Quantidade
                            mensagem('Por Quantidade', cor='[purple]')
                            print('menu:' \
                            '\n[ 1 ] - 5 Mais Vendidos' \
                            '\n[ 2 ] - 5 Menos Vendidos' \
                            '\n[ 0 ] - Voltar')
                            prodquant = inputint('Opção: ')
                            
                            if prodquant == 1:
                                mais_vend = relatorio_pedidos(conexao, cursor, por_quantidade=True)
                                mostrar_tabela(mais_vend, 'Mais Vendidos por Quantidade', 'ID', 'Produto', 'Valor Vendido', 'Quantidade', moeda=-2) 
                                sleep(2)

                            elif prodquant == 2:    
                                menos_vend = relatorio_pedidos(conexao, cursor, por_quantidade=True, asc=True)
                                mostrar_tabela(menos_vend, 'Menos Vendidos por Quantidade', 'ID', 'Produto', 'Valor Vendido', 'Quantidade', moeda=-2) 
                                sleep(2)

                            elif prodquant == 0:
                                print('Voltando ao relatório de vendas...')
                                sleep(1)
                                break
                            else:
                                rprint('[bold red]Opção Inválida![/]')
                                sleep(1)

                        elif prodvend == 2: #Por Valor
                            mensagem('Por Valor', cor='[purple]')
                            print('menu:' \
                            '\n[ 1 ] - 5 Mais Vendidos' \
                            '\n[ 2 ] - 5 Menos Vendidos' \
                            '\n[ 0 ] - Voltar')
                            prodvalor = inputint('Opção: ')

                            if prodvalor == 1:
                                mais_vend = relatorio_pedidos(conexao, cursor)
                                mostrar_tabela(mais_vend, 'Mais Vendidos por Valor', 'ID', 'Produto', 'Valor Vendido', 'Quantidade', moeda=-2) 
                                sleep(2)
                            
                            elif prodvalor == 2:    
                                menos_vend = relatorio_pedidos(conexao, cursor, asc=True)
                                mostrar_tabela(menos_vend, 'Menos Vendidos por Valor', 'ID', 'Produto', 'Valor Vendido', 'Quantidade', moeda=-2) 
                                sleep(2)

                            elif prodvalor == 0:
                                print('Voltando ao relatório de vendas...')
                                sleep(1)
                                break
                            else:
                                rprint('[bold red]Opção Inválida![/]')
                                sleep(1)

                        elif prodvend == 3: #Por ID do Produto
                            id_produto = inputint('ID do Produto: ')
                            produto_vendas = relatorio_pedidos(conexao, cursor, id_produto=str(id_produto))
                            if not produto_vendas:
                                rprint('[bold red]Produto não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(produto_vendas, 'Relatório do Produto', 'ID', 'Produto', 'Valor Vendido', 'Quantidade', moeda=-2) 
                            sleep(2)

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
                mensagem('CADASTRADOS', cor='[cornflower_blue]')
                print('menu: ' \
                '\n[ 1 ] - Pesquisar Clientes' \
                '\n[ 2 ] - Editar Dados de Cliente' \
                '\n[ 3 ] - Pesquisar Funcionários' \
                '\n[ 4 ] - Editar Dados de Funcionário' \
                '\n[ 5 ] - Cadastrar Funcionário' \
                '\n[ 0 ] - Voltar')
                cadastro = inputint('Opção: ')
                
                if cadastro == 1: #Mostrar os clientes cadastrados
                    while True:
                        mensagem('PESQUISAR CLIENTE', cor='[cornflower_blue]')
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
                            sleep(1)

                        elif pesquisar == 2: #Por CPF
                            cpf_cliente = input('Digite o CPF do Cliente: ').strip()
                            cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'cpf_cliente', cpf_cliente)
                            if not cliente_procurado:
                                rprint('[bold red]Cliente não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(cliente_procurado, 'Cliente', 'ID', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')
                            sleep(1)

                        elif pesquisar == 3: #Por ID do Cliente
                            id_cliente = inputint('ID do Cliente: ')
                            cliente_procurado = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_clientes', 'id_cliente', str(id_cliente))
                            if not cliente_procurado:
                                rprint('[bold red]Cliente não encontrado![/]')
                                sleep(1)
                                continue
                            mostrar_tabela(cliente_procurado, 'Cliente', 'ID', 'Nome', 'CPF', 'Telefone', 'E-mail', 'Senha', 'Endereço')
                            sleep(1)

                        elif pesquisar == 0:
                            print('Voltando ao cadastro...')
                            sleep(1)
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                    
                elif cadastro == 2: #Editar os dados do cliente
                    while True:
                        mensagem('EDITAR DADOS DO CLIENTE', cor='[cornflower_blue]')
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
                        sleep(1)
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
                        mensagem('PESQUISAR FUNCIONÁRIO', cor='[cornflower_blue]')
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
                            sleep(1)
                        
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
                        mensagem('EDITAR DADOS DO FUNCIONÁRIO', cor='[cornflower_blue]')
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
                        sleep(1)
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

                elif cadastro == 5: #Cadastro de funcionario
                    mensagem('Cadastro de Funcionário', cor='[cornflower_blue]')
                    novo_nome = inputstr('Digite o Nome do Funcionário(Somente Nome e Sobrenome): ').strip()
                    novo_login = inputstr('Digite o seu Login: ').strip() #Fazer a validação de Login?
                    #Verifica se o login já existe
                    login_existente = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_funcionarios', 'login_funcionario', novo_login)
                    if login_existente:
                        rprint('[bold red]Login já cadastrado![/]')
                        sleep(1)
                        continue
                    while True:
                        nova_senha = inputstr('Digite a sua senha: ').strip() #Fazer a validação da senha depois.
                        if len(nova_senha) < 6:
                            rprint('[bold red]A senha deve ter no mínimo 6 caracteres![/]')
                            sleep(1)
                            continue
                        elif len(nova_senha) > 20:
                            rprint('[bold red]A senha deve ter no máximo 20 caracteres![/]')
                            sleep(1)
                            continue
                        confirmar_senha = inputstr('Digite a senha novamente: ').strip()
                        if nova_senha == confirmar_senha:
                            break
                        rprint('[bold red]Senhas Diferentes. Tente novamente.[/]')
                    while True:
                        nivel_acesso = inputint('Seu Nivel de Acesso [0 - Funcionario / 1 - Gestor]: ')
                        if nivel_acesso == 0:
                            nivel_acesso = '0'
                            break
                        elif nivel_acesso == 1:
                            nivel_acesso = '1'
                            break
                        else:
                            rprint('[bold red]Opção Inválida![/]')
                            sleep(1)
                            
                    dados_func = [novo_nome, nova_senha, nivel_acesso, novo_login]
                    mostrar_dados(dados_func, 'Dados Funcionário', 'Nome', 'Senha', 'Nível de Acesso', 'Login')
                    sleep(1)
                    confirmar = inputint(f'Os dados estão corretos? Fazer o cadastro?[1 - Sim / 2 - Não]: ')
                    if confirmar == 1:
                        inserir_registro(conexao, cursor, 'tbl_funcionarios', 
                                            colunas=['nome_funcionario', 'senha_funcionario', 'acesso_gestor', 'login_funcionario'], 
                                            valores=(dados_func[0], dados_func[1], dados_func[2], dados_func[3]))
                        rprint(f'[green]Funcionário {novo_nome} registrado(a) com sucesso![/]')
                        sleep(1)

                    else:
                        rprint('[bold red]Operação cancelada![/]')
                        sleep(1)

                elif cadastro == 0:
                    print('Voltando ao menu...')
                    sleep(1)
                    break
                else:
                    rprint('[bold red]Opção Inválida![/]')
                    sleep(1)

        elif menu == 0:
            mensagem('OBRIGADO! VOLTE SEMPRE!', cor='[green]')
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
