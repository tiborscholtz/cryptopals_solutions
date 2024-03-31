opening_stanza = "Burning 'em, if you ain't quick and nimble\n I go crazy when I hear a cymbal"
key = "ICE"
result = ""
import binascii
print(binascii.hexlify(bytes(''.join(([chr(ord(opening_stanza[i]) ^ ord(key[i%len(key)])) for i in range(len(opening_stanza))])),"utf-8")))