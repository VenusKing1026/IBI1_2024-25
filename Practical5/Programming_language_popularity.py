# impot matplot
# initialize dictionary
# get what users want to know
# give the value corresponding to the key

# set plot size,title,label
# draw bar plot 

import matplotlib.pyplot as plt # import

popularity_data={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5,} #initialize
Language=str(input('Language:')) # get the key
print(popularity_data.get(Language,"No such language")) # give users data they want
print(popularity_data)

pl=plt.bar(popularity_data.keys(),popularity_data.values()) # initialize barplot

# set labels title for plot
plt.ylabel('Percentage')
plt.xlabel('Language')
plt.title('programming language popularity')
plt.show()



