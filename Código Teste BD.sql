CREATE DATABASE  IF NOT EXISTS `teste_projeto` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `teste_projeto`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: teste_projeto
-- ------------------------------------------------------
-- Server version	8.0.42

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
  `nome_adm` varchar(20) DEFAULT NULL,
  `senha_adm` varchar(20) DEFAULT NULL,
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
  `nome_categoria` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_categorias`
--

LOCK TABLES `tbl_categorias` WRITE;
/*!40000 ALTER TABLE `tbl_categorias` DISABLE KEYS */;
INSERT INTO `tbl_categorias` VALUES (1,'Materiais Básicos'),(2,'Revestimentos'),(3,'Hidráulica'),(4,'Elétrica'),(5,'Ferramentas'),(6,'Tintas'),(7,'Jardinagem'),(8,'Segurança');
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
  `nome_cliente` varchar(100) DEFAULT NULL,
  `cpf_cliente` varchar(14) DEFAULT NULL,
  `senha_cliente` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `cpf_cliente` (`cpf_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_clientes`
--

LOCK TABLES `tbl_clientes` WRITE;
/*!40000 ALTER TABLE `tbl_clientes` DISABLE KEYS */;
INSERT INTO `tbl_clientes` VALUES (1,'João da Silva','123.456.789-01','senha456'),(2,'Maria Souza','987.654.321-02','senha789'),(3,'Carlos Oliveira','234.567.890-03','senha101'),(4,'Ana Pereira','345.678.901-04','senha202'),(5,'Paulo Rocha','456.789.012-05','senha303');
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
  `nome_produto` varchar(100) DEFAULT NULL,
  `qtd_produto` int DEFAULT NULL,
  `valor_produto` decimal(10,2) DEFAULT NULL,
  `fk_tbl_categorias_id_categoria` int DEFAULT NULL,
  `qtd_min_produto` int DEFAULT NULL,
  PRIMARY KEY (`id_produto`),
  KEY `FK_tbl_estoque_produtos_2` (`fk_tbl_categorias_id_categoria`),
  CONSTRAINT `FK_tbl_estoque_produtos_2` FOREIGN KEY (`fk_tbl_categorias_id_categoria`) REFERENCES `tbl_categorias` (`id_categoria`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_estoque_produtos`
--

LOCK TABLES `tbl_estoque_produtos` WRITE;
/*!40000 ALTER TABLE `tbl_estoque_produtos` DISABLE KEYS */;
INSERT INTO `tbl_estoque_produtos` VALUES (1,'Saco de Cimento 50kg',100,25.00,1,20),(2,'Tijolo Cerâmico 6 furos',500,1.50,1,100),(3,'Barra de Aço CA-50 10mm',200,30.00,1,50),(4,'Areia Média 20kg',300,12.00,1,50),(5,'Brita 19mm 20kg',250,15.00,1,50),(6,'Piso Cerâmico 45x45cm',400,20.00,2,80),(7,'Azulejo Branco 30x60cm',350,18.00,2,70),(8,'Porcelanato Polido 60x60cm',300,40.00,2,60),(9,'Rejunte Acrílico 1kg',200,10.00,2,40),(10,'Manta Asfáltica 10m²',150,50.00,2,30),(11,'Tubo PVC 100mm 6m',100,20.00,3,20),(12,'Conexão Joelho 90° 100mm',200,5.00,3,40),(13,'Caixa Sifonada 150x150mm',150,15.00,3,30),(14,'Registro de Gaveta 1\"',100,30.00,3,20),(15,'Fita Veda Rosca 10m',300,3.00,3,60),(16,'Fio Elétrico 2.5mm² 100m',200,80.00,4,40),(17,'Tomada 10A',300,8.00,4,60),(18,'Interruptor Simples',250,5.00,4,50),(19,'Disjuntor Unipolar 20A',100,12.00,4,20),(20,'Lâmpada LED 9W',500,10.00,4,100),(21,'Martelo 500g',100,20.00,5,20),(22,'Chave de Fenda Jogo 6 peças',50,30.00,5,10),(23,'Trena 5m',80,15.00,5,16),(24,'Nível 1m',60,25.00,5,12),(25,'Parafusadeira Elétrica',40,150.00,5,8);
/*!40000 ALTER TABLE `tbl_estoque_produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_produto_venda`
--

DROP TABLE IF EXISTS `tbl_produto_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_produto_venda` (
  `id_produto_venda` int NOT NULL AUTO_INCREMENT,
  `fk_tbl_estoque_produtos_id_produto` int DEFAULT NULL,
  `qtd_prod_venda` int DEFAULT NULL,
  `preco_unitario_prod_venda` decimal(10,2) DEFAULT NULL,
  `fk_tbl_vendas_id_venda` int DEFAULT NULL,
  PRIMARY KEY (`id_produto_venda`),
  KEY `FK_produto_venda_1` (`fk_tbl_estoque_produtos_id_produto`),
  KEY `FK_produto_venda_3` (`fk_tbl_vendas_id_venda`),
  CONSTRAINT `FK_produto_venda_1` FOREIGN KEY (`fk_tbl_estoque_produtos_id_produto`) REFERENCES `tbl_estoque_produtos` (`id_produto`) ON DELETE RESTRICT,
  CONSTRAINT `FK_produto_venda_3` FOREIGN KEY (`fk_tbl_vendas_id_venda`) REFERENCES `tbl_vendas` (`id_venda`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_produto_venda`
--

LOCK TABLES `tbl_produto_venda` WRITE;
/*!40000 ALTER TABLE `tbl_produto_venda` DISABLE KEYS */;
INSERT INTO `tbl_produto_venda` VALUES (1,1,2,25.00,1),(2,6,3,20.00,1),(3,2,10,1.50,2),(4,7,5,18.00,2),(5,11,1,20.00,3),(6,16,2,80.00,4),(7,21,1,20.00,4),(8,3,4,30.00,5),(9,18,10,5.00,5);
/*!40000 ALTER TABLE `tbl_produto_venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_vendas`
--

DROP TABLE IF EXISTS `tbl_vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_vendas` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `data_venda` date DEFAULT NULL,
  `valor_venda` decimal(10,2) DEFAULT NULL,
  `fk_tbl_clientes_id_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id_venda`),
  KEY `FK_tbl_vendas_2` (`fk_tbl_clientes_id_cliente`),
  CONSTRAINT `FK_tbl_vendas_2` FOREIGN KEY (`fk_tbl_clientes_id_cliente`) REFERENCES `tbl_clientes` (`id_cliente`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_vendas`
--

LOCK TABLES `tbl_vendas` WRITE;
/*!40000 ALTER TABLE `tbl_vendas` DISABLE KEYS */;
INSERT INTO `tbl_vendas` VALUES (1,'2024-01-15',120.00,1),(2,'2024-01-20',105.00,2),(3,'2024-02-10',20.00,3),(4,'2024-02-25',180.00,4),(5,'2024-03-05',170.00,5);
/*!40000 ALTER TABLE `tbl_vendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-11 18:53:36

/*Select tbl_produto_venda*/
select tbl_clientes.nome_cliente, tbl_vendas.id_venda, tbl_estoque_produtos.nome_produto,  
tbl_produto_venda.preco_unitario_prod_venda, tbl_produto_venda.qtd_prod_venda,  
tbl_vendas.valor_venda, tbl_vendas.data_venda  
from tbl_produto_venda  
join tbl_clientes  
join tbl_vendas  
join tbl_estoque_produtos  
on tbl_produto_venda.fk_tbl_estoque_produtos_id_produto = tbl_estoque_produtos.id_produto  
and tbl_produto_venda.fk_tbl_vendas_id_venda = tbl_vendas.id_venda  
and tbl_vendas.fk_tbl_clientes_id_cliente = tbl_clientes.id_cliente  
order by tbl_clientes.nome_cliente, tbl_vendas.id_venda;
