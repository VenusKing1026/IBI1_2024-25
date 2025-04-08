#get DNA sequence
#get targeted sequence
# check DNA seq and targeted seq are all in ATCG
# find targeted seq in DNA seq and report+

DNA=str(input('DNA:'))
Tseq=str(input('Targeted sequence:'))

import re
def findTseq(DNA,Tseq):
    if re.match(r'[ATCG]+$',DNA) and re.match(r'[ATCG]+$',Tseq):
        if re.search(Tseq,DNA):
            results= re.finditer(Tseq,DNA)
            for i in results:
                 print(i.start()+1)
        else:
            print('Error:Tseq is not in DNA')
    else:
        print('Error:sequence error')

findTseq(DNA,Tseq)