"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
imports
"""
import random
import math
from constants import N


def Generator(size):
    possible_prime = Random_number(size)
    #print(f'n random = {possible_prime}')
    Miller_Rabin_Primality_Test(possible_prime)

"""
selecione um numero aleatorio de tamanho size
"""
def Random_number(size):
    #random.randrange(pow(2,n-1)+1, pow(2,n)-1)
    return random.randrange(2**(size-1)+1, 2**size - 1)


# n = Random_number, possivel primo
# 1) encontre k e m, tal que n-1 = 2^k * m
# 2) escolha aleatoriamente a: 1 < a < n-1
# 3) b0 = a^m mod n, b(i) = b(i-1)^2
    # b0 = +1 ou -1 => n eh provavelmente primo
    # b(i) = +1 => composto, b(i) = -1 => provavelmente primo, i>0

# realize o teste varias vezes (ex: 20)

"""
Miller Rabin Primality Test
"""
def Miller_Rabin_Primality_Test(possible_prime):
    m = Miller_Rabin_Primality_Test_step1(possible_prime)
    #print(f'm final = {m}')
    a = Miller_Rabin_Primality_Test_step2(possible_prime)
    #print(f'a = {a}')

    if Miller_Rabin_Primality_Test_step3(a, m, possible_prime):
        # possible_prime is [probably] prime
        return possible_prime
    else:
        # possible_prime is not prime (it is composite)
        Generator(10) # restart the process
        #print(f'nao eh primo')

"""
Miller Rabin Primality Test step 1: find k and m such that n-1 = 2^k * m
"""
def Miller_Rabin_Primality_Test_step1(possible_prime):
    old_m = 0
    k = 1
    while(k < 10):
        #print(f'k = {k}')
        # divided by 2
        m = (possible_prime-1)/pow(2,k) # 2**k
        #print(f'm = {m}')
        k += 1

        if not m.is_integer():
            """
            o que fazer quando nao posso nem fazer a primeira divisao? quando old_m = 0
            """
            m = old_m
            return m

        # save possible m value
        old_m = m

"""
Miller Rabin Primality Test step 2: randomly choose a such that 1 < a < n-1
"""
def Miller_Rabin_Primality_Test_step2(possible_prime):
    return random.randrange(2, possible_prime - 2)


"""
Miller Rabin Primality Test step 3:
    1)  b0 = a^m (mod n)
        if b0 = +1 or -1 => n is probably prime
    2)  b(i) = b(i-1)^2 (mod n), i>0
        if b(i) = +1 => composite
        if b(i) = -1 => probably prime

    obs: a%b = -1 = b-1

"""
def Miller_Rabin_Primality_Test_step3(a, m, possible_prime):
    b0 = (a**m)%possible_prime
    print(f'b0 = {b0}')
    if b0 == 1 or b0 == -1:
        return True

    old_b = b0
    #while(True):
    for i in range(3):
        b = (old_b**2)%possible_prime

        #print(f'b = {b}')

        if b == 1:
            return False
        if b == possible_prime-1:
            return True
            
        old_b = b
        """
        pode entrar em loop infinito, tenho que definir um limite de iteracoes
        """
