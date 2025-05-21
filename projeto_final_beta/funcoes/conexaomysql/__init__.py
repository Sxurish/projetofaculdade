
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
    

def procurar_na_tabela_com_condicao_joins(conexao, cursor, retornar_colunas, tabelas, onde_procurar, dado_procurado, joins=None, usar_like=False, operador= '=', comparar_colunas=False, And=None ,descompactar=False):
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


def inserir_registro(conexao, cursor, tabela, colunas, valores):
    colunas_sql = ', '.join(colunas)
    coringas = ', '.join(['%s'] * len(valores))
    print(coringas)
    sql = f"INSERT INTO {tabela} ({colunas_sql}) VALUES ({coringas})"
    cursor.execute(sql, valores)
    conexao.commit()


def atualizar_registro(conexao, cursor, tabela, colunas, valores, onde_procurar, dado_procurado):
    set_sql = ', '.join([f"{coluna} = %s" for coluna in colunas])
    sql = f"UPDATE {tabela} SET {set_sql} WHERE {onde_procurar} = %s"
    cursor.execute(sql, valores + (dado_procurado,))
    conexao.commit()
