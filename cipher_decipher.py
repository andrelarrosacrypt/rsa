"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
import
"""
from keys import Keys

def RSA(x, key):
    """
    RSA cipher/decipher
    """
    return pow(int(x), int(key[0]), int(key[1]))

def Cipher():
    """
    Cifra arquivo texto existente
    """

    # abre arquivo nao cifrado
    file_name = input(f'DIGITE O NOME DO ARQUIVO QUE DESEJA CIFRAR: ')
    try:
        file = open(file_name + '.txt',"r")
    except:
        print("Arquivo nao encontrado\n")

    # gera as chaves publica e privada
    public_key, private_key = Keys()

    # cria arquivo texto com chave privada
    file_priv = open('private_key.txt',"w")
    file_priv.write(str(private_key[0]) + '\n' + str(private_key[1]))
    file_priv.close()
    # cria arquivo texto com chave publica
    file_publ = open('public_key.txt',"w")
    file_publ.write(str(public_key[0]) + '\n' + str(public_key[1]))
    file_publ.close()

    # cifracao
    ciphered_message = ''
    while(True):
        char = file.read(1)

        if not char:
            break

        ciphered_message += str(RSA(ord(char), public_key)) + '\n'

    # cria arquivo texto com a mensagem cifrada
    file_ciphered = open(file_name + '_ciphered.txt', "w")
    file_ciphered.write(ciphered_message)
    file_ciphered.close()

    file.close()


def Decipher():
    """
    Decifra arquivo texto existente
    """

    # abre arquivo cifrado
    file_name = input(f'DIGITE O NOME DO ARQUIVO QUE DESEJA DECIFRAR: ')
    try:
        file = open(file_name + '.txt',"r")
    except:
        print("Arquivo nao encontrado\n")

    # abre arquivo com a chave privada
    private_key = open('private_key.txt', "r")
    pk = private_key.readlines()
    private_key.close()

    # decifracao
    lines = file.readlines()
    deciphered_message = ''
    for l in (lines):
        deciphered_message += chr(RSA(l, pk))

    print(f'Mensagem decifrada: {deciphered_message}')

    file.close()