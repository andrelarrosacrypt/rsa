"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
imports
"""
from generator import Keys, Random_number
#from cipher_decipher import Cipher_decipher
from constants import M_BITS, K_BITS
import random
from operator import xor
from hashlib import sha512
import base64
import sys


"""
RSA
"""
def RSA(x, key):
    """
    RSA cipher/decipher
    """
    return pow(int(x), int(key[0]), int(key[1]))
    #return chr(pow(ord(x), key[0], key[1]))

"""
gerar chave
"""
#public_key, private_key = ((5,14),(11,14))
#public_key, private_key = ((313,784319),(160009,784319))
#public_key, private_key = Keys()
# print(f'\npublic key = (\ne = {public_key[0]}\nn = {public_key[1]}\n)')
# print(f'\nprivate key = (\nd = {private_key[0]}\nn = {private_key[1]}\n)')

#public_key, private_key = ((17,3233), (413, 3233))

"""
cifracao/decifracao - RSA
"""

"""

1) Cipher_decipher esta funcionando
2) p e q sao primos

d esta sendo gerado de maneira errada

e e phi_n precisam ser coprimos para podermos encontrar d

"""

# message = 15896327891625974526945156658
# print(f'message = {message}')

# ciphered_message = Cipher_decipher(message, public_key)
# print(f'\nciphered_message: {ciphered_message}')

# deciphered_message = Cipher_decipher(ciphered_message, private_key)
# print(f'\ndeciphered_message: {deciphered_message}')

# message_code = []

# for char in message:
#     message_code.append(ord(char))


"""
funcionando - comeco
"""
# file_name = input(f'DIGITE O NOME DO ARQUIVO: ')
# message = input(f'DIGITE A MENSAGEM: ')

# file = open(file_name + '.txt',"w")
# file.write(message)



# ciphered_message = []
# for char in message:
#     ciphered_message.append(Cipher_decipher(ord(char), public_key))
# print(f'\nMENSAGEM CIFRADA:\n{ciphered_message}')

# deciphered_message = ''
# deciphered_message_code = []
# for x in ciphered_message:
#     m = Cipher_decipher(x, private_key)
#     deciphered_message_code.append(m)
#     deciphered_message += chr(m)
# print(f'\nMENSAGEM DECIFRADA CODIGO:\n{deciphered_message_code}')
# print(f'\nMENSAGEM DECIFRADA TEXTO:\n{deciphered_message}')
"""
funcionando - fim
"""


# ciphered_message_text = ''
# for char in message:
#     c = Cipher_decipher(ord(char), public_key)
#     ciphered_message_text += chr(c)
# print(f'\nMENSAGEM CIFRADA TEXTO: {ciphered_message_text}')


# deciphered_message_text = ''
# # for char in ciphered_message_text:
# #     d = Cipher_decipher(ord(char), private_key)
# #     #deciphered_message_text += chr(d)
# #     deciphered_message_code.append(d)
# for c in ciphered_message_code:
#     d = Cipher_decipher(c, private_key)
# print(f'\nMENSAGEM DECIFRADA: {deciphered_message_text}')


"""
assinatura
sha3_512 - 64 bit Digest-Size

h = sha(m)
h2 = sha(h)

h != h2


hashlib eh OpenSSL?

"""

"""
assinatura verificacao - comeco
"""
# msg = message.encode()

# # message convertida para base64
# message_utf8 = message.encode("utf-8")
# message64_bytes = base64.b64encode(message_utf8)
# message64_string = message64_bytes.decode("utf-8")
# print(f'message64 = {message64_string}\n')

# message_hash = int.from_bytes(sha512(msg).digest(), 'big')
# print(f'message_hash = {message_hash}\n')

# # assinatura convertida para base64
# signature = Cipher_decipher(message_hash, private_key)
# print(f'signature = {signature}\n')
# signature_bytes = signature.to_bytes(sys.getsizeof(signature),'big')
# signature64 = base64.b64encode(signature_bytes)

# send = (message64_string, signature64)

# # message convertida da base64 para utf-8
# message64_bytes2 = send[0].encode("utf-8")
# message_bytes = base64.b64decode(message64_bytes2)
# message_utf82 = message_bytes.decode("utf-8")
# print(f'message_utf82 = {message_utf82}\n')

# message_hash_2 = int.from_bytes(sha512(message_utf82.encode()).digest(), 'big')
# print(f'message_hash_2 = {message_hash_2}\n')

# # assinatura convertida da base64 para int
# signature_bytes2 = base64.b64decode(signature64)
# print(f'signature_bytes2 = {signature_bytes2}\n')
# signature_recovered = int.from_bytes(signature_bytes2, 'big')
# print(f'signature_recovered = {signature_recovered}\n')

# possible_message_hash = Cipher_decipher(signature_recovered, public_key)
# print(f'possible_message_hash = {possible_message_hash}\n')

# if message_hash_2 == possible_message_hash:
#     print(f'TRUE\n')
#     print(f'message = {message_utf82}\n')
# else:
#     print(f'FALSE\n') 
"""
assinatura verificacao - fim
"""



"""
RSA esta funcionando
o que nao funciona é que, quando a mensagem 'm' é maior que 'n', m^d = x mod n (mensagem cifrada é x)
'x' é igual a 'm' modulo 'n', mas não é exatamente igual a 'm'
ex: message = 15 e n = 14
    então teremos 15 mod 14 = 1
    RSA esta entao trabalhando com 1 ao inves de 15
"""

"""
return hashlib.sha3_256(data).digest()
"""

# msg = 25
# print(f'msg = {msg}\n')

# print("--- PRIVATE TO PUBLIC ---\n")
# msg_encrypt = Cipher_decipher(msg, private_key)
# print(f'msg_encrypt = {msg_encrypt}')

# msg_decrypt = Cipher_decipher(msg_encrypt, public_key)
# print(f'msg_decrypt = {msg_decrypt}')

# print("--- PUBLIC TO PRIVATE ---\n")
# msg_encrypt = Cipher_decipher(msg, public_key)
# print(f'msg_encrypt = {msg_encrypt}')

# msg_decrypt = Cipher_decipher(msg_encrypt, private_key)
# print(f'msg_decrypt = {msg_decrypt}')

"""
verificacao
""" 

#receives = (message, digital_signature)

# send[0] = message
# message_digest_2 = int.from_bytes(sha512(send[0]).digest(), byteorder='big')
# print(f'message_digest_2: {message_digest_2}')    

# # send[1] = digital_signature
# possible_message_digest_1 = Cipher_decipher(send[1], public_key)
# print(f'possible_message_digest_1: {possible_message_digest_1}')

# if send[0] == possible_message_digest_1:
#     print(f'TRUE')
# else:
#     print(f'FALSE')

# RSA verify signature
# msg = b'A message for signing'
# hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
# hashFromSignature = pow(signature, public_key[0], public_key[1])
# print("Signature valid:", hash == hashFromSignature)