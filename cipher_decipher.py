def Cipher_decipher(x, key):
    """
    RSA cipher/decipher
    """
    return pow(x, key[0], key[1])
