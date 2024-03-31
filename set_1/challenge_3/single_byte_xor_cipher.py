import binascii
import pprint
import sys
sys.path.append("../")
from functions import get_best_result
pprint.pprint(str(get_best_result(binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))["text"],"utf-8"))