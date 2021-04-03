import collections
import json
chs = collections.defaultdict()
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file1:
    read_file = json.load(file1)
for act in read_file['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            if action['character'] in chs.keys():
                chs[action['character']].append(action['says'])
            else:
                chs[action['character']] = [action['says']]

with open('task_62.txt', 'w') as text:
    text.write(str(chs))
