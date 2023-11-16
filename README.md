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


