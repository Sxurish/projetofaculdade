
def select_tabela(conexao, cursor, tabela, lista_colunas=None):
    if lista_colunas:
        cursor.execute(f"SELECT {', '.join(lista_colunas)} FROM {tabela}")
    else:
        cursor.execute(f"SELECT * FROM {tabela}")
    
    return cursor.fetchall()

def procurar_na_tabela_com_condicao(conexao, cursor, tabela, onde_procurar, dado_procurado, retornar_colunas='', usar_like=False, operador='=', comparar_colunas=False, And=None, descompactar=False):
    if retornar_colunas != '':
        colunas_sql = retornar_colunas
    else:
        colunas_sql = '*'
    if comparar_colunas:
        # Comparação entre colunas, sem parâmetros
        comparar = f"{onde_procurar} {operador} {dado_procurado}"
        if And:
            sql += f" AND {And}"    
        cursor.execute(f"SELECT {colunas_sql} FROM {tabela} WHERE {comparar}")
    else:
        if usar_like:
            condicao_sql = f"{onde_procurar} LIKE %s"
            dado_procurar = (f"%{dado_procurado}%",)
        else:
            condicao_sql = f"{onde_procurar} {operador} %s"
            dado_procurar = (dado_procurado,)  
        cursor.execute(f"SELECT {colunas_sql} FROM {tabela} WHERE {condicao_sql}", (dado_procurar))

    if descompactar:
        return cursor.fetchone()
    else:   
        return cursor.fetchall()
    

def procurar_na_tabela_com_condicao_joins(conexao, cursor, retornar_colunas, tabelas:list, onde_procurar, dado_procurado, joins:list=None, usar_like=False, operador= '=', comparar_colunas=False, And=None ,descompactar=False):
    sql = f"SELECT {retornar_colunas} FROM {tabelas[0]}"

    if joins:
        c = 0
        for join in joins:
            c += 1
            sql += f" JOIN {tabelas[c]} ON {join}"
    if comparar_colunas:
        # Comparação entre colunas, sem parâmetros
        sql += f" WHERE {onde_procurar} {operador} {dado_procurado}"
        if And:
            sql += f" AND {And}"
        cursor.execute(sql)
    else:
        if usar_like:
            sql += f" WHERE {onde_procurar} LIKE %s"
            dado_procurado = (f"%{dado_procurado}%",)
        else:
            sql += f" WHERE {onde_procurar} {operador} %s"
            dado_procurado = (dado_procurado,)
        cursor.execute(sql, dado_procurado)
    if descompactar:
        return cursor.fetchone()
    else:
        return cursor.fetchall()


def inserir_registro(conexao, cursor, tabela, colunas:list, valores:tuple, retornar_id=False):
    colunas_sql = ', '.join(colunas)
    coringas = ', '.join(['%s'] * len(valores))
    sql = f"INSERT INTO {tabela} ({colunas_sql}) VALUES ({coringas})"
    cursor.execute(sql, valores)
    conexao.commit()
    if retornar_id:
        cursor.execute("SELECT LAST_INSERT_ID()")
        ultimo_id = cursor.fetchone()[0]
        return ultimo_id


def atualizar_registro(conexao, cursor, tabela, colunas:list, valores:tuple, onde_procurar, dado_procurado):
    set_sql = ', '.join([f"{coluna} = %s" for coluna in colunas])
    sql = f"UPDATE {tabela} SET {set_sql} WHERE {onde_procurar} = %s"
    cursor.execute(sql, valores + (dado_procurado,))
    conexao.commit()


def cancelar_pedido(conexao, cursor, lista_pedido:list):
    for pedido in lista_pedido:
        #mudar a quantidade! usando o id de referencia.
        qtd_produto = procurar_na_tabela_com_condicao(conexao, cursor, 'tbl_estoque_produtos', 'id_produto', str(pedido['id']), 'qtd_produto',descompactar=True)
        nova_qtd = int(qtd_produto[0]) + pedido['quantidade']
        atualizar_registro(conexao, cursor, 'tbl_estoque_produtos', ['qtd_produto'], (str(nova_qtd),), 'id_produto', str(pedido['id']))


def relatorio_pedidos(conexao, cursor, por_quantidade=False, asc=False, id_produto='0', resultados=5):
    sql = 'select tbl_estoque_produtos.id_produto ,tbl_estoque_produtos.nome_produto, ' \
    'sum(tbl_itens_pedido_estoque_pedido.preco_unitario_item_pedido * tbl_itens_pedido_estoque_pedido.qtd_item_pedido) ' \
    'as total_vendido, ' \
    'sum(tbl_itens_pedido_estoque_pedido.qtd_item_pedido) ' \
    'as quantidade_vendida ' \
    'from tbl_itens_pedido_estoque_pedido join tbl_estoque_produtos ' \
    'on tbl_itens_pedido_estoque_pedido.fk_tbl_estoque_produtos_id_produto = tbl_estoque_produtos.id_produto '
    
    if id_produto != '0':
        sql += f'where tbl_estoque_produtos.id_produto = {id_produto} '

    sql += 'group by tbl_estoque_produtos.id_produto '
    
    if por_quantidade:
        sql += 'order by quantidade_vendida '
    else:
        sql += 'order by total_vendido '
    if asc:
        sql += 'asc '
    else:
        sql += 'desc '
    sql += f'limit {resultados};'

    cursor.execute(sql)
    return cursor.fetchall()
    