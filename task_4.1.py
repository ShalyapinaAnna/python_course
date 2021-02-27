import xml.etree.ElementTree as etree
text = ''
with open('xml1.txt', 'w', encoding='utf-8') as f:
    tree = etree.parse("annot.opcorpora.no_ambig.xml")
    root = tree.getroot()
    for source in root.iter('source'):
        f.write(str(source.text) + '\n')
