__author__ = 'Andrew'


class SPIMI:

    # This function uses a token stream from each collection object to write ordered dictionary blocks of tokens to disk
    def run(self, collection_list, block_size_mb, folder):
        import sys
        import collections
        inverted_index = {}
        token_count = 0;
        for collection in collection_list:
            token_stream = collection.get_token_stream()
            for token_object in token_stream:
                token_count += 1
                if inverted_index.has_key(token_object["token"]):
                    if token_object['id'] not in inverted_index[token_object["token"]]:
                        inverted_index[token_object["token"]].append(token_object['id'])
                else:
                    inverted_index[token_object["token"]] = [token_object['id']]
                if sys.getsizeof(inverted_index) >= block_size_mb * 1000000:
                    self.write_to_disk(collections.OrderedDict(sorted(inverted_index.iteritems())), folder)
                    inverted_index = {}
            print collection.fileName + "\n"
        self.write_to_disk(collections.OrderedDict(sorted(inverted_index.iteritems())), folder)
        print 'tokens: ' + str(token_count)

    # Private function that writes a dictionary to disk
    def write_to_disk(self, inverted_index, folder):
        folder_path = 'indices/' + folder
        import os
        import uuid
        import json
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        file_path = folder_path + '/block_file_' + str(uuid.uuid4()) + '.json'
        file = open(file_path, 'w')
        for term, postings in inverted_index.iteritems():
            file.write(json.dumps({'term': term, 'postings': sorted(postings)}) + '\n')
        file.close()

    # This function merges blocks of inverted indexes to a master inverted index
    def build_inverted_index(self, folder):
        import json
        import ast
        import glob
        folder_path = 'indices/' + folder + '/block_file_*.json'
        inverted_index_file_path = 'indices/' + folder + '/inverted_index.json'
        inverted_index_file = open(inverted_index_file_path, 'w')
        file_list = glob.glob(folder_path)
        file_pointers = [open(file) for file in file_list]
        first_word_list = []

        for index, file_pointer in enumerate(file_pointers):
            posting_list_item = file_pointer.readline()
            first_word_list.append({'posting': ast.literal_eval(posting_list_item), 'index': index})

        while len(file_pointers) > 0:
            smallest_word = []

            for first_word in first_word_list:
                if len(smallest_word) == 0:
                    smallest_word.append(first_word)
                else:
                    if first_word['posting']['term'] < smallest_word[0]['posting']['term']:
                        smallest_word = [first_word]
                    elif first_word['posting']['term'] == smallest_word[0]['posting']['term']:
                        smallest_word.append(first_word)

            merged_postings_list = []

            for words in smallest_word:
                for posting in words['posting']['postings']:
                    if posting not in merged_postings_list:
                        merged_postings_list.append(posting)

            inverted_index_file.write(json.dumps({'term': smallest_word[0]['posting']['term'], 'postings': sorted(merged_postings_list)}))
            inverted_index_file.write('\n')

            for words in smallest_word:
                posting_list_item = file_pointers[words['index']].readline()
                if posting_list_item == '':
                    file_pointers.pop(words['index'])
                    first_word_list.pop(words['index'])
                    for index, first_word in enumerate(first_word_list):
                        first_word['index'] = index
                else:
                    first_word_list[words['index']] = {'posting': ast.literal_eval(posting_list_item), 'index': words['index']}

        inverted_index_file.close()
