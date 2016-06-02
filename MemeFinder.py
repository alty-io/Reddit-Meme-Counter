'''
This is the main program.
'''

import nltk
from GetComments import getComments
from ListParser import listParser

memeHash = dict(listParser("memes.csv"))
memeCount = dict()

while 1:
    raw_comments = list(getComments())

    for comment in raw_comments:
        for word in nltk.word_tokenize(comment):
            if word in memeHash:
                for phrase in memeHash[word]:
                    if phrase in comment:
                        if phrase in memeCount:
                            memeCount[phrase] += 1
                        else:
                            memeCount[phrase] = 1
