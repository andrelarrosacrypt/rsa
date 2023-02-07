"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
import
"""
from create_file import Create_file
from cipher_decipher import Cipher, Decipher
from signature import Sign, Verify_signature

#https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
menu_options = {
    1 : 'Criar arquivo texto',
    2 : 'Cifrar arquivo texto',
    3 : 'Decifrar arquivo texto',
    4 : 'Assinar arquivo texto',
    5 : 'Validar assinatura',
    6 : 'Sair'
}

def print_menu():
    print('\n')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    print("\n")
    Create_file()

def option2():
    print("\n")
    Cipher()

def option3():
    print("\n")
    Decipher()

def option4():
    print("\n")
    Sign()

def option5():
    print("\n")
    Verify_signature()
    

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha uma opcao: '))
        except:
            print('ERRO: Entrada invalida. Tente novamente')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            exit()
        else:
            print('ERRO: Entrada invalida. Tente novamente')