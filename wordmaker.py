#!/usr/bin/python

import os
import sys

def containsAll(str, set):
    istr = str
    iset = set
    while len(iset) > 0:
        c = iset[0]
        if c not in istr:
            return 0
        else:
            iset = iset.replace(c, "", 1)
            istr = istr.replace(c, "", 1)
    return 1

letters = sys.argv[1]
dictPath = "dict/"
words = []

for filename in os.listdir(dictPath):
    for line in open(dictPath + filename):
        word = line.strip()
        if word != "":
            words.append(word)

result = []

for word in words:
    if containsAll(letters, word):
        result.append(word)

result.sort(key = len)

for word in result:
    print word
