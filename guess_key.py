from utils_demo import *

for i in range(1,4):
    message=read_file("m"+str(1)+".txt")
    cipher=read_bytes("c"+str(1)+".bin")
    nonce=read_bytes("nonce"+str(1)+".bin")
    key=bin(2 ** 127)
    foundkey=False
    count =0
    # print(bitstring_to_bytes(key))
    while foundkey==False:
        # print(decryptor_CTR(cipher,nonce,key))
        # print(message)
        # print(hex(int(key,2)))
        if decryptor_CTR(cipher,nonce,bitstring_to_bytes(key)) == string_to_bytes(message):
            print(decryptor_CTR(cipher,nonce,bitstring_to_bytes(key)))
            print(message)
            foundkey =True
            print(hex(int(key,2)))
        else:
            key=bin(int(key,2)+1)

