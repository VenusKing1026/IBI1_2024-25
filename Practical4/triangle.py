#let (n as the base line) increase from 1 to 10 by 1
#     let i decrease by 1 from n
#      number=sum of i
sum=0
for n in range(1,11):
    for i in range(1,n):
        sum+=i
    print(sum)
    sum=0
    
#or we have sum=(1+n)n/2

sum=0
for n in range(1,11):
    sum=(1+n)*n/2
    print(sum)
    sum=0


sum=0
for i in range(1,11):
    sum+=i
    print(sum)