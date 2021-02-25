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

for hero in chs:
    chs[hero] = len(chs[hero])

character_max = max(chs, key=chs.get)
print(character_max)
