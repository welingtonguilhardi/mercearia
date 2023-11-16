# Mercearia Guilhardi - Sistema de Vendas em Python

## Descrição do Projeto
O Mercearia Guilhardi é um sistema de vendas desenvolvido em Python, utilizando o padrão MVC (Model-View-Controller) e o banco de dados MySQL para armazenar informações sobre produtos, funcionários e vendas.

## Funcionalidades Principais
- Cadastro, busca, alteração e exclusão de produtos.
- Autenticação de funcionários e staff.
- Realização de vendas, com registro de detalhes, comprador, funcionário e valor total.
- Registro de vendas, com opções de busca por data, funcionário e outros filtros.

## Estrutura do Projeto
O projeto é dividido em três partes principais:

### 1. Model
Contém as classes que representam os objetos principais do sistema:
- `Produtos`: Representa um produto com atributos como nome, marca, categoria, etc.
- `Funcionario`: Representa um funcionário ou staff com atributos como nome, senha, setor, etc.
- `Vendas`: Representa uma venda com detalhes, comprador, funcionário e valor.

### 2. DAL (Data Access Layer)
Responsável por realizar as operações de acesso ao banco de dados MySQL:
- `ProdutosDal`: Manipula dados relacionados a produtos.
- `FuncionarioDal`: Manipula dados relacionados a funcionários e staff.
- `VendasDal`: Realiza operações relacionadas a vendas, como busca e filtragem.

### 3. Controller
Contém a lógica de controle do sistema:
- `FuncionarioController`: Controla a autenticação de funcionários e staff, além de gerenciar operações relacionadas a vendas.

## Configuração e Execução
1. **Banco de Dados**: Configure as informações de conexão ao MySQL no arquivo `dal.py` (usuário, senha, host e nome do banco de dados).
2. **Dependências**: Certifique-se de ter o Python instalado, juntamente com o módulo `mysql-connector-python`. Você pode instalá-lo usando:
   ```bash
   pip install mysql-connector-python

## Execução

No linux:`python3 view.py`
No Windows: `python view.py`

# Configuração do Banco de Dados

Antes de começar, certifique-se de ter um servidor MySQL ou MariaDB instalado na sua máquina. Você pode usar o [MariaDB](https://mariadb.org/download/) para este exemplo.

## Executando o Script SQL

1. Abra o seu cliente MySQL ou MariaDB.

2. Conecte-se ao servidor com as credenciais apropriadas.

3. Abra um editor de SQL, como o HeidiSQL, e cole o seguinte script:

```sql
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


