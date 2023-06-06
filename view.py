from dal import ProdutosDal,FuncionarioDal,VendasDal
from model import Produtos
from controller import FuncionarioController

res = False
staff = False
login = False


print("Bem vindo a mercearia Guilhardi \n")
while True:
    
    if login == False:
        print("Fazer login como:\nDigite 1:Staff \nDigite 2:Funcionario")
        y = input("")
        
        if y == "2":
            user = input("User: ")
            senha = input("Senha: ")    
            res = FuncionarioController.loginFuncionario(user,senha)
            FirstLogin = True
            login = True
        elif y == "1":    
            user = input("User: ")
            senha = input("Senha: ")  
            staff = FuncionarioController.loginStaff(user,senha)
            FirstLogin = True
            login = True
        else:
            print("Numero invalido")    
            
    else:
        if res or staff:
            print("Digite 0 para: Encerrar o sistema \nDigite 1 para: Cadastrar um produto \nDigite 2 para: Buscar um produto cadastrado pelo nome \nDigite 3 para: Buscar um produto cadastrado pela categoria \nDigite 4 para: Alterar um produto \nDigite 5 para: Excluir um produto\nDigite 6 para: Realizar uma venda\nDigite 7 para: Buscar vendas\nDigite 8 para: Filtrar ganhos")                
            
            x = input("Escolha um numero: ")
            
            if x == "1" or x == "4"  or x == "5" or  x == "7":
                if res:
                    print("\nApenas staff podem fazer isto\n")
                    continue
                    
                    
            if x == "0":
                print("Sistema encerrado")
                break
            
            elif x == "1":
                nome = input("Nome do produto? ")
                marca = input("Marca do produto? ")
                categoria = input("Categoria do produto? ")
                descricao = input("Descricao do produto? ")
                valor = int(input("Valor do produto? "))
                estoque = int(input("Estoque do produto? "))
                result = Produtos(nome,marca,categoria,descricao,valor,estoque)
                ProdutosDal.cadastro(result)    
                
                
            elif x == "2":
                
                nome = input("Nome? ")
                ProdutosDal.buscar(nome,"n",None)
                
            elif  x == "3":
                categoria = input("Categoria? ")
                ProdutosDal.buscar(categoria,"c",None)
                
            elif x == "4":
                id = int(input("Id do produto? "))
                ProdutosDal.buscar(id,"id",None)
                print("\nDeseja alterar este produto? ")
                res = input(" s:sim n:não \n")
                
                if res == "s":
                    
                    nome = input("Nome? ")
                    marca = input("Marca? ")
                    categoria = input("Categoria? ")
                    descricao = input("Descricao? ")
                    valor = int(input("Valor? "))
                    
                    ProdutosDal.alterar(id, nome, marca, categoria, descricao, valor)
                else:
                    pass    
                
            elif x == "5":
                    
                id = int(input("Id do produtos? "))
                print(str(ProdutosDal.buscar(id,"id",None)[0]))
                print("\nDeseja excluir este produto? ")
                res = input(" s:sim n:não \n")
                
                if res == "s":
                    ProdutosDal.remove(id)
                    print("\nProduto excluido com sucesso")
                else:
                    pass    
                
            elif x == "6":
                
                vendas = []
                while True:
                    print("Deseja adicionar produto na venda? \n")
                    qnt = input("s:sim n:não \n")
                    if qnt == "s" or qnt == "S":
                        id = int(input("id? "))
                        quantidade = int(input("quantidade? "))
                        venda = (id,quantidade)
                        vendas.append(venda)
                    elif qnt == "n" and len(vendas) > 0 or qnt == "N" and len(vendas) > 0:
                        comprador = input("comprador? ")    
                        FuncionarioController.venda(vendas,comprador,user)
                        break
                    else:
                        print('\nOcorreu um error ao finalizar sua venda\n')  
                        break
            elif x == "7":
                print('\nBuscar por:\n1:Todas vendas\n2:Id da venda\n3:Funcionario\n4:Data\n5:Data e funcionario')
                pergunta = int(input("? "))
                if pergunta == 1:
                    FuncionarioDal.buscar(None,"geral")
                elif pergunta == 2:
                    buscaId = int(input("id? "))
                    FuncionarioDal.buscar(buscaId ,"id")
                elif pergunta == 3:
                    funcionario = input("Nome funcionario? ")
                    FuncionarioDal.buscar(funcionario, "funcionario")
                elif pergunta == 4:
                    dia = input("Dia? ")
                    mes = input("Mês? ")
                    ano = input("Ano? ")
                    data = f"{ano}{mes}{dia}"
                    FuncionarioDal.buscar(data,"data")
                elif pergunta == 5:
                    dia = input("Dia? ")
                    mes = input("Mês? ")
                    ano = input("Ano? ")
                    funcionario = input("Nome funcionario? ")
                    data = f"{ano}{mes}{dia}"
                    dataFuncionario = [data, funcionario]
                    FuncionarioDal.buscar(dataFuncionario, "dataFuncionario")
                else:
                    print("\nOpção invalida\n")
                
            elif x == "8":
                print("\nDigite 1 para: Buscar por ano\nDigite 2 para: Buscar por mês\nDigite 3 para: Buscar por mês e funcionario\nDigite 4 para: Buscar por ano e funcionario\n")        
                pergunta = input("? ")
                
                if pergunta == "1":
                    ano = int(input("Ano? "))
                    VendasDal.renda("ano",ano,None)
                elif pergunta == "2":
                    mes = input("Mês? ")
                    ano = input("Ano? ")
                    VendasDal.renda("mes",mes+ano,None)
                elif pergunta == "3":
                    mes = input("Mês? ")
                    ano = input("Ano? ")
                    funcionario = input("Nome funcionario? ")
                    VendasDal.renda("funcionarioMes",mes+ano,funcionario)
                elif pergunta == "4":
                    ano = int(input("Ano? "))
                    funcionario = input("Nome funcionario? ")
                    VendasDal.renda("funcionarioAno",ano,funcionario)
            
            
            
            
            
            
            else:
                print("\nNumero invalido\n")                 
        
        else:
            login = False                         
                    
                
                