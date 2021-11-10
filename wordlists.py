import random
import string

wordlist1 = []
wordlist2 = []
wordlist3 = []
wordlist4 = []
wordlist5 = []
wordlist6 = []
wordlist7 = []
wordlist8 = []
wordlist9 = []
wordlist10 = []
wordlist11 = []
wordlist12 = []
wordlist13 = []
wordlist14 = []
wordlist15 = []


def wordlistgenerator(length, wordlist):
    for i in range(0, length):
        wordlist.append(''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(length)))

    return wordlist


wordlistgenerator(100, wordlist1)
wordlistgenerator(100, wordlist2)
wordlistgenerator(100, wordlist3)
wordlistgenerator(100, wordlist4)
wordlistgenerator(100, wordlist5)
wordlistgenerator(100, wordlist6)
wordlistgenerator(100, wordlist7)
wordlistgenerator(100, wordlist8)
wordlistgenerator(100, wordlist9)
wordlistgenerator(100, wordlist10)
wordlistgenerator(100, wordlist11)
wordlistgenerator(100, wordlist12)
wordlistgenerator(100, wordlist13)
wordlistgenerator(100, wordlist14)
wordlistgenerator(100, wordlist15)

# print(wordlist15)