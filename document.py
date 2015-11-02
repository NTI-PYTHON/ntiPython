__author__ = 'Andrew'

# Represents an individual document within a collection (sgm file)
class Document:
        def __init__(self, body, id):
            self.id = id
            self.body = str(body)

        # Get the token stream fron this document. Tokens are also processed with lossy compression
        def get_token_stream(self):
            import nltk
            tokens = nltk.word_tokenize(self.body)
            #tokens = self._custom_removal(tokens)
            #tokens = self._strip_punctuation(tokens)
            #tokens = self._remove_numbers(tokens)
            #tokens = self._case_fold(tokens)
            #tokens = self._remove_stopwords(tokens)
            #tokens = self._stem(tokens)
            return [{'token': token, 'id': self.id} for token in tokens]

        # Remove body tags from the document
        def _trimBodyTags (self, string):
            return string[6:-7]

        # Remove terms that other lossy compression didn't remove
        def _custom_removal(self, tokens):
            import re
            toRemove = ['\x03', "'", "''", '"', '""']
            return [i for i in tokens if i not in toRemove and not re.match('\d+',i)]

        # Remove punctuation from words
        def _strip_punctuation(self, tokens):
            import string
            return [i for i in tokens if i not in string.punctuation]

        # Remove words if they are stop words
        def _remove_stopwords(self, tokens):
            from nltk.corpus import stopwords
            return [i for i in tokens if i not in stopwords.words('english')]

        # Stem the tokens
        def _stem(self, tokens):
            from nltk.stem.porter import PorterStemmer
            stemmer = PorterStemmer()
            return [stemmer.stem(token) for token in tokens]

        # Remove tokens if they are numbers
        def _remove_numbers(self, tokens):
            return [i for i in tokens if not self._is_number(i)]

        # Case fold the terms
        def _case_fold(self, tokens):
            return [token.lower() for token in tokens]

        # Check if an individual word is a number
        def _is_number(self,s):
            try:
                float(s)
                return True
            except ValueError:
                pass

            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError, ValueError):
                pass
            return False

