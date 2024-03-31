You can find the challenge description here:

https://cryptopals.com/sets/1/challenges/2

Solution details:

The two base strings are in hexadecimal format.

We can convert them to bytes, using the `bytes.fromhex` function. After that, using the `strxor` function from `Crypto.Util.strxor`, we get the XOR'd value, but we need to display it in hexadecimal format. For that, we can use `binascii.hexlify`.

You can read more about XOR here: [https://en.wikipedia.org/wiki/Exclusive_or]