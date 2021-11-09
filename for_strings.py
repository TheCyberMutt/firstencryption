import random

import encrpyt
import wordlists

user_string = input("Enter your secret message: ")

user_wordlist = user_string.split()


print(user_wordlist)

step_list = []


def string_encrypt(user_input_wordlist):
    encrypted_string = []
    for word in user_input_wordlist:
        if len(word) == 1:
            length = len(wordlists.wordlist1)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist1[step]))

        elif len(word) == 2:
            length = len(wordlists.wordlist2)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist2[step]))

        elif len(word) == 3:
            length = len(wordlists.wordlist3)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist3[step]))

        elif len(word) == 4:
            length = len(wordlists.wordlist4)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist4[step]))

        elif len(word) == 5:
            length = len(wordlists.wordlist5)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist5[step]))

        elif len(word) == 6:
            length = len(wordlists.wordlist6)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist6[step]))

        elif len(word) == 7:
            length = len(wordlists.wordlist7)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist7[step]))

        elif len(word) == 8:
            length = len(wordlists.wordlist8)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist8[step]))

        elif len(word) == 9:
            length = len(wordlists.wordlist9)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist9[step]))

        elif len(word) == 10:
            length = len(wordlists.wordlist10)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist10[step]))

        elif len(word) == 11:
            length = len(wordlists.wordlist11)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist11[step]))

        elif len(word) == 12:
            length = len(wordlists.wordlist12)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist12[step]))

        elif len(word) == 13:
            length = len(wordlists.wordlist13)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist13[step]))

        elif len(word) == 14:
            length = len(wordlists.wordlist14)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist14[step]))

        elif len(word) == 15:
            length = len(wordlists.wordlist15)
            step = random.randint(1, length - 1)
            step_list.append(step)
            encrypted_string.append(encrpyt.word_generator(word, wordlists.wordlist15[step]))

    print(encrypted_string)


string_encrypt(user_wordlist)
print(step_list)