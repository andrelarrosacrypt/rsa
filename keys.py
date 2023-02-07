"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
import
"""
import random
from constants import ITERATIONS, MAX_MRPT, SIZE
import math


def Keys():
    """
    Gera as chaves pública e privada
    """

    # p, q
    while(True):
        p = Prime()
        q = Prime()   

        if p != q:
            break

    # n
    n = p*q

    # phi(n)
    phi_n = (p-1)*(q-1)

    # e, d
    while(True):
        e = random.randrange(2, phi_n-1)
        d = -1

        if math.gcd(e, phi_n) == 1:
            d  = pow(e, -1, phi_n)

        if d != -1 and d != 1 and e != d:
            break
    
    # chave pública: (e,n)
    # chave privada: (d,n) 
    return ((e,n), (d,n))

def Prime():
    """
    Gera um número (provavelmente) primo de acordo com o Teste de Primalidade Miller-Rabin
    """

    # Miller_Rabin_Primality_Test(Random_number(size))
    while(True):
        flag_composite = False
        possible_prime = Random_number(SIZE)
        
        for _ in range(ITERATIONS):
            if not Miller_Rabin_Primality_Test(possible_prime):
                # número é composto
                flag_composite = True
                break

        if not flag_composite:
            # número é primo
            return possible_prime

def Random_number(size):
    """
    Escolhe aleatoriamente um número de tamnaho 'size'
    """

    return random.getrandbits(size)

def Miller_Rabin_Primality_Test(possible_prime):
    """
    Teste de Primalidade Miller-Rabin
    Verifica se um número é (provavelmente) primo
    """

    if possible_prime%2 == 0:
        # número par é composto
        return False
        
    m = Miller_Rabin_Primality_Test_step1(possible_prime)
    a = Miller_Rabin_Primality_Test_step2(possible_prime)

    if Miller_Rabin_Primality_Test_step3(a, m, possible_prime):
        # número é primo
        return True
    else:
        # número é composto
        return False

def Miller_Rabin_Primality_Test_step1(possible_prime):
    """
    Miller Rabin Primality Test step 1: encontre 'k' e 'm' tal que 'n-1 = 2^k * m'
    """

    m = possible_prime - 1
    while(m%2 == 0):
        # como 'possible_prime' é ímpar, 'm' é par, logo pode ser dividido por 2 ao menos uma vez 
        m = m >> 1

    return m

def Miller_Rabin_Primality_Test_step2(possible_prime):
    """
    Miller Rabin Primality Test step 2: escolha um número 'a' tal que '1 < a < n-1'
    """

    return random.randrange(2, possible_prime - 2)

def Miller_Rabin_Primality_Test_step3(a, m, possible_prime):
    """
    Miller Rabin Primality Test step 3:
        1)  b0 = a^m (mod n)
            se b0 = +1 or -1 => n é (provavelmente) primo
        2)  b(i) = b(i-1)^2 (mod n), i>0
            se b(i) = +1 => n é composto
            se b(i) = -1 => n é (provavelmente) primo

        obs: a%b = -1 = b-1
    """

    b0 = pow(int(a), int(m), possible_prime)

    if (b0 == 1 or b0 == possible_prime - 1):
        # número é primo
        return True

    old_b = b0

    for _ in range(MAX_MRPT):
        b = pow(old_b, 2, possible_prime)

        if b == 1:
            # número é composto
            return False
        if b == possible_prime - 1:
            # número é primo
            return True
            
        old_b = b

    # número é composto
    return False