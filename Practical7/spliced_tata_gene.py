file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')


# create a dict{gene:sequence}
# read each line in file
# if start from >, put the gene name into dict
#      then get the line under it 
#      until met another line start from >
# for each sequence check if there are TATAbox in there
#     if so ,then put this gene in to tata_gene(a dict)
# print the tata_gene dict as a .fa file

# in TATAbox, if the seq inclue the input,put it in output(dict)
# out put the dict
dict={}
seq=''
gene=[0]
import re
input=str(input('donator:'))    
if not(input in ['ATAC','GCAG','GTAC']):
    exit()
    
    
for line in file:            
    if re.search(r'^>',line):
        dict[gene[0]]=seq
        gene=re.findall(r'gene:(\S+)',line)
        seq=''
    if not(re.search(r'^>',line)):
        seq+=str(line[:-1])
del dict[0]

tata_gene={}
for gene1 in dict.keys():
    if re.search(r'TATA[AT]A[AT]',dict[gene1]):
        tata_gene[gene1]=dict[gene1]
    else:
        continue

output=open(str(input)+'_spliced_genes.fa','w')

for gene2,seq2 in tata_gene.items():
    if re.search(input,seq2):
         output.write('>'+str(gene2)+'   tata:'+str(len(re.findall(r'TATA[AT]A[AT]',seq2)))+'\n')
         output.write(str(seq2)+'\n')
       









