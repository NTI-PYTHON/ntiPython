__author__ = 'Andrew'

# Personal Branch

import re

text = 'First commit to the repository. Very simple string tokenization!'

def tokenize(string):

    return re.split('!|\.| ', text)

print tokenize(text)