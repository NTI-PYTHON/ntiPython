__author__ = 'Andrew'

# Class representing a search engine on an inverted index
class SearchEngine:
    def __init__(self, name):
        self.name = name
        self.inverted_index = self._load_index()

    # Loads the inverted index into memory
    def _load_index(self):
        inverted_index_file = open('indices/' + self.name + '/inverted_index.json')
        inverted_index = {}

        term_count = 0
        while True:
            term_count += 1
            import ast
            line = inverted_index_file.readline()
            if line == '':
                break
            posting = ast.literal_eval(line)
            inverted_index[posting["term"]] = posting["postings"]

        print "terms: " + term_count
        return inverted_index

    # Process the query
    def search(self, query):
        from document import Document
        query_processor = Document(query, 0)
        query_as_tokens = query_processor.get_token_stream()
        list_result = []

        # Intersect posting lists
        for token in query_as_tokens:
            if self.inverted_index.has_key(token['token']):
                if len(list_result) > 0:
                    list_result = self._and(list_result, self.inverted_index[token['token']])
                else:
                    list_result = self.inverted_index[token['token']]
            else:
                list_result = self._and(list_result, [])


        return list_result

    # Return the intersection
    def _and(self, postings1, postings2):
        return list(set(postings1) & set(postings2))
