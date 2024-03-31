import base64
import sys
sys.path.append("../")
from functions import read_base64_file
from Crypto.Cipher import AES
from Crypto.Util import Padding
key = b"YELLOW SUBMARINE"
clean_text = read_base64_file("./7.txt")
cipher = AES.new(key, AES.MODE_ECB)
print(Padding.unpad(cipher.decrypt(clean_text),len(key)))