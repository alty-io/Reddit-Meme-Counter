'''
This is the main program.

It takes a predefinied list of memes and hashes them into a real
language hashed list.

Then it uses GetComments to grab recent comments from reddit, and
compares the words in it against the keywords of the hash table.

If it finds a keyword in a comment, it then checks the phrases linked
to that keyword against the comment to see if the full phrase exists.

If a full phrase is found, it puts it into a dictionary with a counter,
and then updates a log file with total counts for each phrase found.

By Tyler Sullivan and Alex Hildreth
'''

import nltk
import csv
from GetComments import getComments
from ListParser import listParser

memeHash = dict(listParser("memes.csv"))
memeCount = dict()

# set up loop for gathering comments and searching them for memes
while 1:
    raw_comments = list(getComments())

    # searches comments for keywords
    for comment in raw_comments:
        for word in nltk.word_tokenize(comment):
            if word in memeHash:
                # if keyword is found, search for substrings of keyword
                for phrase in memeHash[word]:
                    if phrase in comment:
                        # if the substring is in the comment, log the counter dictionary
                        if phrase in memeCount:
                            memeCount[phrase] += 1
                        else:
                            memeCount[phrase] = 1

    # saves the counts to a log file
    with open("meme_log.csv", "w") as logfile:
        wr = csv.writer(logfile)
        for phrase in memeCount:
            wr.writerow([phrase, memeCount[phrase]])
