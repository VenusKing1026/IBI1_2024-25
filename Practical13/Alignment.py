# input file: read fasta1 fasta2 and save as 2 variables
# read BLOSUM62 matrix as dataframe
# 
# compare:
#   for each aa1,aa2 in seq1,
#        find the position in matrix 
#        find the score and sum
#
#output:
#   2 seq alighnment
#   score

import pandas as pd
import re
path1='Practical13\P04179.fa'
path2='Practical13\P09671.fasta.txt'
path3='Practical13\\random.txt'

def get_seq(pathi):
    temp=open(pathi,'r')
    seq=''
    lines = temp.readlines()[1:]
    for line in lines:
        seq+=line[:-1]
    return seq
seq1=get_seq(path1)
seq2=get_seq(path2)
seq3=get_seq(path3)
print(seq1)
print(seq3)

matrix=pd.read_csv('./Practical13/blosum62_matonly.txt',sep='\t')
matrix.set_index('Unnamed: 0',inplace=True)

result=0
for i in range(len(seq1)): # human-mouse
    aa1=seq1[i]
    aa2=seq2[i]
    score=matrix.loc[aa1,aa2]
    result=result+score
print(result)
for j in range(len(seq1)): # human-random
    aa1=seq1[j]
    aa2=seq3[j]
    score=matrix.loc[aa1,aa2]
    result=result+score
print(result)
for k in range(len(seq1)): # mouse-random
    aa1=seq2[k]
    aa2=seq3[k]
    score=matrix.loc[aa1,aa2]
    result=result+score
print(result)



edit_similarity	=	0		
#set	initial	distance	as	zero	
for	i	in	range(len(seq1)):	#compare	each	amino	acid	
    if	seq1[i]==seq2[i]:				
        edit_similarity+=	1	#add	a	score	1	if	amino	acids	are	different	
print	(edit_similarity/222)	


