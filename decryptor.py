# Popescu Vasile
# Date 10/6/2021 2:16 PM
import string
from textwrap import wrap

def decryptor(msg):
    decrypted = []
    for char in msg:
        char = int(char,16)
        for n in range(256):
            if( ((256*n+char)-18) % 123 == 0):
                decrypted.append(chr( int( ((256*n+char)-18)/123 )  ))
                break
    return decrypted

f = open('./msg.enc','r+')
encoded = f.readline()
encoded = wrap(encoded,2)
f.seek(f.tell())
decrypted = "".join(decryptor(encoded))
f.write("Decrypted message:\n"+decrypted)
f.close()

#print("Decrypted message:\n"+decrypted)