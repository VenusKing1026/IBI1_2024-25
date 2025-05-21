import xml.sax
import datetime
#read by line
#   startElemnt:
#       store tag as current data
#       if current data=is_a, count+1
#   character:
#       if current data==id, store id
#       if current data==namespace, store id into dict
#   endElement:
#       current data=''
#       store count in to related dict


t1=datetime.datetime.now()

BP={}
MF={}
CP={}
class Gohandler(xml.sax.ContentHandler):    
    def __init__(self):
        self.current_data=''
        self.id=''
        self.namespace=''
        self.count=0
        
    def startElement(self, tag, attrs):
        self.current_data=tag
        if self.current_data=='is_a':
            self.count+=1
            

    def characters(self, content):
        if self.current_data=='id':
            self.id=content
        if self.current_data=='namespace':
            self.namespace=content      
    
    def endElement(self, tag):
        if tag=='term':
            if self.namespace=='biological_process':
                BP[self.id]=self.count
            if self.namespace=='molecular_function':
                MF[self.id]=self.count
            if self.namespace=='cellular_component':
                CP[self.id]=self.count
            self.count=0
        self.current_data=''
parser = xml.sax.make_parser()

parser.setFeature(xml.sax.handler.feature_namespaces, 0)
     

Handler = Gohandler

parser.setContentHandler(Handler())

parser.parse('go_obo.xml')



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