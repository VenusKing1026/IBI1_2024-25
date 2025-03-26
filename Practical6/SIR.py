import numpy as np
import matplotlib.pyplot as plt

#define basic variables 
N=10000
I=1
R=0
S=N-I-R

#beta=infection probablity gama=recovery probability
beta=0.3
gama=0.05

# track for every day
track_R=[R] 
track_S=[S]
track_I=[I]

# Function version:
# make 1000 loops
# for each loop i:
#    Recovered_i+1= Recovered_i + Infected_i * gama  # revovered_i + new_recovered
#    Infected_i+1= Infected_i - Infected_i * gama  + Suspected_i * beta * Infected_i/N # infected_i - new_recovered + new_infected
#    Suspected_i+1= N- R_i+1 - I_i+1
#    add into track_


# for i in range(0,1001):
    #  R=R + I*gama
    #  I=I - I*gama + S*beta*I/N
    #  S=N-R-I
    #  track_R.append(R)
    #  track_I.append(I)
    #  track_S.append(S)


# Random_Pick version:
# make 1000 loops
# for each loop:
#   every S have p(beta) get sick 
#   every I have p(gama) get recovered
#   count new sick people and add into I
#   count new recovered people and add into R
#


for i in range(0,1001):
    S_condition=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N])
    new_infected=sum(S_condition)
    I_condition=np.random.choice(range(2),I,p=[1-gama,gama])
    new_recovered=sum(I_condition)
    S=S-new_infected
    I=I+new_infected-new_recovered
    R=R+new_recovered
    track_R.append(R)
    track_I.append(I)
    track_S.append(S)


plt.figure(figsize=(10,10))
plt.plot(track_I,label='Infected')
plt.plot(track_S,label='Suspected')
plt.plot(track_R,label='Recovery')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.savefig("SIR model")
plt.show()




      