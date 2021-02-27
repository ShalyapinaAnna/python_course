import xml.etree.ElementTree as etree
conj = 0
verb = 0
tree = etree.parse("annot.opcorpora.no_ambig.xml")
root = tree.getroot()
for token in root.iter('token'):
    if token.get('text') == 'может':
        if token[0][0][0][0].get('v') == 'CONJ':
            conj += 1
        elif token[0][0][0][0].get('v') == 'VERB':
            verb += 1
    elif token.get('text') == 'Может':
        if token[0][0][0][0].get('v') == 'CONJ':
            conj += 1
        elif token[0][0][0][0].get('v') == 'VERB':
            verb += 1
print('conj = ' + str(conj))
print('verb = ' + str(verb))
