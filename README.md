"# firstencryption" 

The encryption takes a word from the user input and compares it to a word of equal length from a wordlist. The algorithm is designed to have multiple wordlists where each wordlist only has words of equal lengths.

For example:
car -> part of wordlist with ["bar", "jim", "toe"]
rocket -> part of wordlist with ["robots", "doggie", "toejam"]

A random number generator is used to pick word from the wordlist based on placement on list. This number is added to a list that is going to be used to decode the message. 
The scrypt here will have a sample list to test the code, but you can use a random string generator on a foor loop to create the list(s). 

After word from wordlist is selected for comparison, the word and user input are broken up into individual characters and converted to numbers that represent their placement in the alphabet.

A -> 1
a -> 1
B -> 2
b -> 2
C -> 3
c -> 3
...
...

Next, the algorithm runs a function that either subtracts or adds the numbers that correspond to the same position of the words being compared depending on their sum.
The resulting numbers are then converted back to letters and joined to become a new word!

For example:

Given

wordlist = ["loki", "axyz", "crack", "this", "code"]

And

user_input = "abcd"

random_number_generated = 2

Leads

"abcd" = ["a", "b", "c", "d"] -> [ 1, 2, 3, 4]

"axyz" = ["a", "x", "y", "z"] -> [1, 24, 25, 26]

Result

[1 + 1, 2 + 24, |3 - 25|, |4 - 26|] -> [2, 26, 22, 22] = ["b", "z", "v", "v"] -> ["bzvv"]



