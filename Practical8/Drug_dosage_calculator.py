#input weight
#input paracetamol
#calculate

def DrugDose(weight,sop):
    '''
    If the strength of paracetamol is 120mg/5ml, sop=0. If it is 250mg/5ml, sop=1 
    '''
    if 100>=weight>=10:
        c=[24,50][sop]
        V=15*weight/c
        print(V)
    else:
        print('Error:Weight is not normal')

#EXAMPLE
DrugDose(50,0)
DrugDose(0,0)