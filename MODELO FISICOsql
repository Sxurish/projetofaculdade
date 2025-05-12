CREATE DATABASE  IF NOT EXISTS `projeto_final_bd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projeto_final_bd`;
-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: localhost    Database: projeto_final_bd
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_adms`
--

DROP TABLE IF EXISTS `tbl_adms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_adms` (
  `id_adm` int NOT NULL AUTO_INCREMENT,
  `nome_adm` varchar(20) NOT NULL,
  `senha_adm` varchar(20) NOT NULL,
  PRIMARY KEY (`id_adm`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_adms`
--

LOCK TABLES `tbl_adms` WRITE;
/*!40000 ALTER TABLE `tbl_adms` DISABLE KEYS */;
INSERT INTO `tbl_adms` VALUES (1,'admin','senha123');
/*!40000 ALTER TABLE `tbl_adms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_categorias`
--

DROP TABLE IF EXISTS `tbl_categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_categorias` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nome_categoria` varchar(100) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_categorias`
--

LOCK TABLES `tbl_categorias` WRITE;
/*!40000 ALTER TABLE `tbl_categorias` DISABLE KEYS */;
INSERT INTO `tbl_categorias` VALUES (1,'Cimento e Argamassas'),(2,'Tijolos e Blocos'),(3,'Revestimentos'),(4,'Pisos'),(5,'Hidráulica'),(6,'Elétrica'),(7,'Ferramentas'),(8,'Tintas e Acessórios');
/*!40000 ALTER TABLE `tbl_categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_clientes`
--

DROP TABLE IF EXISTS `tbl_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome_cliente` varchar(100) NOT NULL,
  `cpf_cliente` varchar(14) NOT NULL,
  `rua` varchar(100) DEFAULT NULL,
  `num_casa` int DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `email_cliente` varchar(100) NOT NULL,
  `telefone_cliente` varchar(20) NOT NULL,
  `senha_cliente` varchar(20) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `cpf_cliente` (`cpf_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_clientes`
--

LOCK TABLES `tbl_clientes` WRITE;
/*!40000 ALTER TABLE `tbl_clientes` DISABLE KEYS */;
INSERT INTO `tbl_clientes` VALUES (1,'João Silva','123.456.789-01','Rua das Flores',123,'Jardim Primavera','Taboão da Serra','SP','joao.silva@email.com','(11) 99999-8888','senha123'),(2,'Maria Souza','987.654.321-02','Avenida Brasil',456,'Centro','São Paulo','SP','maria.souza@email.com','(11) 88888-7777','senha456'),(3,'Carlos Oliveira','111.222.333-03','Rua das Palmeiras',789,'Vila Nova','Embu das Artes','SP','carlos.oliveira@email.com','(11) 77777-6666','senha789'),(4,'Ana Pereira','444.555.666-04','Travessa da Amizade',101,'Parque Pinheiros','Itapecerica da Serra','SP','ana.pereira@email.com','(11) 66666-5555','senha012'),(5,'Ricardo Santos','777.888.999-05','Alameda dos Pássaros',222,'Jardim Europa','Cotia','SP','ricardo.santos@email.com','(11) 55555-4444','senha345'),(6,'Fernanda Lima','222.333.444-06','Rua da Paz',333,'Jardim das Oliveiras','Osasco','SP','fernanda.lima@email.com','(11) 44444-3333','senha678'),(7,'Pedro Rodrigues','555.666.777-07','Avenida São Paulo',444,'Bela Vista','Barueri','SP','pedro.rodrigues@email.com','(11) 33333-2222','senha901'),(8,'Camila Gomes','888.999.000-08','Rua das Acácias',555,'Jardim Santo Antônio','Carapicuíba','SP','camila.gomes@email.com','(11) 22222-1111','senha234'),(9,'Lucas Costa','333.444.555-09','Travessa das Rosas',666,'Vila Dirce','Itapevi','SP','lucas.costa@email.com','(11) 11111-0000','senha567'),(10,'Mariana Oliveira','666.777.888-10','Alameda das Flores',777,'Jardim Bela Vista','Embú-Guaçu','SP','mariana.oliveira@email.com','(11) 98765-4321','senha890');
/*!40000 ALTER TABLE `tbl_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_estoque_produtos`
--

DROP TABLE IF EXISTS `tbl_estoque_produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_estoque_produtos` (
  `id_produto` int NOT NULL AUTO_INCREMENT,
  `nome_produto` varchar(100) NOT NULL,
  `desc_produto` varchar(100) DEFAULT NULL,
  `qtd_produto` int NOT NULL,
  `valor_produto` decimal(10,2) NOT NULL,
  `qtd_minima_produto` int NOT NULL,
  `fk_tbl_categorias_id_categoria` int DEFAULT NULL,
  PRIMARY KEY (`id_produto`),
  KEY `FK_tbl_estoque_produtos_2` (`fk_tbl_categorias_id_categoria`),
  CONSTRAINT `FK_tbl_estoque_produtos_2` FOREIGN KEY (`fk_tbl_categorias_id_categoria`) REFERENCES `tbl_categorias` (`id_categoria`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_estoque_produtos`
--

LOCK TABLES `tbl_estoque_produtos` WRITE;
/*!40000 ALTER TABLE `tbl_estoque_produtos` DISABLE KEYS */;
INSERT INTO `tbl_estoque_produtos` VALUES (1,'Saco de cimento 50kg','Cimento Portland CP II',100,35.50,20,1),(2,'Argamassa AC-III 20kg','Argamassa colante para porcelanato',50,45.90,10,1),(3,'Tijolo cerâmico 9x19x29','Tijolo comum de 6 furos',500,1.20,100,2),(4,'Bloco de concreto estrutural 14x19x39','Bloco para alvenaria estrutural',300,3.80,50,2),(5,'Piso cerâmico 60x60 tipo A','Piso cerâmico para áreas internas',200,29.90,40,4),(6,'Porcelanato polido 80x80','Porcelanato brilhante retificado',150,79.90,30,3),(7,'Tubo PVC água 20mm','Tubo de PVC para água fria',300,2.50,60,5),(8,'Conexão joelho 90° 20mm','Joelho de PVC para tubulação de água',200,0.80,40,5),(9,'Fio elétrico 2.5mm','Fio de cobre isolado',500,1.50,100,6),(10,'Disjuntor bipolar 32A','Dispositivo de proteção elétrica',100,15.00,20,6),(11,'Martelo em aço forjado','Martelo com cabo de madeira',50,25.00,10,7),(12,'Chave de fenda Phillips','Chave com ponta cruzada',100,8.00,20,7),(13,'Tinta acrílica branca 18L','Tinta lavável para paredes internas e externas',80,120.00,15,8),(14,'Rolo de lã para pintura','Rolo de pintura com cabo',150,12.50,30,8),(15,'Saco de areia lavada 20kg','Areia para construção',200,8.00,40,1),(16,'Brita nº 1','Pedra britada para concreto',150,15.00,30,1),(17,'Bloco de vidro ondulado 19x19','Bloco de vidro para iluminação',60,18.00,12,2),(18,'Revestimento cerâmico 30x60','Revestimento para paredes',180,35.00,35,3),(19,'Piso laminado cor madeira','Piso flutuante de alta resistência',120,49.90,25,4),(20,'Registro de esfera 1/2\"','Registro para controle de fluxo de água',80,10.50,16,5),(21,'Eletroduto corrugado 25mm','Tubo flexível para fiação elétrica',250,1.80,50,6),(22,'Alicate universal 8\"','Alicate para diversas funções',70,18.00,14,7),(23,'Tinta esmalte sintético preto 3.6L','Tinta para metal e madeira',40,55.00,8,8),(24,'Broxa para pintura','Pincel grande para pintura',90,7.00,18,8),(25,'Cal hidratada 20kg','Cal para argamassa e pintura',110,12.00,22,1),(26,'Vergalhão CA-50 10mm','Barra de aço para concreto armado',80,28.00,16,1),(27,'Telha cerâmica colonial','Telha para cobertura',1000,2.50,200,2),(28,'Azulejo branco 15x15','Revestimento cerâmico para cozinha e banheiro',300,19.90,60,3),(29,'Rodapé de PVC branco','Acabamento para piso',200,5.50,40,4),(30,'Sifão sanfonado universal','Sifão para pia e tanque',120,6.80,24,5);
/*!40000 ALTER TABLE `tbl_estoque_produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_itens_venda_estoque_pedido`
--

DROP TABLE IF EXISTS `tbl_itens_venda_estoque_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_itens_venda_estoque_pedido` (
  `id_item` int NOT NULL AUTO_INCREMENT,
  `qtd_item_venda` int NOT NULL,
  `preco_unitario_item` decimal(10,2) NOT NULL,
  `fk_tbl_estoque_produtos_id_produto` int DEFAULT NULL,
  `fk_tbl_pedidos_id_pedido` int DEFAULT NULL,
  PRIMARY KEY (`id_item`),
  KEY `FK_tbl_itens_venda_estoque_pedido_2` (`fk_tbl_estoque_produtos_id_produto`),
  KEY `FK_tbl_itens_venda_estoque_pedido_3` (`fk_tbl_pedidos_id_pedido`),
  CONSTRAINT `FK_tbl_itens_venda_estoque_pedido_2` FOREIGN KEY (`fk_tbl_estoque_produtos_id_produto`) REFERENCES `tbl_estoque_produtos` (`id_produto`),
  CONSTRAINT `FK_tbl_itens_venda_estoque_pedido_3` FOREIGN KEY (`fk_tbl_pedidos_id_pedido`) REFERENCES `tbl_pedidos` (`id_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_itens_venda_estoque_pedido`
--

LOCK TABLES `tbl_itens_venda_estoque_pedido` WRITE;
/*!40000 ALTER TABLE `tbl_itens_venda_estoque_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_itens_venda_estoque_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_pedidos`
--

DROP TABLE IF EXISTS `tbl_pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_pedidos` (
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  `data_pedido` date NOT NULL,
  `valor_pedido` decimal(10,2) NOT NULL,
  `fk_tbl_clientes_id_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `FK_tbl_pedidos_2` (`fk_tbl_clientes_id_cliente`),
  CONSTRAINT `FK_tbl_pedidos_2` FOREIGN KEY (`fk_tbl_clientes_id_cliente`) REFERENCES `tbl_clientes` (`id_cliente`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_pedidos`
--

LOCK TABLES `tbl_pedidos` WRITE;
/*!40000 ALTER TABLE `tbl_pedidos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_pedidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-12 20:12:27
