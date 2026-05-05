#!/usr/bin/env python
import sys
import re

# Define stopwords
stopwords = set([
    "the","and","to","of","in","a","is","that","it","for",
    "on","with","as","by","at","an","be","this","which","or"
])

for line in sys.stdin:
    line = line.lower()
    words = re.findall(r'\b[a-z]+\b', line)
    
    for word in words:
        if word not in stopwords:
            print "%s\t%d" % (word, 1)
