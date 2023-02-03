"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
constantes
"""

# key (p and q) size
# TODO: decimal.Overflow: [<class 'decimal.Overflow'>]. How to handle large numbers?
SIZE = 1024
# decimal precision
PRECISION = 1000000000000000000
# alphabet size
ALPHABET_LEN = 26
# number of iterations of the Miller Rabin Primality Test
ITERATIONS = 40
# max amount of iteration for the third step of the Miller Rabin Primality Test
MAX_MRPT = 100
# OAEP: message size after padding
M_BITS = 1000
# OAEP: random k-bits number
K_BITS = 500