__author__ = 'Andrew'

import re

text = 'First commit to the repository. Very simple string tokenization!'

tokens = re.split('!|\.| ', text)

print tokens

