__author__ = 'Andrew'

import os

if(os.path.exists('test.txt')):
    file = open('test.txt', 'r+')
    text = file.read()
    file.write('\nnewline')
    file.close()
    print text
else:
    print 'file not found!'