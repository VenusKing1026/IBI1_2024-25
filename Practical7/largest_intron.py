seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 

import re

# start from GT and end with AG
intron=re.findall(r'GT\S+AG',seq)
print(intron,len(intron[0]))