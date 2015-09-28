__author__ = 'Andrew'

import os
from bs4 import BeautifulSoup


class collection:
    def __init__(self, fileName):
        self.fileName = fileName
        if (os.path.exists(fileName)):
            self.file = open(fileName)
            self.text = self.file.read()

    def getDocuments(self):
        if (hasattr(self, "documents")):
            return self.documents
        else:
            util = UtilityFunctions()
            dom = BeautifulSoup(self.text, 'html.parser')
            documents = dom.find_all('body');
            docsAsStrings = []
            for document in documents:
                docsAsStrings.append(util.trimBodyTags(str(document)))
            self.documents = docsAsStrings
            return self.documents


class UtilityFunctions:
    def trimBodyTags(self, text):
        return text[6:-7]
