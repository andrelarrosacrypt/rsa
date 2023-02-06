def Cipher_decipher(x, key):
    """
    RSA cipher/decipher
    """
    return pow(x, key[0], key[1])
    #return chr(pow(ord(x), key[0], key[1]))
