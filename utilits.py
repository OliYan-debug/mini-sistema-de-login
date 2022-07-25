from save_data import saveData
from recovery_data import recoveryData
from time import sleep
import os

class Utilits:

    def data(self):
        data = recoveryData()
        return data
    
    
    def limpar_terminal(self):
        sleep(2)
        os.system('cls')
        

    def criar_conta(self):
        data = ut.data()
        ut.nome = input('\nDigite Seu Usuario: ').strip()
        ut.senha = input('Digite Sua Senha: ').strip()

        if ut.nome == "" or  ut.senha == "":
            print("\n O usuário ou a senha não podem ser vazio!")
            ut.limpar_terminal()
            ut.criar_conta()
        elif ut.verificar_conta_criar():
            print('\nConta Criada Com Sucesso')
            saveData(ut.nome, ut.senha)
            ut.limpar_terminal()
            sl.menu()
        else:
            print('\nUsuario Ja Existente')
            ut.limpar_terminal()
            ut.criar_conta()

    def verificar_conta_criar(self):
        data = ut.data()
        ut.sucesso_criar = True

        for dado in data:
            if ut.nome == dado[0]:
                ut.sucesso_criar = False
        
        return ut.sucesso_criar
            
    
    def logar_conta(self):
        data = ut.data()

        ut.login_nome = input('\nDigite Seu Login: ')
        ut.login_senha = input('Digite Sua Senha: ')

        ut.sucesso_login = False
        
        for dado in data:
            if dado[0] == ut.login_nome and dado[1] == ut.login_senha:
                ut.sucesso_login = True
        if ut.sucesso_login:
            print('\nUsuario Logado Com Sucesso!')
            ut.limpar_terminal()
        else:
            ut.verificar_conta_login()
            
    def verificar_conta_login(self):
        ut.falha_login = False
        data = ut.data()
        if not ut.sucesso_login:
            for dado in data:
                if ut.login_nome == dado[0]:
                    ut.falha_login = True
            if ut.falha_login:
                print('\nSenha Incorreta')
                ut.limpar_terminal()
                ut.logar_conta()
            else:
                print('\nUsuario Inexistente!')
                ut.limpar_terminal()
                sl.menu()
    
    def sair_programa(self):
        print('\nSaindo Do Programa')
        ut.limpar_terminal()
        os.system('exit')


ut = Utilits()


