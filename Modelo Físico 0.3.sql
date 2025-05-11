/* Modelo Lógico 0.2: */
CREATE DATABASE projeto_final_bd;
USE projeto_final_bd;

CREATE TABLE tbl_estoque_produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR (100),
    desc_produto VARCHAR (100),
    qtd_produto INT,
    valor_produto DECIMAL (10,2),
    fk_tbl_clientes_id_cliente INT,
    fk_tbl_categorias_id_categoria INT,
    fk_tbl_adms_id_adm INT
);

CREATE TABLE tbl_vendas (
    id_venda INT PRIMARY KEY,
    data_venda DATE,
    valor_venda DECIMAL (10,2),
    fk_tbl_clientes_id_cliente INT
);

CREATE TABLE tbl_clientes (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR (100),
    cpf_cliente VARCHAR (14) UNIQUE,
    rua VARCHAR (100),
    num_casa INT,
    bairro VARCHAR (100),
    cidade VARCHAR (100),
    estado VARCHAR (2),
    email_cliente VARCHAR (100),
    telefone_cliente VARCHAR (20)
);

CREATE TABLE tbl_itens_venda (
    id_item INT PRIMARY KEY,
    qtd_itens_venda INT,
    preco_unitario_itens_venda DECIMAL (10,2),
    fk_tbl_vendas_id_venda INT
);

CREATE TABLE tbl_categorias (
    id_categoria INT PRIMARY KEY,
    nome_categoria VARCHAR (100),
    desc_categoria VARCHAR (100)
);

CREATE TABLE tbl_adms (
    id_adm INT PRIMARY KEY,
    nome_adm VARCHAR (20),
    senha_adm VARCHAR (20)
);

CREATE TABLE produto_venda (
    fk_tbl_itens_venda_id_item INT,
    fk_tbl_estoque_produtos_id_produto INT
);
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_2
    FOREIGN KEY (fk_tbl_clientes_id_cliente)
    REFERENCES tbl_clientes (id_cliente)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_3
    FOREIGN KEY (fk_tbl_categorias_id_categoria)
    REFERENCES tbl_categorias (id_categoria)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_4
    FOREIGN KEY (fk_tbl_adms_id_adm)
    REFERENCES tbl_adms (id_adm)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_vendas ADD CONSTRAINT FK_tbl_vendas_2
    FOREIGN KEY (fk_tbl_clientes_id_cliente)
    REFERENCES tbl_clientes (id_cliente)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_itens_venda ADD CONSTRAINT FK_tbl_itens_venda_2
    FOREIGN KEY (fk_tbl_vendas_id_venda)
    REFERENCES tbl_vendas (id_venda)
    ON DELETE RESTRICT;
 
ALTER TABLE produto_venda ADD CONSTRAINT FK_produto_venda_1
    FOREIGN KEY (fk_tbl_itens_venda_id_item)
    REFERENCES tbl_itens_venda (id_item)
    ON DELETE RESTRICT;
 
ALTER TABLE produto_venda ADD CONSTRAINT FK_produto_venda_2
    FOREIGN KEY (fk_tbl_estoque_produtos_id_produto)
    REFERENCES tbl_estoque_produtos (id_produto)
    ON DELETE RESTRICT;/* Modelo Lógico 0.3: */

CREATE DATABASE projeto_final_bd;
USE projeto_final_bd;

CREATE TABLE tbl_estoque_produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR (100),
    desc_produto VARCHAR (100),
    qtd_produto INT,
    valor_produto DECIMAL (10,2),
    fk_tbl_clientes_id_cliente INT,
    fk_tbl_categorias_id_categoria INT,
    fk_tbl_adms_id_adm INT
);

CREATE TABLE tbl_vendas (
    id_venda INT PRIMARY KEY,
    data_venda DATE,
    valor_venda DECIMAL (10,2),
    fk_tbl_clientes_id_cliente INT
);

CREATE TABLE tbl_clientes (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR (100),
    cpf_cliente VARCHAR (14) UNIQUE,
    rua VARCHAR (100),
    num_casa INT,
    bairro VARCHAR (100),
    cidade VARCHAR (100),
    estado VARCHAR (2),
    email_cliente VARCHAR (100),
    telefone_cliente VARCHAR (20),
    senha_cliente VARCHAR (100)
);

CREATE TABLE tbl_itens_venda (
    id_item INT PRIMARY KEY,
    qtd_itens_venda INT,
    preco_unitario_itens_venda DECIMAL (10,2),
    fk_tbl_vendas_id_venda INT
);

CREATE TABLE tbl_categorias (
    id_categoria INT PRIMARY KEY,
    nome_categoria VARCHAR (100),
    desc_categoria VARCHAR (100)
);

CREATE TABLE tbl_adms (
    id_adm INT PRIMARY KEY,
    nome_adm VARCHAR (20),
    senha_adm VARCHAR (20)
);

CREATE TABLE produto_venda (
    fk_tbl_itens_venda_id_item INT,
    fk_tbl_estoque_produtos_id_produto INT
);
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_2
    FOREIGN KEY (fk_tbl_clientes_id_cliente)
    REFERENCES tbl_clientes (id_cliente)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_3
    FOREIGN KEY (fk_tbl_categorias_id_categoria)
    REFERENCES tbl_categorias (id_categoria)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_4
    FOREIGN KEY (fk_tbl_adms_id_adm)
    REFERENCES tbl_adms (id_adm)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_vendas ADD CONSTRAINT FK_tbl_vendas_2
    FOREIGN KEY (fk_tbl_clientes_id_cliente)
    REFERENCES tbl_clientes (id_cliente)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_itens_venda ADD CONSTRAINT FK_tbl_itens_venda_2
    FOREIGN KEY (fk_tbl_vendas_id_venda)
    REFERENCES tbl_vendas (id_venda)
    ON DELETE RESTRICT;
 
ALTER TABLE produto_venda ADD CONSTRAINT FK_produto_venda_1
    FOREIGN KEY (fk_tbl_itens_venda_id_item)
    REFERENCES tbl_itens_venda (id_item)
    ON DELETE RESTRICT;
 
ALTER TABLE produto_venda ADD CONSTRAINT FK_produto_venda_2
    FOREIGN KEY (fk_tbl_estoque_produtos_id_produto)
    REFERENCES tbl_estoque_produtos (id_produto)
    ON DELETE RESTRICT;