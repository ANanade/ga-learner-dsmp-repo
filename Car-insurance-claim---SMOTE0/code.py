# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# Code starts here

# Read the dataframe in the df dataframe
df = pd.read_csv(path)

# Print the head of dataframe showing top 5 record
#print(df.head())

# Print dataframe information
#print(df.info())

# Remove $ and , from the column
column_name = ['INCOME', 'HOME_VAL', 'BLUEBOOK', 'OLDCLAIM', 'CLM_AMT']
df[column_name] = df[column_name].replace({'\$': '', ',': ''}, regex=True)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Count the total of value count for y column
count = df['CLAIM_FLAG'].value_counts()

# Split the dataset in train and test dataset
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3, random_state=6)

# Code ends here



# --------------
# Code starts here
for column in column_name:
    X_train[column] = X_train[column].astype('float')
    X_test[column] = X_test[column].astype('float')

print(X_train.isnull().sum())
print(X_test.isnull().sum())


# Code ends here


# --------------
# Code starts here
X_train.dropna(subset=['YOJ', 'OCCUPATION'], inplace=True)
X_test.dropna(subset=['YOJ', 'OCCUPATION'], inplace=True)
y_train = y_train[X_train.index]
y_test = y_test[X_test.index]

column_mean = ['AGE', 'CAR_AGE', 'INCOME']

for column in column_mean:
    mean_train = X_train[column].mean()
    mean_test  = X_test[column].mean()
    X_train[column].fillna(value=mean_train, inplace=True)
    X_test[column].fillna(value=mean_test, inplace=True)


# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
le = LabelEncoder()

for column in columns:
    X_train[column] = le.fit_transform(X_train[column].astype('str'))
    X_test[column] = le.transform(X_test[column].astype('str'))


# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression



# code starts here 
print(X_train.isnull().sum())

# Create a Logistic Regression Model
model = LogisticRegression(random_state = 6)

# Fit the model on Train and Test Dataset
model.fit(X_train, y_train)

# Make Predeciton on Test DataSet
y_pred = model.predict(X_test)

# Calculate Accuracy Score
score = accuracy_score(y_test, y_pred)
print('Accuracy Score:- ', score)

# Calclulate Precision Score
precision = precision_score(y_test, y_pred)
print('Precision Score', precision)
# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here

smote=SMOTE(random_state=6)
X_train,y_train=smote.fit_sample(X_train,y_train)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# Code ends here


# --------------
# Code Starts here

model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
score=accuracy_score(y_test,y_pred)
# Code ends here


