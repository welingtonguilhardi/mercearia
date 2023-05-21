from dal import ProdutosDal
from model import Produtos
from controller import FuncionarioController

staff = False
login = False


print("Bem vindo a mercearia Guilhardi \n")
while True:
    
    if login == False:
        nome = input("User: ")
        senha = input("Senha: ")    
        res = FuncionarioController.login(nome,senha)
        staff = FuncionarioController.loginStaff(nome,senha)
        login = True
    else:        
        if res == True and staff == False:
                print("Digite 0 para encerrar o sistema \nDigite 1 para cadastrar um produto \nDigite 2 para buscar um produto cadastrado pelo nome \nDigite 3 para buscar um produto cadastrado pela categoria \nDigite 4 para alterar um produto \nDigite 5 para excluir um produto")
                
                x = int(input("Escolha um numero: "))
                
                
                if x == 0:
                    print("Sistema encerrado")
                    break

                elif x == 1 or x == 4 or x == 5:
                    print("\nApenas staff podem fazer isto\n")
                elif x == 2:
                    
                    nome = input("Nome? ")
                    ProdutosDal.buscar(nome,"n")
                    
                elif  x == 3:
                    categoria = input("Categoria? ")
                    ProdutosDal.buscar(categoria,"c")
                    

                            
                    
    
        
        elif staff == True and res == True:
                print("Digite 0 para encerrar o sistema \nDigite 1 para cadastrar um produto \nDigite 2 para buscar um produto cadastrado pelo nome \nDigite 3 para buscar um produto cadastrado pela categoria \nDigite 4 para alterar um produto \nDigite 5 para excluir um produto")
                
                x = int(input("Escolha um numero: "))
        
                if x == 1:
                    nome = input("Nome do produto? ")
                    marca = input("Marca do produto? ")
                    categoria = input("Categoria do produto? ")
                    descricao = input("Descricao do produto? ")
                    valor = int(input("Valor do produto? "))
                    result = Produtos(nome,marca,categoria,descricao,valor)
                    ProdutosDal.cadastro(result)
                        
                elif x == 4:
                    id = int(input("Id do produto? "))
                    ProdutosDal.buscar(id,"id")
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
                    
                elif x == 5:
                        
                    id = int(input("Id do produtos? "))
                    ProdutosDal.buscar(id,"id")
                    print("\nDeseja excluir este produto? ")
                    res = input(" s:sim n:não \n")
                    
                    if res == "s":
                        ProdutosDal.remove(id)
                        print("\nProduto excluido com sucesso")
                    else:
                        pass
        else:
            login = False         
                 
              
            