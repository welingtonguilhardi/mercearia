import mysql.connector
from model import Funcionario

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mercearia')

class FuncionarioController():
    
    
    def login(nome,senha):
                
            consultar = f"SELECT  *  FROM  funcionario WHERE nome = '{nome}' AND senha = '{senha}';"
            cursor = cnx.cursor()
            cursor.execute(consultar)
            linhas = cursor.fetchall()
                
            if len(linhas) == 0:
                print("Usuario ou senha está incorrecta \n")
                return False
            else:
                print("Login efetuado com sucesso \n")
                return True        
            cursor.close()
            
    def loginStaff(nome,senha):
                
            consultar = f"SELECT  *  FROM  funcionario WHERE nome = '{nome}' AND senha = '{senha}' AND staff = 1 ;"
            cursor = cnx.cursor()
            cursor.execute(consultar)
            linhas = cursor.fetchall()
                
            if len(linhas) == 0:
                return False
            else:
                return True        
            cursor.close()            
            
        
        
        
        


FuncionarioController.login("welington",507155)      
        
        
        
    