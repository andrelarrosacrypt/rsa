"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

from generator import Generator
from constants import KEY_SIZE
import random
"""
gerar chave
"""

def Find_d(phi_n, e):
    for d in range(100):    # TODO: range(?)
        if (d*e)%phi_n == 1:
            return d
    return -1


# gerar p e q de tamanho 512 para ter p*q com tamanho 1024
p = Generator(KEY_SIZE)
print(f'p = {p}')
q = Generator(KEY_SIZE)
print(f'q = {q}')

"""
    n = p*q
    phi(n) = (p-1)*(q-1)
    1 < e < phi(n)

    lock = (e, n)

    d such that d*e (mod phi(n)) = 1

    key = (d, n)
"""

n = p*q
phi_n = (p-1)*(q-1)

while(True):
    e = random.randrange(2, phi_n-1)
    d = Find_d(phi_n, e)

    if d != -1:
        break

public_key = (e, n)
private_key = (d, n)

print(f'public_key (e,n) = {public_key}')
print(f'private_key (d,n) = {private_key}')

"""
cifracao/decifracao
"""

"""
assinatura
"""

"""
verificacao
"""