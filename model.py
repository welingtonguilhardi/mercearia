class Produtos():
    
    def __init__(self,nome,marca,categoria,descricao,valor,estoque):
        
        self.nome = nome
        self.marca = marca
        self.categoria = categoria
        self.descricao = descricao    
        self.valor = valor
        self.estoque = estoque
class Funcionario () :
    
    def __init__(self,staff,nome,senha,setor):
        
        self.staff = staff
        self.nome = nome
        self.senha = senha
        self.setor = setor
        
class Vendas ():
    
    def __init__(self,detalhes,comprador,funcionario,valor):   
        
        self.detalhes = detalhes
        self.comprador = comprador 
        self.funcionario = funcionario
        self.valor = valor  
                