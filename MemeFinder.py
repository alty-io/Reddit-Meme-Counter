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
testcount = 10

# set up loop for gathering comments and searching them for memes
count = 0
meme_found = False
with open("meme_log.csv", "w") as logfile:
    wr = csv.writer(logfile)
    while count < testcount:
        raw_comments = list(getComments())
        # searches comments for keywords
        for comment in raw_comments:
            comment = str(comment)
            for word in nltk.word_tokenize(comment):
                if word in memeHash:
                    #print("found keyword")
                    # if keyword is found, search for substrings of keyword
                    for phrase in memeHash[word]:
                        if phrase in comment:
                            print("found meme")
                            meme_found = True
                            # if the substring is in the comment, log the counter dictionary
                            if phrase in memeCount:
                                memeCount[phrase] += 1
                            else:
                                memeCount[phrase] = 1
    
        for phrase in memeCount:
            print(phrase + str(memeCount[phrase]))
            wr.writerow([phrase, memeCount[phrase]])
        
        if meme_found:
            break
        #count += 1
