import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
for V in range(0,10000,1000):
    
#define basic variables 
#because if I=1 it is too easy for him to revover, so I set 10
    N=10000
    I=1
    R=0
    S=N-I-R-V
 

#beta=infection probablity gama=recovery probability
    beta=0.3
    gama=0.05

# track for every day
    track_R=[R] 
    track_S=[S]
    track_I=[I]


# make 1000 loops
# for each loop:
#   every S have p(beta*I/N) get sick 
#   every I have p(gama) get recovered
#   count new sick people and add into I
#   count new recovered people and add into R
#

    for i in range(0,1001):
        S_condition=[]
        I_condition=[]
        S_condition=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N]) 
        new_infected=sum(S_condition)
        I_condition=np.random.choice(range(2),I,p=[1-gama,gama])
        new_recovered=sum(I_condition)
        S=S-new_infected
        I=I+new_infected-new_recovered
        R=R+new_recovered

        track_I.append(I)
   
    # plot 
    plt.plot(track_I,label="Vaccination:"+str(int(V*100/N))+'%')

plt.plot([0]*1000,label="Vaccination:100%")    
plt.xlabel('time')
plt.ylabel('number of infected people')
plt.title('Herd immunity')
plt.legend()
plt.show()


