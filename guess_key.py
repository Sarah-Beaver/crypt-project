from utils_demo import *

message1=read_file("m1.txt")
cipher1=read_bytes("c1.bin")
nonce1=read_bytes("nonce1.bin")
message2=read_file("m2.txt")
cipher2=read_bytes("c2.bin")
nonce2=read_bytes("nonce2.bin")
message3=read_file("m3.txt")
cipher3=read_bytes("c3.bin")
nonce3=read_bytes("nonce3.bin")
# starting the key at 8000....0000
key=bin(2 ** 127)
foundkey=False
# checks if key has been found
while foundkey==False:
    # checks if decrypt of the key is equal to the messages in bytes for each cipher and noonce and prints key in hex 
    # otherwise increments key
    if decryptor_CTR(cipher1,nonce1,bitstring_to_bytes(key)) == string_to_bytes(message1):
        if decryptor_CTR(cipher2,nonce2,bitstring_to_bytes(key)) == string_to_bytes(message2) and decryptor_CTR(cipher3,nonce3,bitstring_to_bytes(key)) == string_to_bytes(message3):
            foundkey = True
            print(hex(int(key,2)))
    else:
        key=bin(int(key,2)+1)

