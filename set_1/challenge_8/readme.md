You can find the challenge description here:

https://cryptopals.com/sets/1/challenges/8

Solution details:

First, we read the file, using the following code:

```python
b64_file = open("./8.txt","r")
```

We use list comprehension, to clean and decode the lines in the text file:

```python
b64_decoded_text_decoded = ([base64.b64decode(x.strip()) for x in b64_file.readlines()])
```

The `readlines()` function returns an array. In this array, we `strip()` every element from any possible whitespaces, and use `base64.b64decode` to convert the text back to its original form. After that, we have a list of base64 decoded texts.

We can find out which text is encrypted with ECB, by searching for repetitve parts inside the lines. For that, we need to get the multiples of 16, since ECB uses a multiple of 16 to encrypt the data.

```python
multiples_of_sixteen = [((item + 1) * 16) for item in range(10)]
print(multiples_of_sixteen)
[16, 32, 48, 64, 80, 96, 112, 128, 144, 160]
```

After that, we need two for loops: one, for each line inside the text file, and one, to check each multple of sixteen.

```python
for elem in b64_decoded_text_decoded:
    for i in multiples_of_sixteen:
```

The `current_list = list(list_chunks(elem,i))` line cuts each lines to 16,32,48 length parts, based on what is the current value of i.  
Inside this list, we can check for equals elements, using `set(current_list)`. If we find equal elements, it means that there is a repeating pattern in the text, and the ECB method created an equal encryption for these two texts.

