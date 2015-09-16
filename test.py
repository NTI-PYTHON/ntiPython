__author__ = 'Andrew'

# Personal Branch

import re

text = 'First commit to the repository. Very simple string tokenization!'

tokens = re.split('!|\.| ', text)

print tokens

