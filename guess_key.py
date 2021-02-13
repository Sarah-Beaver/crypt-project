from utils_demo import *
# loops through each set of messages, ciphers, and nonce
for i in range(1,4):
    message=read_file("m"+str(i)+".txt")
    cipher=read_bytes("c"+str(i)+".bin")
    nonce=read_bytes("nonce"+str(i)+".bin")
    # starting the key at 8000....0000
    key=bin(2 ** 127)
    foundkey=False
    # checks if key has been found
    while foundkey==False:
        # checks if decrypt of the key is equal to the message in bytes and prints key in hex 
        # otherwise increments key
        if decryptor_CTR(cipher,nonce,bitstring_to_bytes(key)) == string_to_bytes(message):
            foundkey = True
            print(hex(int(key,2)))
        else:
            key=bin(int(key,2)+1)

