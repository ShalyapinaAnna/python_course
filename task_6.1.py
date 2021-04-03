import collections
import json
chs = {}
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file1:
    read_file = json.load(file1)
    for act in read_file['acts']:
        for scene in act['scenes']:
            for action in scene['action']:
                if action['character'] in chs.keys():
                    chs[action['character']].append(action['says'])
                else:
                    chs[action['character']] = [action['says']]

dictionary = ''
for hero in chs.keys():
    for line in chs[hero]:
        dictionary += str(line)

dictionary = dictionary.replace('?', ' ').replace(',', ' ').replace('!', ' ').replace(':', '').replace('-', ' ')\
    .replace('.', ' ').replace('[', ' ').replace(']', ' ').replace("'", ' ').replace(';', ' ').replace('"', ' ').lower()
vocab = dictionary.split(" ")
vocab1 = []
for elem in vocab:
    if elem != '':
        vocab1.append(elem)
count = collections.Counter(vocab1)
often_list = count.most_common(20)
rarely_list = count.most_common()[-20:-1]
print(often_list, '\n', rarely_list)
