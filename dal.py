import mysql.connector
from model import Produtos,Funcionario


cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mercearia')



class ProdutosDal():
    
    def cadastro (produto:Produtos):
            inserir_produto = f"INSERT INTO `mercearia`.`produto` (`idProduto`, `nome`, `marca`,`categoria` , `descricao`, `valor`,`estoque`) VALUES (0, '{produto.nome}', '{produto.marca}','{produto.categoria}', '{produto.descricao}',{produto.valor},'{produto.estoque}');"
            cursor = cnx.cursor()
            cursor.execute(inserir_produto)
            cnx.commit()
            cursor.close()
            print("\nCadastro concluido com sucesso\n")
            
    def buscar(nome,tipo,qntd):
            cursor = cnx.cursor()
            if tipo == "n":    
                sql = f"SELECT  *  FROM  produto WHERE nome = '{nome}';"
            elif tipo == "id" or tipo == "idBD":
                sql = f"SELECT  *  FROM  produto WHERE idProduto = '{nome}';"                 
                cursor.execute(sql)
                linhas = cursor.fetchall()
                result = []
                for linha in linhas:
                    if tipo =="id":
                        desc = f'id: {linha[0]}\nnome: {linha[1]}\nmarca: {linha[2]}\ncategoria: {linha[3]}\ndescricao: {linha[4]}\nvalor: {linha[5]}\nestoque: {linha[6]}\n'
                        result.append(desc)
                        
                        print("Id:", linha[0])
                        print("Nome:", linha[1])
                        print("Marca:", linha[2],)
                        print("Categoria:", linha[3],)
                        print("Descrição:", linha[4],)
                        print("Valor:", linha[5], )
                        print("Estoque:", linha[6],"\n")
                    else:
                        desc = (linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],qntd) 
                        result.append(desc)
                cursor.close()           
                return result    
            else:
                sql = f"SELECT  *  FROM  produto WHERE categoria = '{nome}';"
            
            cursor.execute(sql)
            linhas = cursor.fetchall()    
            for linha in linhas:
            
                print("Id:", linha[0])
                print("Nome:", linha[1])
                print("Marca:", linha[2],)
                print("Categoria:", linha[3],)
                print("Descrição:", linha[4],)
                print("Valor:", linha[5], )
                print("Estoque:", linha[6],"\n")
                    
                
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
        
    def venda (id,quantidade):
        
        result = f"SELECT  *  FROM  produto WHERE idProduto = '{id}';"
        cursor = cnx.cursor()
        cursor.execute(result)
        linhas = cursor.fetchall()
        
        if len(linhas) == 0:
            print("Produto não encontrado")
        else:    
            estoqueAtual = linhas[0][6]
            estoqueNovo = estoqueAtual - quantidade
            if estoqueNovo < 0 :
                print(f"Só existem {estoqueAtual} no estoque desse produto")
                
            else:
                sql = f"UPDATE produto SET estoque = {estoqueNovo} WHERE idProduto = '{id}'"
                cursor = cnx.cursor()
                cnx.commit()
                cursor.close()
                print("Estoque Atualizado \n")
        
              
            
class FuncionarioDal():
    
    
    def loginFuncionario(nome,senha):
            consultar = f"SELECT  *  FROM  funcionario WHERE nome = '{nome}' AND senha = '{senha}' AND staff=0;"
            cursor = cnx.cursor()
            cursor.execute(consultar)
            linhas = cursor.fetchall()
            cursor.close()
            if len(linhas) == 0:
                return False
            else:
                return True
    def loginStaff(nome,senha):  
        consultar = f"SELECT  *  FROM  funcionario WHERE nome = '{nome}' AND senha = '{senha}' AND staff = 1 ;"
        cursor = cnx.cursor()
        cursor.execute(consultar)
        linhas = cursor.fetchall()
        cursor.close()
        if len(linhas) == 0:
            return False
        else:
            return True      
            
            
            
    
    def cadastro (funcionario:Funcionario):
        
            inserir_funcionario = f"INSERT INTO `mercearia`.`funcionario` (`staff`,`nome`, `senha`,`setor`) VALUES ({funcionario.staff}, '{funcionario.nome}', '{funcionario.senha}','{funcionario.setor}');"
            cursor = cnx.cursor()
            cursor.execute(inserir_funcionario)
            cnx.commit()
            cursor.close()
    
    def cadastroVenda(descVenda,valorTotal,comprador,user,data):
            sql = f"INSERT INTO `mercearia`.`venda` (`detalhes`, `comprador`, `funcionario`,`valor`,`data`) VALUES ( '{descVenda}', '{comprador}','{user}', '{valorTotal}','{data}');"
            cursor = cnx.cursor()
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            print("Venda concluida com sucesso!")
                  
    def buscar(busca,tipo):
        
        if tipo == "geral":
            sql = "SELECT * FROM venda"
        elif tipo == "id":
            sql = f"SELECT * FROM venda WHERE idVenda = {busca}"
        elif tipo == "funcionario":
            sql = f"SELECT * FROM venda WHERE funcionario = '{busca}'"
        elif tipo == "data":
            sql = f"SELECT * FROM venda WHERE data = {busca}"
        elif tipo == "dataFuncionario":
              sql = f"SELECT * FROM venda WHERE data = {busca[0]} AND funcionario = '{busca[1]}'"      
            
        cursor = cnx.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("\nResultado:\n")
        for linha in resultado:
            print(f"Id venda: {linha[0]}")
            print(f"Produtos: {linha[1]}")
            print(f"Comprador: {linha[2]}")
            print(f"Funcionario: {linha[3]}")
            print(f"Valor total: {linha[4]}")
            print(f"Data: {linha[5].strftime('%d/%m/%Y')}\n")
                
                     
class VendasDal:
    
    def renda(tipo,responseData,responseFuncionario):
        valorTotal = 0
        sql = "SELECT * FROM venda"
        cursor = cnx.cursor()
        cursor.execute(sql)
        linhas = cursor.fetchall()
        print("\nProdutos vendidos:\n")
        for linha in linhas:
            data = str(linha[5])
            ano = int(data[:4])
            mes = data[5:7]
            funcionario = linha[3]

            
            try:
                funcionarioMes:str = responseData[:2]
                funcionarioAno = int(responseData[2:]) 

                if tipo == "mes" and mes == funcionarioMes and ano == funcionarioAno:
                    print("\nId:", linha[0])
                    print("Detalhes:", linha[1])
                    print("Comprador:", linha[2])
                    print("Funcionario:", linha[3])
                    print("Valor:",linha[4])
                    print(f"Data: {linha[5]}\n")
                    valorTotal = valorTotal + linha[4]
                elif tipo == "funcionarioMes" and mes == funcionarioMes and ano == funcionarioAno and responseFuncionario == funcionario:
                    print("\nId:", linha[0])
                    print("Detalhes:", linha[1])
                    print("Comprador:", linha[2])
                    print("Funcionario:", linha[3])
                    print("Valor:",linha[4])
                    print(f"Data: {linha[5]}\n")
                    valorTotal = valorTotal + linha[4]        
            except:
                if tipo == "ano" and ano == responseData:
                    print("\nId:", linha[0])
                    print("Detalhes:", linha[1])
                    print("Comprador:", linha[2])
                    print("Funcionario:", linha[3])
                    print("Valor:",linha[4])
                    print(f"Data: {linha[5]}\n")
                    valorTotal = valorTotal + linha[4]
                elif tipo == "funcionarioAno" and ano == responseData and responseFuncionario == funcionario:
                    print("\nId:", linha[0])
                    print("Detalhes:", linha[1])
                    print("Comprador:", linha[2])
                    print("Funcionario:", linha[3])
                    print("Valor:",linha[4])
                    print(f"Data: {linha[5]}\n")
                    valorTotal = valorTotal + linha[4]    
                    


            
        print(f"\nVALOR DE GANHOS TOTAIS: {valorTotal}\n")    
        cursor.close()        
                
                      
            
        

        
                
            
          