import codecs
from Crypto.Util.strxor import strxor
import binascii
print(binascii.hexlify(strxor(bytes.fromhex("1c0111001f010100061a024b53535009181c"), bytes.fromhex('686974207468652062756c6c277320657965'))))