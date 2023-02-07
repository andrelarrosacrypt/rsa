import base64
from hashlib import sha512
from rsa import RSA
import sys
from cipher_decipher import RSA

def Sign():
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

    # message convertida para base64
    message_utf8 = message.encode("utf-8")
    #print(f'message_utf8 sign = {message_utf8}\n')
    #print(f'message_utf8 len sign = {len(message_utf8)}\n')
    message64_bytes = base64.b64encode(message_utf8)
    #print(f'message64_bytes sign = {message64_bytes}\n')
    #print(f'message64_bytes len sign = {len(message64_bytes)}\n')
    message64_string = message64_bytes.decode("utf-8")

    # print(f'message64_string  = {message64_string}\n')
    # print(f'message_utf8  = {message_utf8}\n')

    # SHA-3
    message_hash = int.from_bytes(sha512(message_utf8).digest(), 'big')
    #print(f'message_hash sign = {message_hash}\n')

    # assinatura
    signature = RSA(message_hash, pk)
    #print(f'signature = {signature}\n')

    # assinatura convertida para base64
    signature_bytes = signature.to_bytes(sys.getsizeof(signature),'big')
    #print(f'signature_bytes sign = {signature_bytes}\n')
    #print(f'signature_bytes len sign = {len(signature_bytes)}\n')
    signature64 = base64.b64encode(signature_bytes)
    
    signature_bytes2 = base64.b64decode(signature64)
    if signature_bytes == signature_bytes2:
        print(f'TRUE\n')
    
    print(f'signature = {signature}\n')
    print(f'signature type = {type(signature)}\n')
    print(f'signature_bytes = {signature_bytes}\n')
    print(f'signature_bytes type = {type(signature_bytes)}\n')
    print(f'signature64 = {signature64}\n')
    print(f'signature64 type = {type(signature64)}\n')
    #print(f'signature64 len sign = {len(signature64)}\n')

    message_signature = message64_string + '\n'

    # cria arquivo com mensagem em base64 e assinatura
    file_sign = open(file_name + '_signed.txt',"w")
    file_sign.write(message_signature)
    file_sign.close()
    file_sign = open(file_name + '_signed.txt',"ab")
    file_sign.write(signature64)
    file_sign.close()

    #print(f'send = {send}\n')
    
    file.close()

def Verify_signature():
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

    #print(f'message = {message64_string}\n')

    # message convertida da base64 para utf-8
    message64_bytes = file_lines[0].encode("utf-8")
    message_utf8 = base64.b64decode(message64_bytes)
    message = message_utf8.decode("utf-8")
    #print(f'message = {message}\n')

    # SHA-3
    message_hash = int.from_bytes(sha512(message_utf8).digest(), 'big')
    #print(f'message_hash verify = {message_hash}\n')
    """
    a parte de cima esta certa
    """

    signature = file_lines[1]
    print(f'signature = {signature}\n')
    print(f'signature type = {type(signature)}\n')

    # assinatura convertida da base64 para int
    signature64 = signature.encode("utf-8")
    signature_bytes = base64.b64decode(bytes(signature64))
    print(f'signature_bytes verify = {signature_bytes}\n')
    recovered_signature = int.from_bytes(signature_bytes, 'big')
    print(f'recovered_signature = {recovered_signature}\n')

    possible_message_hash = RSA(recovered_signature, pk)
    #print(f'possible_message_hash = {possible_message_hash}\n')

    if message_hash == possible_message_hash:
        print(f'Assinatura verificada\nMensagem: {message}')
    else:
        print(f'Verificação inválida\n')


    file_sign.close()