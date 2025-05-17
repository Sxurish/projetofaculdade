-- Criação do banco de dados
CREATE DATABASE projeto_final_bd;
USE projeto_final_bd;

-- Tabela de estoque dos produtos
CREATE TABLE tbl_estoque_produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR (100) NOT NULL,
    desc_produto VARCHAR (100),
    qtd_produto INT NOT NULL,
    valor_produto DECIMAL (10,2) NOT NULL,
    qtd_minima_produto INT NOT NULL,
    fk_tbl_categorias_id_categoria INT,
    fk_tbl_funcionarios_id_funcionario INT
);

-- Tabela de pedidos
CREATE TABLE tbl_pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    data_pedido DATE NOT NULL,
    valor_pedido DECIMAL (10,2) NOT NULL,
    fk_tbl_clientes_id_cliente INT
);

-- Tabela de clientes
CREATE TABLE tbl_clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR (100) NOT NULL,
    cpf_cliente VARCHAR (14) UNIQUE NOT NULL,
    telefone_cliente VARCHAR (20) NOT NULL,
    email_cliente VARCHAR (100) NOT NULL,
    senha_cliente VARCHAR (20) NOT NULL,
    endereco_cliente VARCHAR (150) NOT NULL
);

-- Tabela de categorias
CREATE TABLE tbl_categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR (100) NOT NULL
);

-- Tabela de funcionarios
CREATE TABLE tbl_funcionarios (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome_funcionario VARCHAR (20) NOT NULL,
    senha_funcionario VARCHAR (20) NOT NULL,
    acesso_gestor BOOL NOT NULL,
    login_funcionario VARCHAR (100) NOT NULL
);

-- Tabela de itens (pedido)
CREATE TABLE tbl_itens_pedido_estoque_pedido (
    id_item_pedido INT AUTO_INCREMENT PRIMARY KEY,
    qtd_item_pedido INT NOT NULL,
    preco_unitario_item_pedido DECIMAL (10,2) NOT NULL,
    fk_tbl_estoque_produtos_id_produto INT,
    fk_tbl_pedidos_id_pedido INT
);
 
 -- Chaves estrangeiras
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_2
    FOREIGN KEY (fk_tbl_categorias_id_categoria)
    REFERENCES tbl_categorias (id_categoria)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_estoque_produtos ADD CONSTRAINT FK_tbl_estoque_produtos_3
    FOREIGN KEY (fk_tbl_funcionarios_id_funcionario)
    REFERENCES tbl_funcionarios (id_funcionario)
    ON DELETE CASCADE;
 
ALTER TABLE tbl_pedidos ADD CONSTRAINT FK_tbl_pedidos_2
    FOREIGN KEY (fk_tbl_clientes_id_cliente)
    REFERENCES tbl_clientes (id_cliente)
    ON DELETE RESTRICT;
 
ALTER TABLE tbl_itens_pedido_estoque_pedido ADD CONSTRAINT FK_tbl_itens_pedido_estoque_pedido_2
    FOREIGN KEY (fk_tbl_estoque_produtos_id_produto)
    REFERENCES tbl_estoque_produtos (id_produto);
 
ALTER TABLE tbl_itens_pedido_estoque_pedido ADD CONSTRAINT FK_tbl_itens_pedido_estoque_pedido_3
    FOREIGN KEY (fk_tbl_pedidos_id_pedido)
    REFERENCES tbl_pedidos (id_pedido);
   
-- Inserções nas tabelas   
 INSERT INTO tbl_categorias (nome_categoria) VALUES
('Ferramentas'),
('Elétrica'),
('Hidráulica'),
('Tintas'),
('Construção Pesada'),
('Acabamento'),
('Madeiras'),
('Iluminação'),
('Jardinagem'),
('Pisos e Revestimentos');


INSERT INTO tbl_funcionarios (nome_funcionario, senha_funcionario, acesso_gestor, login_funcionario) VALUES
('Carlos Silva', 'senha123', TRUE, 'carlos@lojadarcan.com'),
('Ana Souza', 'senha456', FALSE, 'ana@lojadarcan.com'),
('Bruno Rocha', 'senha789', FALSE, 'bruno@lojadarcan.com'),
('Letícia Lima', 'leticia321', FALSE, 'leticia@lojadarcan.com'),
('Diego Freitas', 'diegof12', FALSE, 'diego@lojadarcan.com'),
('Paula Mendes', 'paula987', TRUE, 'paula@lojadarcan.com'),
('Tiago Santos', 'tsantos22', FALSE, 'tiago@lojadarcan.com'),
('Fernanda Luz', 'fluz111', FALSE, 'fernanda@lojadarcan.com'),
('Julio Reis', 'julioreizao1', FALSE, 'julio@lojadarcan.com'),
('Marina Prado', 'mprado', TRUE, 'marina@lojadarcan.com');


INSERT INTO tbl_clientes (nome_cliente, cpf_cliente, telefone_cliente, email_cliente, senha_cliente, endereco_cliente) VALUES
('João Pereira', '123.456.789-09', '(11) 91234-5678', 'joao@gmail.com', 'joao123', 'SP, Taboão da Serra, Rua das Palmeiras, 27'),
('Maria Oliveira', '987.654.321-00', '(21) 98183-1122', 'maria@email.com', 'maria456', 'RJ, Duque de Caxias, Rua do Sol, 189'),
('Lucas Ferreira', '111.222.333-96', '(31) 99888-7766', 'lucas@email.com', 'lucas321', 'MG, Belo Horizonte, Rua das Acácias, 45'),
('Camila Dias', '456.789.123-68', '(71) 98500-3322', 'camila@gmail.com', 'camila987', 'BA, Salvador, Rua da Luz, 103'),
('Rafael Gomes', '321.654.987-70', '(41) 98700-2233', 'rafael@email.com', 'rafael12', 'PR, Curitiba, Rua dos Ipês, 98'),
('Juliana Costa', '741.852.963-20', '(81) 98811-3344', 'juliana@gmail.com', 'juliana88', 'PE, Recife, Rua das Rosas, 56'),
('Bruno Lima', '852.963.741-15', '(51) 98765-4321', 'bruno@yahoo.com.br', 'bruno789', 'RS, Porto Alegre, Rua das Laranjeiras, 71'),
('Patrícia Nunes', '159.357.486-01', '(85) 99123-4567', 'patricia@email.com', 'pat123', 'CE, Fortaleza, Rua do Mar, 212'),
('Gustavo Moraes', '369.258.147-92', '(62) 99777-0000', 'gustavo@email.com', 'gus001', 'GO, Goiânia, Rua das Oliveiras, 134'),
('Aline Martins', '204.618.357-36', '(48) 99666-1122', 'aline@email.com', 'aline999', 'SC, Florianópolis, Rua do Cedro, 62');


INSERT INTO tbl_estoque_produtos (nome_produto, desc_produto, qtd_produto, valor_produto, qtd_minima_produto, fk_tbl_categorias_id_categoria, fk_tbl_funcionarios_id_funcionario) VALUES
/*1*/ ('Martelo Darcan', 'Martelo de aço com cabo emborrachado', 53, 29.90, 20, 1, 1),
/*2*/('Chave de Fenda Darcan', 'Chave média com ponta imantada', 102, 9.50, 40, 1, 2),
/*3*/('Interruptor Simples Darcan', 'Interruptor 10A branco', 228, 4.80, 90, 2, 3),
/*4*/('Tinta Acrílica Darcan 18L', 'Tinta branca para parede', 0, 159.99, 10, 4, 4),
/*5*/('Cimento Darcan II 50kg', 'Saco de cimento', 112, 42.00, 50, 5, 5),
/*6*/('Torneira de Metal', 'Torneira para pia cozinha', 63, 35.00, 30, 3, 6),
/*7*/('Porcelanato 60x60', 'Piso claro brilhante', 28, 69.90, 40, 10, 7),
/*8*/('Rolo de Pintura Darcan', 'Rolo de lã para tinta acrílica', 18, 18.90, 20, 4, 8),
/*9*/('Luminária LED Darcan', 'Luminária de sobrepor 18W', 41, 45.00, 20, 8, 9),
/*10*/('Caixa d’água Darcan 500L', 'Caixa em polietileno', 8, 320.00, 3, 3, 10);


INSERT INTO tbl_pedidos (data_pedido, valor_pedido, fk_tbl_clientes_id_cliente) VALUES 
('2025-05-01', 84.00, 1),
('2025-05-02', 9.60, 2),
('2025-05-03', 39.40, 3),
('2025-05-04', 115.00, 4),
('2025-05-05', 139.80, 5),
('2025-05-06', 159.99, 6),
('2025-05-07', 37.80, 7),
('2025-05-08', 90.00, 8),
('2025-05-09', 18.90, 9),
('2025-05-10', 640.00, 10);


INSERT INTO tbl_itens_pedido_estoque_pedido (qtd_item_pedido, preco_unitario_item_pedido, fk_tbl_estoque_produtos_id_produto, fk_tbl_pedidos_id_pedido) VALUES 
(2, 42.00, 5, 1), -- 2x Cimento Darcan II 50kg (Pedido 1)
(2, 4.80, 3, 2), -- 2x Interruptor Simples Darcan (Pedido 2)
(1, 29.90, 1, 3), -- 1x Martelo Darcan (Pedido 3)
(1, 9.50, 2, 3), -- 1x Chave de Fenda Darcan (Pedido 3)
(2, 35.00, 6, 4), -- 2x Torneira de Metal (Pedido 4)
(1, 45.00, 9, 4), -- 1x Luminária LED Darcan (Pedido 4)
(2, 69.90, 7, 5), -- 2x Porcelanato 60x60 (Pedido 5)
(1, 159.99, 4, 6), -- 1x Tinta Acrílica Darcan 18L (Pedido 6)
(2, 18.90, 8, 7), -- 2x Rolo de Pintura Darcan (Pedido 7)
(2, 45.00, 9, 8), -- 2x Luminária LED Darcan (Pedido 8)
(1, 18.90, 8, 9), -- 1x Rolo de Pintura Darcan (Pedido 9)
(2, 320.00, 10, 10); -- 2x Caixa d’água Darcan 500L (Pedido 10)
