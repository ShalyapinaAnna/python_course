import json
scenes = []
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file1:
    read_file = json.load(file1)
    for act in read_file['acts']:
        for scene in act['scenes']:
            characters = []
            for action in scene['action']:
                characters.append(action['character'])
            chs = list(set(characters))
            scenes.append(chs)

with open('json2.json', 'w', encoding='utf-8') as file2:
    for time in scenes:
        t = json.dumps(time)
        file2.write(t + '\n')


