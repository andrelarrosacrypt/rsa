"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

from generator import Keys
from constants import SIZE, ALPHABET_LEN
import random
from cipher_decipher import Cipher_decipher

#TODO: do I need SIZE here? Or can I only use it on the other files?

"""
gerar chave
"""

#public_key, private_key = ((5,14),(11,14))
public_key, private_key = Keys(SIZE)
print(f'publ and priv = {public_key, private_key}')

"""
cifracao/decifracao
"""
message = input('INSIRA MENSAGEM QUE DESEJA CIFRAR: ')

ciphered_message = ''
for char in message:
    ciphered_message += Cipher_decipher(char, public_key)
print(f'\nMENSAGEM CIFRADA:\n{ciphered_message}')

deciphered_message = ''
for char in ciphered_message:
    deciphered_message += Cipher_decipher(char, private_key)
print(f'\nMENSAGEM DECIFRADA:\n{deciphered_message}')







"""
assinatura
"""

"""
verificacao
"""