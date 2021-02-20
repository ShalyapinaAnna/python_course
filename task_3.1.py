import json
readfile = "wikidata_1000.json"
data = {}
with open(readfile, 'r', encoding='utf-8') as file1:
    for line in file1:
        read_file = json.loads(line)
        for item in read_file:
            if "description" in read_file:
                data[read_file['label']['value']] = read_file['description']['value']
            else:
                data[read_file['label']['value']] = "None"
    print(data)
with open("json1.json", 'w', encoding='utf-8') as file2:
    json.dump(data, file2, ensure_ascii=False)
