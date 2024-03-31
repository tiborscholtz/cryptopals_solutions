from Crypto.Util.strxor import strxor
import pprint
import base64
def get_best_result(string_to_check):
    FREQUENCY_TABLE = {
        'a':  0.08167,
        'b':  0.01492,
        'c':  0.02782,
        'd':  0.04253,
        ' ':  0.35,
        'e':  0.1270,
        'f':  0.02228,
        'g':  0.02015,
        'h':  0.06094,
        'i':  0.06966,
        'j':  0.00153,
        'k':  0.00772,
        'l':  0.04025,
        'm':  0.02406,
        'n':  0.06749,
        'o':  0.07507,
        'p':  0.01929,
        'q':  0.00095,
        'r':  0.05987,
        's':  0.06327,
        't':  0.09056,
        'u':  0.02758,
        'v':  0.00978,
        'w':  0.02360,
        'x':  0.00150,
        'y':  0.01974,
        'z':  0.00074,
    }
    ret_value = {}
    max_value = 0
    for i in range(256):
        current_character = chr(i)
        current_xor = strxor(string_to_check,bytes(i.to_bytes(1,byteorder='big') * len(string_to_check)))
        current_val = 0
        for c in current_xor:
            current_char = chr(c)
            if current_char in FREQUENCY_TABLE:
                current_val += FREQUENCY_TABLE[current_char]
        if max_value < current_val:
            ret_value = {"letter":current_character,"text":current_xor,"value":current_val}
            max_value = current_val
    return ret_value

def read_base64_file(file_path):
    file_object = open(file_path,"r")
    lines = file_object.readlines()
    clean_text = ""
    for l in lines:
        clean_line = l.strip()
        clean_text += clean_line
    clean_text = base64.b64decode(clean_text)
    file_object.close()
    return clean_text