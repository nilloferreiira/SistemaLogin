from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Pessoa
from hashlib import sha256

def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "login"
    PORT = 3308

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro:

    @classmethod
    def Verificar_dados(cls, nome, email, senha):
        if len(nome) < 3 or len(nome) > 50:
            return 2
        if len(email) < 13 or len(email) > 200:
            return 3
        if len(senha) < 6 or len(senha) > 100:
            return 4
        
        return 1


    @classmethod
    def Cadastrar(cls):
        nome = input("Digite o nome que deseja cadastrar: ")
        email = input("Digite a email que deseja cadastrar: ")
        senha = input("Digite a senha que deseja cadastrar: ")
        
        session  = RetornaSession()

        user = session.query(Pessoa).filter(Pessoa.email == email).all()
        if len(user) > 0:
            
            return 5

        dados_verificados = cls.Verificar_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados

        try:
            senha = sha256(senha.encode()).hexdigest()
            x = Pessoa(nome=nome, email=email, senha=senha)
            session.add(x)
            session.commit()
            
            return 1
        except:
            return 6


class ControllerLogin():
    @classmethod
    def Logar(cls):
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        senha = sha256(senha.encode()).hexdigest()
        
        session = RetornaSession()

        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha ==  senha).all()

        if len(logado) == 1:
            
            return {'Logado': True, 'id': logado[0].id}
        else:
            
            return False            

