import wiktionaryparser
from random import randrange
parser = wiktionaryparser.WiktionaryParser()
file = open('english3.txt', 'r')
words = file.read().split('\n')
leng = [len(i) for i in words]
leng9 = [i for i in words if len(i) == 9]
leng9_item = words[randrange(1,len(words) - 1)]
print(leng9_item)
leng9_item = parser.fetch(leng9_item)
print(leng9_item[0]['definitions'][0]['text'][1])