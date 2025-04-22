import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change dir
# os.chdir('E:/IBI/IBI1_2024-25/Practical10')
# print(os.getcwd())
# print(os.listdir())

dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')
# print(dalys_data.head(5))

# # show third column for the first 10 rows
print(dalys_data.iloc[:10,2])

# !!!!the 10th year in Afghanistan
print(dalys_data.iloc[9,2])


# #for balabal part
print(dalys_data.loc[dalys_data.Year==1990,'DALYs'])

#compare uk and france
ukm=dalys_data.loc[dalys_data.Entity=='United Kingdom','DALYs'].mean()
frm=dalys_data.loc[dalys_data.Entity=='France','DALYs'].mean()
print('UK>FR' if ukm>frm else 'UK<FR')

#store uk info
uk=dalys_data.loc[dalys_data.Entity=='United Kingdom',['DALYs','Year']]
plt.plot(uk.Year,uk.DALYs,'bo')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel('Years')
plt.ylabel('DALYs')
plt.title('UK DALYs over time')
plt.show()

# average of DALYs change over whorld
# groupby years
# calculate average
# plot

data=dalys_data.groupby('Year').DALYs.sum()
plt.plot(data,'bo')
plt.xticks(uk.Year,rotation=-90)
plt.title('World DALYs average over time')
plt.xlabel('Years')
plt.ylabel('DALYs')
plt.show()