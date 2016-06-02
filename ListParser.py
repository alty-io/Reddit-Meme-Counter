'''
This code gathers information from a csv file and utilizes the strash code
'''

import csv
from strash import strash

with open("memes.csv") as infile:
    rd = csv.reader(infile, delimiter='\n')
    memes = list()
    for row in rd:
        memes.extend(row)

hashed_memes = strash(memes)
