import mysql.connector
from datetime import datetime
import json
from model import Funcionario
from dal import FuncionarioDal, ProdutosDal


class FuncionarioController():
    
    
    def loginFuncionario(nome,senha):
                
            resultado = FuncionarioDal.loginFuncionario(nome,senha)
                
            if resultado :
                print("Login efetuado com sucesso \n")
                return True
            else:
                print("Usuario ou senha está incorrecta \n")
                return False        
            
            
    def loginStaff(nome,senha):
    
        resultado = FuncionarioDal.loginStaff(nome,senha)                        
        if resultado:
            print("\nLogin efetuado com sucesso \n")
            return True
        else:
            print("\nUsuario ou senha está incorrecta \n")
            return False
    
    def venda (vendas,comprador,user):
        
        descVenda = []
        for venda in vendas:
            ProdutosDal.venda(venda[0],venda[1])
            descProduto = ProdutosDal.buscar(venda[0],"idBD",venda[1])[0]  
            descVenda.append(descProduto)
            # print(f"id produto: {venda[0]} quantidade: {venda[1]}")
        detalhes = FuncionarioController.detalhes(descVenda)
        print(detalhes)    
        valorTotal = FuncionarioController.calcVenda(descVenda)
        #print(f'descrição: {descVenda} Valor: {valorTotal} comprador: {comprador} funcinario:{user}')
        data = FuncionarioController.calcData()
        FuncionarioDal.cadastroVenda(detalhes,valorTotal,comprador,user,data)
        
        
    def detalhes(descVenda):
        
        resultDetalhes = []
        for produto in descVenda:
            resultDetalhes.append(f'{produto[7]}x {produto[1]}')
        resultDetalhes = json.dumps(resultDetalhes)
        return resultDetalhes
        
    def calcVenda(descVenda):
        
        totalVenda = 0
        for vendaProduto in descVenda:
           totalVenda = vendaProduto[5] * vendaProduto[7] + totalVenda    
        return totalVenda
    
    def calcData():
        d = datetime.today()#.strftime("%d/%m/%Y, %H:%M:%S")
        return d        
            
            
            
           
            
            
            
            
            

    

                        
                        
            
        
        
        
        


# FuncionarioController.login("welington",507155)      
        
        
        
    