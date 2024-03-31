You can find the challenge description here:

https://cryptopals.com/sets/1/challenges/3

Solution details:

This one is a bit challenging.

We need to find what is that single character that the task used to XOR the text.

The site mentions the following:' "scoring" a piece of English plaintext'. This simply means, that if we XOR the encoded string against each letter in the alphabet, the most "meaningful" (in english language) should be the best one. For that, we can utilize a character freuqency table, which is different for every language. But for now, we need only the english language's character freuency. The `get_best_result` function applies a scan for each possible letter, until it finds the one with the best score.