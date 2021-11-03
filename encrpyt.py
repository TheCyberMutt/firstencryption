import random
from string import ascii_lowercase

sample_wordlist = ["terces", "twosix", "yofour"]
length = len(sample_wordlist)
sample_input = "secret"

step = random.randint(1, length - 1)

code_word = sample_wordlist[step]

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return numbers


input_word_as_number = alphabet_position(sample_input)
code_word_as_number = alphabet_position(code_word)

print(input_word_as_number)
print(code_word_as_number)



