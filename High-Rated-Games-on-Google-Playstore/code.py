# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
data['Rating'].hist()
data = data[data['Rating'] <= 5]

data['Rating'].hist()
#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
print(total_null)
percent_null = (total_null/data.isnull().count())
print(percent_null)

print(type(percent_null))
missing_data = pd.concat([total_null, percent_null], axis =1, keys =['Total','Percent'])
print(missing_data)


data = data.dropna()


total_null_1 = data.isnull().sum()
print(total_null_1)
percent_null_1 = (total_null_1/data.isnull().count())
print(percent_null_1)

print(type(percent_null_1))

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis =1, keys =['Total','Percent'])

# code ends here


# --------------

#Code starts here

a =sns.catplot(x = 'Category' , y= 'Rating',data=data, kind="box", height = 10)
a.set_xticklabels(rotation=30)
a.set_titles("Rating vs Category [BoxPlot]")

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
sns.countplot( y ='Installs' , data = data)

#data.Installs.apply(lambda x: x.strip(','))
#data.Installs.str.apply(lambda x: x.strip('+'))

data.Installs = data.Installs.str.replace(',','').str.replace('+','')
data.Installs = data.Installs.astype('int')

le = LabelEncoder()
le.fit(data['Installs'])
data['Installs'] = le.transform(data['Installs'])

a = sns.regplot( x="Installs", y="Rating" ,data=data)
a.set_title("Rating vs Installs [RegPlot]")
#Code ends here



# --------------
#Code starts here


plt.figure(figsize = (10,6))
w = sns.countplot( x ='Price' , data = data)

data.Price = data.Price.str.replace('$','')
data.Price = data.Price.astype('float')

#type(data['Price'])

s = sns.regplot(x="Price", y="Rating" , data=data)
s.set_title('Rating vs Price [RegPlot]')


#Code ends here


# --------------

#Code starts here

a = data.Genres.unique()
  
#print(df.Geek_ID.str.split('_').str[0]) 

data['Genres'] =  data['Genres'].str.split(';').str[0]
gr_mean = data.groupby("Genres",as_index=False)['Genres','Rating'].mean()
print(gr_mean.describe())

gr_mean = gr_mean.sort_values(by = 'Rating')
print(gr_mean.head(1))

print(gr_mean.tail(1))


#Code ends here


# --------------

#Code starts here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
#df['Date']= pd.to_datetime(df['Date']) 
#data.dtypes
max_date = data['Last Updated'].max()

data['Last Updated Days'] = max_date - data['Last Updated']
data['Last Updated Days'] = data['Last Updated Days'].dt.days

x = sns.regplot( x="Last Updated Days", y="Rating", data=data)
x.set_title('Rating vs Last Updated [RegPlot]')

#Code ends here


