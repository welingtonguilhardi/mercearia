-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.21-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando estrutura para tabela mercearia.fornecedor
CREATE TABLE IF NOT EXISTS `fornecedor` (
  `idFornecedor` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL DEFAULT '0',
  `cnpj` int(11) NOT NULL,
  PRIMARY KEY (`idFornecedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela mercearia.fornecedor: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela mercearia.funcionario
CREATE TABLE IF NOT EXISTS `funcionario` (
  `idFuncionario` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `staff` int(11) NOT NULL DEFAULT 0,
  `nome` varchar(150) NOT NULL DEFAULT '0',
  `senha` varchar(150) NOT NULL DEFAULT '0',
  `setor` varchar(150) NOT NULL DEFAULT '0',
  PRIMARY KEY (`idFuncionario`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela mercearia.funcionario: ~2 rows (aproximadamente)
INSERT INTO `funcionario` (`idFuncionario`, `staff`, `nome`, `senha`, `setor`) VALUES
	(1, 1, 'welington', '50715', 'CEO'),
	(2, 0, 'marcos', '0', 'vendas');

-- Copiando estrutura para tabela mercearia.produto
CREATE TABLE IF NOT EXISTS `produto` (
  `idProduto` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL DEFAULT '',
  `marca` varchar(150) NOT NULL DEFAULT '',
  `categoria` varchar(150) DEFAULT NULL,
  `descricao` varchar(250) NOT NULL DEFAULT '',
  `valor` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idProduto`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela mercearia.produto: ~4 rows (aproximadamente)
INSERT INTO `produto` (`idProduto`, `nome`, `marca`, `categoria`, `descricao`, `valor`) VALUES
	(8, 'Refri', 'coca', 'Refri 1 litro', 'refigerante de 1 litro', 9),
	(9, 'Sabao', 'dove', 'limpeza', 'sabao para banho', 20),
	(10, 'sabao', 'dove', 'limpeza', 'sabao para banho', 20);

-- Copiando estrutura para tabela mercearia.venda
CREATE TABLE IF NOT EXISTS `venda` (
  `idVenda` int(11) NOT NULL AUTO_INCREMENT,
  `produto` varchar(150) DEFAULT NULL,
  `comprador` varchar(150) DEFAULT NULL,
  `vendedor` varchar(150) DEFAULT NULL,
  `quantidade` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`idVenda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Copiando dados para a tabela mercearia.venda: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
