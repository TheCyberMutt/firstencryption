import random

import encrpyt
import wordlists

user_string = input("Enter your secret message: ")

user_wordlist = user_string.split()

print(user_wordlist)

step_list = []

encrypted_string = []


def string_encrypt(user_input_wordlist):
    for word in user_input_wordlist:
        if len(word) == 1:
            length = len(wordlists.wordlist1)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist1[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 2:
            length = len(wordlists.wordlist2)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist2[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 3:
            length = len(wordlists.wordlist3)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist3[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 4:
            length = len(wordlists.wordlist4)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist4[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 5:
            length = len(wordlists.wordlist5)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist5[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 6:
            length = len(wordlists.wordlist6)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist6[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 7:
            length = len(wordlists.wordlist7)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist7[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 8:
            length = len(wordlists.wordlist8)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist8[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 9:
            length = len(wordlists.wordlist9)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist9[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 10:
            length = len(wordlists.wordlist10)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist10[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 11:
            length = len(wordlists.wordlist11)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist11[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 12:
            length = len(wordlists.wordlist12)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist12[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 13:
            length = len(wordlists.wordlist13)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist13[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 14:
            length = len(wordlists.wordlist14)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist14[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))

        elif len(word) == 15:
            length = len(wordlists.wordlist15)
            step = random.randint(1, length - 1)
            step_list.append(step)
            num_word = encrpyt.alphabet_position(word)
            num_code_word = encrpyt.alphabet_position(wordlists.wordlist15[step])
            encrypted_string.append(encrpyt.word_generator(num_word, num_code_word))


string_encrypt(user_wordlist)

print(step_list)
print(encrypted_string)

the_string = ' '.join(encrypted_string)
print(the_string)