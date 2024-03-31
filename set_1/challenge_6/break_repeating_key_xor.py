import numpy as np
import base64
import sys
import pprint
sys.path.append("../")
from functions import get_best_result
from functions import read_base64_file
def hamming2(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
hamming_distance = hamming2(''.join(format(ord(i), '08b') for i in 'this is a test'),''.join(format(ord(i), '08b') for i in 'wokka wokka!!!'))
print("hamming_distance for 'this is a test' and 'wokka wokka!!!' is:")
print(hamming_distance)
whole_content = read_base64_file("./6.txt")
results = {}
smallest_key = None
smallest = float('inf')
for i in range(39):
    all_current_hamming_distances = []
    has_index = True
    current_index_to_check = 0
    current_key_size = (i + 2)
    while  True:
        first_index_to_check_start = current_index_to_check
        first_index_to_check_end = (current_index_to_check + current_key_size)
        second_index_to_check_start = (current_index_to_check + current_key_size)
        second_index_to_check_end = (current_index_to_check + current_key_size) + current_key_size
        current_index_to_check += (current_key_size * 2)
        if second_index_to_check_end > len(whole_content):
            break
        all_current_hamming_distances.append(hamming2(''.join(format(j, '08b') for j in whole_content[first_index_to_check_start:first_index_to_check_end]) ,''.join(format(j, '08b') for j in whole_content[second_index_to_check_start:second_index_to_check_end])) / current_key_size)
    results[current_key_size] = np.sum(all_current_hamming_distances) / len(all_current_hamming_distances)
    if(results[current_key_size]) < smallest:
        smallest = results[current_key_size]
        smallest_key = current_key_size
chunks = [whole_content[i:i+smallest_key] for i in range(0, len(whole_content), smallest_key)]
first_elem_length = len(chunks[0])
last_elem_index = len(chunks) - 1
if len(chunks[last_elem_index]) != first_elem_length:
    chunks[len(chunks) - 1] += b'1'
    while len(chunks[last_elem_index]) != first_elem_length :
        chunks[len(chunks) - 1] += b'0'
transposed_array = [bytearray([c[i] for c in chunks]) for i in range(first_elem_length)]
transposed_array_result = [get_best_result(t) for t in transposed_array]
print("possible key is:")
print(''.join([r["letter"] for r in transposed_array_result]))