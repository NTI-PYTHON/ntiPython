__author__ = 'Andrew'

# Represents an sgm file
class Collection:
    def __init__(self, fileName):
        self.fileName = fileName

    # Private function used to extract the documents from this collection
    def _get_documents(self):
        from document import Document
        from bs4 import BeautifulSoup
        file = open(self.fileName)
        text = file.read()
        document_model = BeautifulSoup(text, 'html.parser')
        documents = document_model.find_all('reuters')
        document_collection = []
        for document in documents:
            document_body = document.find('body')
            document_id = document['newid']
            document_collection.append(Document(document_body, document_id))
        return document_collection

    # Get a token stream from the list of documents
    def get_token_stream(self):
        token_stream = []
        for doc in self._get_documents():
            token_stream.extend(doc.get_token_stream())
        return token_stream



