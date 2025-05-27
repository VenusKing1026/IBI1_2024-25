file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')


# create a dict{gene:sequence}
# read each line in file
# if start from >, put the gene name into dict
#      then get the line under it 
#      until met another line start from >
# for each sequence check if there are TATAbox in there
#     if so ,then put this gene in to tata_gene(a dict)
# print the tata_gene dict as a .fa file
dict={}
seq=''
gene=[0]
import re
             
for line in file:           #   get every gene name and sequence in the dict   
    if re.search(r'^>',line): # if it is the first line in one gene,store the sequence for last gene and store name for this gene
        dict[gene[0]]=seq
        gene=re.findall(r'gene:(\S+)',line)
        seq=''
    if not(re.search(r'^>',line)): # if it is not the first line in one gene, store the sequence as one line
        seq+=str(line[:-1])
del dict[0]

tata_gene={}
for gene1 in dict.keys():    # if it is tata gene, store it into tata_gene
    if re.search(r'TATA[AT]A[AT]',dict[gene1]):
        tata_gene[gene1]=dict[gene1]
    else:
        continue

output=open('tata_genes.fa','w')

for gene2,seq2 in tata_gene.items():  # output
    output.write('>'+str(gene2)+'\n')
    output.write(str(seq2)+'\n')









