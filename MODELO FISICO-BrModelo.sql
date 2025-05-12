CREATE DATABASE projeto_final_bd;
USE projeto_final_bd;

CREATE TABLE tbl_estoque_produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR (100) NOT NULL,
    desc_produto VARCHAR (100),
    qtd_produto INT NOT NULL,
    valor_produto DECIMAL (10,2) NOT NULL,
    qtd_minima_produto INT NOT NULL,
    fk_tbl_categorias_id_categoria INT
);

CREATE TABLE tbl_pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    data_pedido DATE NOT NULL,
    valor_pedido DECIMAL (10,2) NOT NULL,
    fk_tbl_clientes_id_cliente INT
);

CREATE TABLE tbl_clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR (100) NOT NULL,
    cpf_cliente VARCHAR (14) UNIQUE NOT NULL,
    rua VARCHAR (100),
    num_casa INT,
    bairro VARCHAR (100),
    cidade VARCHAR (100),
    estado VARCHAR (2),
    email_cliente VARCHAR (100) NOT NULL,
    telefone_cliente VARCHAR (20) NOT NULL,
    senha_cliente VARCHAR (20) NOT NULL
);

CREATE TABLE tbl_categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR (100) NOT NULL
);

CREATE TABLE tbl_adms (
    id_adm INT AUTO_INCREMENT PRIMARY KEY,
    nome_adm VARCHAR (20) NOT NULL,
    senha_adm VARCHAR (20) NOT NULL
);

CREATE TABLE tbl_itens_venda_estoque_pedido (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    qtd_item_venda INT NOT NULL,
    preco_unitario_item DECIMAL (10,2) NOT NULL,
    fk_tbl_estoque_produtos_id_produto INT,
    fk_tbl_pedidos_id_pedido INT
);
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_2
    FOREIGN KEY (fk_tbl_categorias_id_categoria)
    REFERENCES tbl_categorias (id_categoria)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_pedidos ADD CONSTRAINT FK_tbl_pedidos_2
    FOREIGN KEY (fk_tbl_clientes_id_cliente)
    REFERENCES tbl_clientes (id_cliente)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_itens_venda_estoque_pedido ADD CONSTRAINT FK_tbl_itens_venda_estoque_pedido_2
    FOREIGN KEY (fk_tbl_estoque_produtos_id_produto)
    REFERENCES tbl_estoque_produtos (id_produto);
 
ALTER TABLE tbl_itens_venda_estoque_pedido ADD CONSTRAINT FK_tbl_itens_venda_estoque_pedido_3
    FOREIGN KEY (fk_tbl_pedidos_id_pedido)
    REFERENCES tbl_pedidos (id_pedido);