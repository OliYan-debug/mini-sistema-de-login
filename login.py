from utilits import *
os.system("cls")


class sistemalogin():
    
    def menu(self):
        print('''
[ Version 2.0 ] [ By: Nanaue & Japa ]

[1] Logar 
[2] Criar Conta
[3] Sair Do Programa
''')    
        try:
            menu = int(input('\nSelecione Sua Opcao: '))
            if menu == 1:
                ut.logar_conta()
            elif menu == 2:
                ut.criar_conta()
            elif menu == 3:
                ut.sair_programa()
            else:
                print('\nDigite apenas opcoes listadas no menu!\nVoltando ao menu...')
                ut.limpar_terminal()
                sl.menu()
        except:
            ut.limpar_terminal()
            sl.menu()
            

sl = sistemalogin()
ut = Utilits()
sl.menu()