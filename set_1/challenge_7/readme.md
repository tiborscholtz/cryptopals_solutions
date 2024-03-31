You can find the challenge description here:

https://cryptopals.com/sets/1/challenges/7

Solution details:

The rules are the following:

- The content of `7.txt` file has been encrypted:
    - AES-128[https://hu.wikipedia.org/wiki/Advanced_Encryption_Standard]
    - ECB mode[https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)]
    - with the key "YELLOW SUBMARINE"

We store the key in a variable, like:

```python
key = b"YELLOW SUBMARINE"
```

After that, we create a cipher, using the following code:

```python
cipher = AES.new(key, AES.MODE_ECB)
```

Finally, we can decrypt the data, using the created `cipher` instance:

```python
Padding.unpad(cipher.decrypt(clean_text),len(key))
```

If you leave out the `Padding.unpad` option, the text is still decrypted, but some padding will be left in the end of the text.