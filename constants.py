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
PRECISION = 1000000000
# alphabet size
ALPHABET_LEN = 26
# number of iterations of the Miller Rabin Primality Test
ITERATIONS = 10
# max amount of iteration for the third step of the Miller Rabin Primality Test
MAX_MRPT = 100