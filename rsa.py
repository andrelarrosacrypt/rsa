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
from cipher_decipher import Cipher_decipher
from constants import M_BITS, K_BITS
import random
from operator import xor
from hashlib import sha512

"""
gerar chave
"""
#public_key, private_key = ((5,14),(11,14))
#public_key, private_key = ((313,784319),(160009,784319))
public_key, private_key = Keys()
print(f'\npublic key = {public_key}')
print(f'\nprivate key = {private_key}')


"""
cifracao/decifracao - RSA
"""
message = input('\nESCREVA MENSAGEM: ')

message_code = []

for char in message:
    message_code.append(ord(char))

print(f'\nMENSAGEM CODIGO: {message_code}')

ciphered_message_text = ''
ciphered_message_code = []
for char in message:
    c = Cipher_decipher(ord(char), public_key)
    ciphered_message_text += chr(c)
    ciphered_message_code.append(c)
print(f'\nMENSAGEM CIFRADA TEXTO: {ciphered_message_text}')
print(f'\nMENSAGEM CIFRADA CODIGO: {ciphered_message_code}')


deciphered_message_text = ''
deciphered_message_code = []
for char in ciphered_message_text:
    d = Cipher_decipher(ord(char), private_key)
    deciphered_message_text += chr(d)
    deciphered_message_code.append(d)
print(f'\nMENSAGEM DECIFRADA: {deciphered_message_text}')
print(f'\nMENSAGEM DECIFRADA CODIGO: {deciphered_message_code}')


"""
assinatura
"""
# #msg = message.encode(encoding = 'UTF-8', errors = 'strict')
# #message = 'teste'.encode(encoding = 'UTF-8', errors = 'strict')
# message = 10
# print(f'message =  {message}\n')

# #message_digest_1 = int.from_bytes(sha512(message).digest(), byteorder='big')
# # print(f'message_digest_1: {message_digest_1}')
# # print(f'message_digest_1 type: {type(message_digest_1)}\n')

# #digital_signature = Cipher_decipher(message_digest_1, private_key)
# digital_signature = Cipher_decipher(message, private_key)
# print(f'digital_signature: {digital_signature}')
# print(f'digital_signature type: {type(digital_signature)}\n')

#send = (message, digital_signature)

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