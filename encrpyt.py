import random
from string import ascii_lowercase
from typing import List, Any

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


def word_generator(user, code):
    generated_word = []
    for i in range(1, len(sample_input) + 1):
        if int(user[i - 1]) + int(code[i - 1]) > 26:
            val = abs(int(user[i - 1]) - int(code[i - 1]))
        else:
            val = int(user[i - 1]) + int(code[i - 1])

        generated_word.append(str(val))

    final_word = []
    for num in generated_word:

        for key, value in LETTERS.items():
            if num == value:
                final_word.append(key)
    final_word = ''.join(final_word)

    return final_word


print(LETTERS)
print(word_generator(input_word_as_number, code_word_as_number))
