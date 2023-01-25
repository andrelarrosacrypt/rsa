"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

from generator import Generator
from constants import KEY_SIZE
"""
gerar chave
"""
# gerar p e q de tamanho 512 para ter p*q com tamanho 1024
p = Generator(KEY_SIZE)
print(f'p = {p}')

"""
cifracao/decifracao
"""

"""
assinatura
"""

"""
verificacao
"""