__author__ = 'Andrew'

#slides: lossy compression, spimi

from collection import Collection
from spimi import SPIMI
from search_engine import SearchEngine
import glob

#usa, bacon 26085210 Erik Stodola
#zurich, president, cocoa

# Get all sgm files and store them in an array as collection objects
#collection = [Collection(file) for file in glob.glob('collection/reut*.sgm')]
collection = [Collection('collection/reut2-000.sgm')]

# Create an instance of the spimi class
spimi = SPIMI()

# This function uses a token stream from each collection object to write ordered dictionary blocks of tokens to disk
#spimi.run(collection, 1, 'reuters-freq')

# Build master inverted index with block files
#spimi.build_inverted_index('reuters-freq')

# Create an instance of the search engine object with the specified inverted index file

search_engine = SearchEngine('reuters-freq')

# Get user input and return a result
while True:
    input = raw_input('Enter query: ')
    if input == 'exit':
        break
    print search_engine.search(input)





