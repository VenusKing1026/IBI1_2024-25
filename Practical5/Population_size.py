# initialize data and labels
# prepare a figure contain 2 plots
# set each of them
# show




import matplotlib.pyplot as plt 

# intialize data
uk_countries=[57.11,3.13,1.91,5.45]
zj_neighbours=[65.77,41.88,45.28,61.27,85.15]

# initialize label
uk_countries_lables=['England','Wales','Northern Ireland','Scotland']
zj_neighbours_lables=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']

# output 2 lists
print('UK_countries:',uk_countries,'Zhejinag_neighbors:',zj_neighbours)

# create a figure contains 2 plot
fig,(plt1,plt2)=plt.subplots(1,2,figsize=(12,6))

# set plot 1
plt1.pie(uk_countries,labels=uk_countries_lables,explode=[0.1,0,0,0],startangle=30,autopct='%1.1f%%',wedgeprops={'edgecolor':'blue','linewidth':1,'antialiased':True})
plt1.set_title('UK_countries')

# set plot 2
plt2.pie(zj_neighbours,labels=zj_neighbours_lables,explode=[0.1,0,0,0,0.1],startangle=30,autopct='%1.1f%%',wedgeprops={'edgecolor':'blue','linewidth':1,'antialiased':True})
plt2.set_title('zhejiang_neighbours')

#show
plt.tight_layout()
plt.show()