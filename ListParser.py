'''
This code gathers information from a csv file and utilizes the strash code
to create a real language hash keyword.

By Tyler Sullivan and Alex Hildreth
'''

import csv
from Strash import strash

# pass by name of file. file should be simple list of phrases separated by newlines
def listParser(filename):
    with open(filename) as infile:
        rd = csv.reader(infile, delimiter='\n')
        memes = list()
        for row in rd:
            memes.extend(row)
        # hashes the list of phrases using the string hasher
        hashed_memes = dict(strash(memes))
    #returns hashed dictionary
    return hashed_memes
