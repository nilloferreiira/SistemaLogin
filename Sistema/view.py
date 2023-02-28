from model import Pessoa
from controller import ControllerCadastro, ControllerLogin

while True:
    decisao = int(input("Digite 1 para se cadastrar \n"
                    "Digite 2 para logar \n"
                    "Digite 3 para sair \n"))
    if decisao == 1:
        resultado = ControllerCadastro.Cadastrar()
        if resultado == 1:
            print("Usuário cadastrado com sucesso!")
        elif resultado == 2:
            print("Tamanho do nome digitado inválido!")
        elif resultado == 3:
            print("Email inválido!")
        elif resultado == 4:
            print("Senha muito curta!")
        elif resultado == 5:
            print("Email já cadastrado!")
        elif resultado == 6:
            print("Erro interno do sistema!")
    elif decisao == 2:
        resultado = ControllerLogin.Logar()
        if not resultado:
            print("Email ou senha incorretos!")
            
        else:
            print(resultado)
            break
    else:
        break