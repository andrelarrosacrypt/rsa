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
from constants import PRECISION, ITERATIONS, MAX_MRPT
import decimal


def Keys(size):
    """
    Generates public and private keys
    """
    # p and q
    while(True):
        p = Prime(size)
        q = Prime(size)

        if p != q:
            break

    # n
    n = p*q

    # phi(n)
    phi_n = (p-1)*(q-1)

    # e and d
    while(True):
        e = random.randrange(2, phi_n-1)
        gcd = Gcd(e, phi_n)
        d = Find_d(phi_n, e)

        # TODO: why? g = gcd(e, phi)

        if d != -1 and gcd == 1 and e != d:
            break   # TODO: end program, failed to find d
    
    return ((e,n), (d,n))

def Find_d(phi_n, e):
    # TODO: always selecting the first d, the lowest. Thats a problem
    for d in range(100):    # TODO: range(?)
        if (d*e)%phi_n == 1:
            return d
    return -1

def Gcd(a, b):
    """
    Greatest common divisor (Euclidean algorithm)
    """
    if b == 0:
        return a
    
    return Gcd(b, a%b)

def Prime(size):
    # Miller_Rabin_Primality_Test(Random_number(size))
    while(True):
        flag_composite = False
        possible_prime = Random_number(size)
        
        for i in range(ITERATIONS):
            if not Miller_Rabin_Primality_Test(possible_prime):
                # number is composite
                flag_composite = True
                break

        if not flag_composite:
            # number is prime
            return possible_prime

def Random_number(size):
    """
    Picks a random number with specific size 
    """
    return random.randrange(2**(size-1)+1, 2**size - 1)

def Miller_Rabin_Primality_Test(possible_prime):
    """
    Miller Rabin Primality Test
    Verifies if a number is probably prime
    """
    if possible_prime%2 == 0:
        # even number (composite)
        return False
        
    m = Miller_Rabin_Primality_Test_step1(possible_prime)
    a = Miller_Rabin_Primality_Test_step2(possible_prime)

    if Miller_Rabin_Primality_Test_step3(a, m, possible_prime):
        # number is prime
        return True
    else:
        # number is composite
        return False

def Miller_Rabin_Primality_Test_step1(possible_prime):
    """
    Miller Rabin Primality Test step 1: find [k] and [m] such that [n-1 = 2^k * m]
    """
    old_m = 0
    k = 1
    while(True):
        # divide by 2
        # possible_prime - 1 is even (possible_prime is odd), then we can divide it by a power of 2 at least once
        m = (possible_prime-1)/2**k
        
        if not m.is_integer():        
            m = old_m
            return m

        # save possible m value
        old_m = m
        # increases the power of 2
        k += 1

def Miller_Rabin_Primality_Test_step2(possible_prime):
    """
    Miller Rabin Primality Test step 2: choose a number [a] such that [1 < a < n-1]
    """
    return random.randrange(2, possible_prime - 2)

def Miller_Rabin_Primality_Test_step3(a, m, possible_prime):
    """
    Miller Rabin Primality Test step 3:
        1)  b0 = a^m (mod n)
            if b0 = +1 or -1 => n is probably prime
        2)  b(i) = b(i-1)^2 (mod n), i>0
            if b(i) = +1 => composite
            if b(i) = -1 => probably prime

        obs: a%b = -1 = b-1
    """
    decimal.getcontext().prec = PRECISION
    
    b0 = (decimal.Decimal(a)**decimal.Decimal(m))%decimal.Decimal(possible_prime)

    if (b0 == 1 or b0 == -1):
        # number is prime
        return True

    old_b = b0

    for i in range(MAX_MRPT):
        b = (old_b**2)%possible_prime

        if b == 1:
            # number is composite
            return False
        if b == possible_prime-1:
            # number is prime
            return True
            
        old_b = b

    # number is composite
    return False