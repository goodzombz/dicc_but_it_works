import wiktionaryparser
parser = wiktionaryparser.WiktionaryParser()
file = open('english3.txt', 'r')
words = file.read().split('\n')
file = open('dic.txt', 'a')
file.write('dictionary = {\n')
print(parser.fetch('aachen'))
for i in words:
    try:
        parser.fetch(i)[0]['definitions'][0]['text'][1]
    except:
        print(f'{i} failed')
    else:
        file.write(f"{i} : {parser.fetch(i)[0]['definitions'][0]['text'][1]}\n")