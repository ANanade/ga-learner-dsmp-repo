# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data= pd.read_csv(path)
#Code starts here 
#print(data)
data['Gender'].replace('-','Agender', inplace= True)
print(data)

gender_count= data['Gender'].value_counts()
print(gender_count)


# --------------
#Code starts here
alignment= data['Alignment'].value_counts()

print(alignment)
plt.pie(alignment)
#plt.title ='Character Alignment'


# --------------
#Code starts here
sc_df=data[['Strength','Combat']].iloc[::].copy()
print(sc_df)
sc_covariance=sc_df.Strength.cov(sc_df.Combat)
print(sc_covariance)
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
sc_pearson=(sc_covariance/(sc_strength*sc_combat))
print(sc_pearson)
ic_df=data[['Intelligence','Combat']].iloc[::].copy()
ic_covariance=ic_df.Intelligence.cov(ic_df.Combat)
ic_combat=ic_df.Combat.std()

ic_intelligence=ic_df.Intelligence.std()
ic_pearson=(ic_covariance/(ic_intelligence*ic_combat))
print(ic_pearson)
#sc_covariance= 


# --------------
#Code starts here

#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)

#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

#Printing the names
print(super_best_names)

#Code ends here


# --------------
#Code starts here

import matplotlib.pyplot as plt


fig ,(ax_1) = plt.subplots()
fig1 , ax_2 = plt.subplots()
fig2 , ax_3 = plt.subplots()
ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')


