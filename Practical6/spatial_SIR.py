import numpy as np
import matplotlib.pyplot as plt
import imageio
# create population and set parameters
# randomly pick a person to be 0 patient
# spread and recover 100 times
# for every time
#   get patien's position
#   for every patient, infect the suspect around him
#   for every patient, let some of them recover

beta=0.3
gama=0.05
 
# make array as population 
population=np.zeros((100,100))

outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1


def infect(position):
    x,y=position[0],position[1]
    people_around=[[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    for i in people_around:
        if i[0] and i[1]>=0 and i[0]<100 and i[1]<100: # check the boundary
            if population[i[0],i[1]]==0: # if the people around him are suspected
                population[i[0],i[1]]=np.random.choice(range(2),1,p=[1-beta,beta])[0] #spread to people around him

            
def recover(position):
    population[position[0],position[1]]=np.random.choice(range(1,3),1,p=[1-gama,gama])[0]

#show the first patient
plt.subplot(3,4,1)
plt.title('step:0')
plt.imshow(population)

# loop for 100 times
for n in range(0,101):
    patient_x,patient_y=np.where(population==1) #get patient as a array
    patient=list(zip(patient_x,patient_y))# make coodinates
    for p in patient: 
        infect(p)
        recover(p)
    if n in [10,20,30,40,50,60,70,80,90,100]: # show at 10,50,100 times
        plot_position={10:2,20:3,30:4,40:5,50:6,60:7,70:8,80:9,90:10,100:11}
        plt.subplot(3,4,plot_position[n])
        plt.imshow(population)
        plt.title('step:'+str(n))
plt.tight_layout()
plt.show()
    
   