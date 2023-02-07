"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
import
"""
import base64
from hashlib import sha512
import sys
from cipher_decipher import RSA

def Sign():
    """
    Cria arquivo texto com mensagem de outro arquivo texto existente e assinatura
    """

    # abre arquivo nao cifrado
    file_name = input(f'DIGITE O NOME DO ARQUIVO QUE DESEJA ASSINAR: ')
    try:
        file = open(file_name + '.txt',"r")
    except:
        print("Arquivo nao encontrado\n")

    # abre arquivo com a chave privada
    private_key = open('private_key.txt', "r")
    pk = private_key.readlines()
    private_key.close()

    # lendo a mesagem do arquivo
    message = file.readlines()
    message = ' '.join([str(m) for m in message])

    # mensagem convertida para base64
    message_utf8 = message.encode("utf-8")
    message64_bytes = base64.b64encode(message_utf8)
    message64_string = message64_bytes.decode("utf-8")

    # hash SHA-3
    message_hash = int.from_bytes(sha512(message_utf8).digest(), 'big')

    # assinatura
    signature = RSA(message_hash, pk)

    # assinatura convertida para base64
    signature_bytes = signature.to_bytes(sys.getsizeof(signature),'big')
    signature64 = base64.b64encode(signature_bytes)

    message_signature = message64_string + '\n'

    # cria arquivo com mensagem e assinatura em base64
    file_sign = open(file_name + '_signed.txt',"w")
    file_sign.write(message64_string + '\n')
    file_sign.close()
    file_sign = open(file_name + '_signed.txt',"ab")
    file_sign.write(signature64)
    file_sign.close()
    
    file.close()

def Verify_signature():
    """
    Verifica se a mensagem de um arquivo texto assinado é válida
    """

    # abre arquivo com mensagem e assinatura
    file_name = input(f'DIGITE O NOME DO ARQUIVO QUE DESEJA VERIFICAR: ')
    try:
        file_sign = open(file_name + '.txt',"r")
    except:
        print("Arquivo nao encontrado\n")

    # abre arquivo com a chave publica
    public_key = open('public_key.txt', "r")
    pk = public_key.readlines()
    public_key.close()

    # lendo a mesagem do arquivo
    file_lines = file_sign.readlines()
    # message64_string = file_lines[0]
    # signature64 = file_lines[1]

    # message convertida da base64 para utf-8
    message64_bytes = file_lines[0].encode("utf-8")
    message_utf8 = base64.b64decode(message64_bytes)
    message = message_utf8.decode("utf-8")

    # hash SHA-3
    message_hash = int.from_bytes(sha512(message_utf8).digest(), 'big')

    # assinatura convertida da base64 para int
    signature64_utf8 = file_lines[1].encode("utf-8")
    signature_bytes = base64.b64decode(bytes(signature64_utf8))
    signature = int.from_bytes(signature_bytes, 'big')

    # calculo do hash da mensagem original
    possible_message_hash = RSA(signature, pk)

    # comparação de hash
    if message_hash == possible_message_hash:
        print(f'Assinatura verificada\nMensagem: {message}')
    else:
        print(f'Verificação inválida\n')

    file_sign.close()