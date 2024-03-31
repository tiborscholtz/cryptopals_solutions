import binascii
import pprint
import sys
sys.path.append("../")
from functions import get_best_result
arr_data = [get_best_result(binascii.unhexlify(x.strip())) for x in open("./4.txt").readlines()]
max_elem = {"value":0}
for i in arr_data:
    max_elem = i if i["value"] > max_elem["value"] else max_elem
pprint.pprint(str(max_elem["text"],"utf-8").strip())