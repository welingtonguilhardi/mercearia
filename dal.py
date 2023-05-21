import mysql.connector
from model import Produtos,Funcionario


cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mercearia')


class ProdutosDal():
    
    def cadastro (produto:Produtos):
            inserir_produto = f"INSERT INTO `mercearia`.`produto` (`idProduto`, `nome`, `marca`,`categoria` , `descricao`, `valor`) VALUES (0, '{produto.nome}', '{produto.marca}','{produto.categoria}', '{produto.descricao}',{produto.valor});"
            cursor = cnx.cursor()
            cursor.execute(inserir_produto)
            cnx.commit()
            cursor.close()
            
    def buscar(nome,tipo):
        
            if tipo == "n":    
                consultar = f"SELECT  *  FROM  produto WHERE nome = '{nome}';"
                cursor = cnx.cursor()
                cursor.execute(consultar)
                linhas = cursor.fetchall()
                
                for linha in linhas:
                    
                    print("Id:", linha[0])
                    print("Nome:", linha[1])
                    print("Marca:", linha[2],)
                    print("Categoria:", linha[3],)
                    print("Descrição:", linha[4],)
                    print("Valor:", linha[5], "\n")
                
                cursor.close()
            elif tipo == "id":
                consultar = f"SELECT  *  FROM  produto WHERE idProduto = '{nome}';"
                cursor = cnx.cursor()
                cursor.execute(consultar)
                linhas = cursor.fetchall()
                
                for linha in linhas:
                    
                    print("Id:", linha[0])
                    print("Nome:", linha[1])
                    print("Marca:", linha[2],)
                    print("Categoria:", linha[3],)
                    print("Descrição:", linha[4],)
                    print("Valor:", linha[5], "\n")
            else:
                consultar = f"SELECT  *  FROM  produto WHERE categoria = '{nome}';"
                cursor = cnx.cursor()
                cursor.execute(consultar)
                linhas = cursor.fetchall()
                
                for linha in linhas:
                    
                    print("Id:", linha[0])
                    print("Nome:", linha[1])
                    print("Marca:", linha[2],)
                    print("Categoria:", linha[3],)
                    print("Descrição:", linha[4],)
                    print("Valor:", linha[5], "\n")
                
                cursor.close()
                
    def alterar(id,nome,marca,categoria,descricao,valor):
        
        sql = f"UPDATE produto SET nome = '{nome}', marca = '{marca}',categoria = '{categoria}', descricao = '{descricao}', valor = '{valor}' WHERE idProduto = '{id}'"
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        cursor.close()             
    
    def remove (id):
        
        sql = f"DELETE FROM produto WHERE idProduto = {id};"
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        cursor.close()   
            
class FuncionarioDal():
    
    def cadastro (funcionario:Funcionario):
        
            inserir_funcionario = f"INSERT INTO `mercearia`.`funcionario` (`staff`,`nome`, `senha`,`setor`) VALUES ({funcionario.staff}, '{funcionario.nome}', '{funcionario.senha}','{funcionario.setor}');"
            cursor = cnx.cursor()
            cursor.execute(inserir_funcionario)
            cnx.commit()
            cursor.close()
            
        
    

                
# ProdutosDal.alterar(8,"Refrigerante","Coca-cola","Liquidos","Refri 1 litro",8) 
        
        
# p1 = Produtos("Well","Pro","categoria","descricao",20)      

# ProdutosDal.buscar("Well")
        
# ProdutosDal.cadastro(p1) 

# ProdutosDal.remove(6)

     