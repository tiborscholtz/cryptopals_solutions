You can find the challenge description here:

https://cryptopals.com/sets/1/challenges/5

Solution details:

Repeating-key XOR means, that you should continously encrypt the current letter of the text, with the current letter of the text you use as the XOR key.

For example, if the text is: "lorem ipsum dolor sit amet", and the key is "secret", the repeating-key xor should look the following:

| l | o | r | e | m |   | i | p | s| u | m |  | d | o | l | o |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| s | e | c | r | e | t | s | e | c | r | e | t | s | e | c | r |



It continues to apply the current letter of the key, if the text is longer than the key.

We define the text in a varible:

```python
opening_stanza = "Burning 'em, if you ain't quick and nimble\n I go crazy when I hear a cymbal"
```

We use list comprehesion in the code. It is a bit crowded at first sight, so let's break it down to pieces:

```python
[chr(ord(opening_stanza[i]) ^ ord(key[i%len(key)])) for i in range(len(opening_stanza))]
```

The `range(len(opening_stanza)` part gives us a list of numbers from 0 to the length of the variable `opening_stanza`.

```python
ord(opening_stanza[i]) ^ ord(key[i%len(key)])
```

This is where the actual xor happens.  

We XOR the current letter of the `opening_stanza` variable, with the currently available letter, for the `key` variable.  

The `key[i%len(key)]` should always procude `0`, `1`, or `2` as a result.