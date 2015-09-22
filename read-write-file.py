__author__ = 'Andrew'


import os
from bs4 import BeautifulSoup
import nltk

file = open('doc.sgm', 'r')
text = file.read()
soup = BeautifulSoup(text, "html.parser")
body = str(soup.find_all('body')[0]);

tokens = nltk.word_tokenize(body)
print tokens