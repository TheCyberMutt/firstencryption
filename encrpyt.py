import random
from string import ascii_lowercase

sample_wordlist = ["terces", "twosix", "yofour"]
length = len(sample_wordlist)
sample_input = "secret"

# Random number generated, stored and used to select word from wordlist
step = random.randint(1, length - 1)

code_word = sample_wordlist[step]

# Generates dictionary of lowercase letters with numbers that correspond to their placement on the American English
# Alphabet
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


# turns word into a set of numbers based on the LETTERS dictionary
def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return numbers


input_word_as_number = alphabet_position(sample_input)
code_word_as_number = alphabet_position(code_word)


# print(input_word_as_number)
# print(code_word_as_number)


# Uses number list of the user input and word from wordlist to calculate new number
def word_generator(user, code):
    generated_word = []
    for i in range(1, len(user) + 1):
        if (int(user[i - 1]) + int(code[i - 1])) > 26:
            val = abs(int(user[i - 1]) - int(code[i - 1]))
        else:
            val = int(user[i - 1]) + int(code[i - 1])

        generated_word.append(str(val))
    # New number is used to determine new word using LETTERS dictionary
    final_word = []
    for num in generated_word:

        for key, value in LETTERS.items():
            if num == value:
                final_word.append(key)
    final_word = ''.join(final_word)
    # This is the encrypted word
    return final_word

# print(LETTERS)
# print(word_generator(input_word_as_number, code_word_as_number))
