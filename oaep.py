"""
cifracao/decifracao - OAEP
"""

"""
Encryption
    1)  padding of message m, generating M
    2)  generates random number r (k-bits)
    2)  G function that transforms k-bits to m-bits (masking)
    3)  H function that transforms m-bits to k-bits (masking)
    4)  P = P1 || P2
        P1 = M xor G(r)
        P2 = H(P1) xor r
    5)  apply RSA on P

Decryption
    1)  apply RSA on ciphered message C
    2)  r = P2 xor H(P1)
    3)  M = P1 xor G(r)
    4) unpadding of M, generting m (original message)

"""

message = input('INSIRA MENSAGEM QUE DESEJA CIFRAR: ')

"""
get message
transform message to numeric version (ex: exemplo = [101, 120, 101, 109, 112, 108, 111] => 101120101109112108111)
"""

# convert message to binary
message_num = []
for m in message:
    message_num.append(ord(m))

# padding of message
# TODO: what is the size of m, how much should I padd?
message_len =  message_num
padding_size = M_BITS - message_len

print(f'padding_size = {padding_size}')

#M = int(message_bin)
M = message_bin

for i in range(padding_size):
    M += chr(random.randrange(48, 50))   # 0 or 1

print(f'M = {M}')

# generating random k-bits number r
r = Random_number(K_BITS)

print(f'r = {r}')

# TODO: G and H?


M_xor_r = xor(M,'0110')

print(f'M_xor_r = {M_xor_r}')