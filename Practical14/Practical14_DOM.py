# sort terms in to 3 types of ontology
# in every category: find terms with the most is_a
#   store count in a dict
#   out put the the key with the largest value
import xml.dom.minidom
import datetime
t1=datetime.datetime.now()
DOMTree = xml.dom.minidom.parse("go_obo.xml")
obo=DOMTree.documentElement
terms=obo.getElementsByTagName('term')
MF={}
BP={}
CP={}
for term in terms:
    id=term.getElementsByTagName('id')[0].firstChild.nodeValue
    is_a=len(term.getElementsByTagName('is_a'))
    if term.getElementsByTagName('namespace')[0].firstChild.nodeValue=='molecular_function':
        MF[id]=is_a
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue=='biological_process':
        BP[id]=is_a
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue=='cellular_component':
        CP[id]=is_a
    
max_key1, max_value1 = max(MF.items(), key=lambda x: x[1])
max_key2, max_value2 = max(BP.items(), key=lambda x: x[1])
max_key3, max_value3 = max(CP.items(), key=lambda x: x[1])
print('Molecular_Function:')
print('id:',max_key1,'is_a:',max_value1)
print('Biological_Process:')
print('id:',max_key2,'is_a:',max_value2)
print('Cellular_components:')
print('id:',max_key3,'is_a:',max_value3)
t2=datetime.datetime.now()
print(t2-t1)



#for term in terms:
#    print('************')
#    id=term.getElementsByTagName('id')[0].firstChild.nodeValue
#    print('id=',id)
#    is_a=len(term.getElementsByTagName('is_a'))
#    print(is_a)

