"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

def Create_file():
    """
    cria arquivo texto ou sobrescreve mensagem em arquivo ja existente
    """
    
    file_name = input(f'DIGITE O NOME DO ARQUIVO: ')
    message = input(f'DIGITE A MENSAGEM: ')

    file = open(file_name + '.txt',"w")
    file.write(message)

    file.close()
