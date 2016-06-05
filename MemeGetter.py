import nltk
import itertools
import praw
import csv
import string
from GetComments import getComments

swords = set(nltk.corpus.stopwords.words(fileids = "english"))
punc = string.punctuation

def getAllSubstrings (tokens):
    for i, j in itertools.combinations(range(len(tokens) + 1), 2):
         yield tokens[i:j]

def getSubstrings(raw_comments):
    substrings = list()
    for comment in raw_comments:
        for sub in sorted(getAllSubstrings(nltk.word_tokenize(str(comment).lower())), key=len):
            phrase = ' '.join(sub).strip(punc + ' ')
            if phrase not in swords and phrase not in punc and len(phrase.split()) > 1:
                substrings.append(phrase)
    #substrings = list(filter(lambda meme: [meme for sub in substrings if meme in sub and meme != sub] == [], substrings))
    return substrings

def countSubstrings(substrings):
    subcounter = dict()
    for substring in substrings:
        if substring in subcounter:
            subcounter[substring] += 1
        else:
            subcounter[substring] = 1
    return subcounter

def getMemes(subcounter):
    memes = list()
    for substring, count in subcounter.items():
        if count > 10:
            memes.append(substring)
    return memes

def storeMemes(memes):
    with open("memes.csv", "a") as infile:
        wr = csv.writer(infile, delimiter = '\n')
        for meme in memes:
            wr.writerow([meme])

raw_comments = getComments()
substrings = getSubstrings(raw_comments)
subcounter = countSubstrings(substrings)
memes = getMemes(subcounter)
storeMemes(memes)
