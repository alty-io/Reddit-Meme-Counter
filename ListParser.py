'''
This code gathers information from a csv file and utilizes the strash code
'''

import csv
from Strash import strash

def listParser(filename):
    with open(filename) as infile:
        rd = csv.reader(infile, delimiter='\n')
        memes = list()
        for row in rd:
            memes.extend(row)

        hashed_memes = strash(memes)

    return hashed_memes
