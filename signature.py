import base64
from hashlib import sha512
from rsa import RSA
import sys

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
    message64_bytes = base64.b64encode(message_utf8)
    message64_string = message64_bytes.decode("utf-8")

    # print(f'message64_string  = {message64_string}\n')
    # print(f'message_utf8  = {message_utf8}\n')

    # SHA-3
    message_hash = int.from_bytes(sha512(message_utf8).digest(), 'big')

    # assinatura
    signature = RSA(message_hash, pk)

    # assinatura convertida para base64
    signature_bytes = signature.to_bytes(sys.getsizeof(signature),'big')
    signature64 = base64.b64encode(signature_bytes)

    #print(f'signature64  = {signature64}\n')

    message_signature = message64_string + '\n' + str(signature64)

    # cria arquivo com mensagem em base64 e assinatura
    file_sign = open(file_name + '_signed.txt',"w")
    file_sign.write(message_signature)
    file_sign.close()

    #print(f'send = {send}\n')
    
    file.close()

def Verify_signature():
    # message convertida da base64 para utf-8
    message64_bytes2 = send[0].encode("utf-8")
    message_bytes = base64.b64decode(message64_bytes2)
    message_utf82 = message_bytes.decode("utf-8")
    print(f'message_utf82 = {message_utf82}\n')

    message_hash_2 = int.from_bytes(sha512(message_utf82.encode()).digest(), 'big')
    print(f'message_hash_2 = {message_hash_2}\n')

    # assinatura convertida da base64 para int
    signature_bytes2 = base64.b64decode(signature64)
    print(f'signature_bytes2 = {signature_bytes2}\n')
    signature_recovered = int.from_bytes(signature_bytes2, 'big')
    print(f'signature_recovered = {signature_recovered}\n')

    possible_message_hash = Cipher_decipher(signature_recovered, public_key)
    print(f'possible_message_hash = {possible_message_hash}\n')
