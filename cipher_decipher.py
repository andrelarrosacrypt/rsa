def Cipher_decipher(char, key):
    """
    RSA cipher/decipher
    """
    return chr(pow(ord(char), key[0], key[1]))
