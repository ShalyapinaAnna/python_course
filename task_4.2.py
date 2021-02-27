import xml.etree.ElementTree as etree
text = ''
with open('xml2.txt', 'w', encoding='utf-8') as f:
    tree = etree.parse("annot.opcorpora.no_ambig.xml")
    root = tree.getroot()
    for token in root.iter('token'):
        if token[0][0][0][0].get('v') == 'NOUN':
            if token[0][0][0][3].get('v') == 'plur':
                f.write(str(token.get('text')) + '\n')
