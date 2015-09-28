__author__ = 'Andrew'

from bs4 import BeautifulSoup
import nltk

def trimBodyTags (string):
    return string[6:-7]

def extractDocuments (fileName):
    file = open(fileName, 'r')
    fileAsText = file.read()
    documentModel = BeautifulSoup(fileAsText, "html.parser")
    documents = documentModel.find_all('body');
    docsAsStrings = []
    for document in documents:
        docsAsStrings.append(trimBodyTags(str(document)))
    return docsAsStrings

tokens = nltk.word_tokenize(extractDocuments('doc.sgm')[0])

print tokens
