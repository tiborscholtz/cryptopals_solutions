You can find the challenge description here:

https://cryptopals.com/sets/1/challenges/6

Solution details:

It is one of the hardest challange in set 1. So, let's walk through step by step. I'm going to paste the corresponding code part to each step the website states:  

**Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.**

For that, we are going to iterate through 0 to 39.

```python
for i in range(39):
```

**Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:**

`this is a test`  

and  

`wokka wokka!!!`  

is **37**. Make sure your code agrees before you proceed.

Some mentionable parts of the code:

`format(ord(i), '08b')` means, that if the text is shorter than 8 characters, it will be padded with zeros to the left, until it reaches the width of 8 characters.  

`assert len(s1) == len(s2)` means, that we make sure that the length of the two texts are equal.  

`sum(c1 != c2 for c1, c2 in zip(s1, s2))`  The `zip` function takes two iterables (s1 and s2) and pairs up their elements element-wise. The `sum` function sums up the values yielded by the generator expression, which can return 1 or 0. The generator expression returns 1(True) if the elements are different, or returns 0(False), if they are not.


```python
def hamming2(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
hamming_distance = hamming2(''.join(format(ord(i), '08b') for i in 'this is a test'),''.join(format(ord(i), '08b') for i in 'wokka wokka!!!'))
print("hamming_distance for 'this is a test' and 'wokka wokka!!!' is:")
print(hamming_distance)
```


**For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.**

```python
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
```

We check the following index pairs, for example:
- 0-30 and 30-60
- 60-90 and 90-120
- 120-150 and 150-180


Just to be safe, we check, if the end of the second part is bigger than the length of the whole text document, we break the process.  

**The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.**

```python
results[current_key_size] = np.sum(all_current_hamming_distances) / len(all_current_hamming_distances)
if(results[current_key_size]) < smallest:
    smallest = results[current_key_size]
    smallest_key = current_key_size
```

As the description says, we check the current edit distance, and if it is smaller than our previously saved one, it will be our possible key.

**Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.**  

```python
chunks = [whole_content[i:i+smallest_key] for i in range(0, len(whole_content), smallest_key)]
first_elem_length = len(chunks[0])
last_elem_index = len(chunks) - 1
if len(chunks[last_elem_index]) != first_elem_length:
    chunks[len(chunks) - 1] += b'1'
    while len(chunks[last_elem_index]) != first_elem_length :
        chunks[len(chunks) - 1] += b'0'
```

**Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.**

```python
transposed_array = [bytearray([c[i] for c in chunks]) for i in range(first_elem_length)]
```

**Solve each block as if it was single-character XOR. You already have code to do this.**

```python
transposed_array_result = [get_best_result(t) for t in transposed_array]
```

**For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.**

```python
print("possible key is:")
print(''.join([r["letter"] for r in transposed_array_result]))
```