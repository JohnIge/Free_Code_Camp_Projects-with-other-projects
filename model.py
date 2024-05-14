#A model to predict who survived in the Titanic with prepared data.

#import necessary modules.
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Read .csv files in dataframes.
train_df = pd.read_csv("Titanic_train.csv")
test_df = pd.read_csv("test.csv ")

#function to show the total number of values of each field in the dataframes.
train_df.isna().sum()
test_df.isna().sum()

#Concatenate both train and test dataframes in into df & count the prefix they are and their values.
df = pd.concat([train_df, test_df])
df.Name.str.split(', ', expand=True)[1].str.split('.', expand=True)[0].value_counts()


#CLEANING STARTS
#Cleaning Function:
def clean(df):
    df.drop(['Cabin'], axis=1,inplace=True)
    df['Surname'] = df.Name.str.split(', ', expand=True)[0]
    df['Honourific'] = df.Name.str.split(', ', expand=True)[1].str.split('.', expand=True)[0]
    df.drop(['Name'], axis=1,inplace=True)
   
    for x in ['Mlle', 'Ms']:
        df.Honourific = df.Honourific.replace(x, 'Miss')
    for x in ['Lady', 'Mme', 'the Countess', 'Dona']:
        df.Honourific = df.Honourific.replace(x, 'Mrs')
    for x in ['Sir', 'Don']:
        df.Honourific = df.Honourific.replace(x, 'Mr')
    for x in ['Dr', 'Rev', 'Major', 'Col', 'Capt']:
        df.Honourific = df.Honourific.replace(x, 'Others')
    df.Honourific = df.Honourific.replace('Jonkheer', 'Master')
    return df

#Use Cleaning Function.
train_df = clean(train_df)
test_df = clean(test_df)

#Print the total no. of surnames in train dataframe only, test dataframe and both dataframes. 
print('Only Train: ', len(set(train_df.Surname.unique()).difference(set(test_df.Surname.unique()))))
print('Only test: ', len(set(test_df.Surname.unique()).difference(set(train_df.Surname.unique()))))
print('Both Train & Test: ', len(set(train_df.Surname.unique()).intersection(set(test_df.Surname.unique()))))

#Drop the 'surname' column in both dataframes.
train_df.drop(['Surname'], axis = 1, inplace=True)
test_df.drop(['Surname'], axis =1, inplace=True )

#Concatenate the updated version of the dataframes into the general dataframe 'df'.
df = pd.concat([train_df,test_df])
#CLEANING ENDS


#PREPROCESSING STARTS
#Check if they are null values in the dataframe 'df'.
df.isna().sum()

#Find the mean age of the group of people having the same prefix/honourific
for title in df.Honourific.unique():
    print(f'{title}:', df[df. Honourific == title].Age.mean())

#Count of values in the field 'Embarked' & null value check for the field/column 'Fare'.
df.Embarked.value_counts()
df[df.Fare.isna()]

#Find the correlation between the fare paid & Class of Passenger.
df.corr()['Fare']['Pclass']

#Use this function to find the missing entries.
def missing_entry(df):
    df.Embarked = df.Embarked.fillna('S')
    df.Fare = df.Fare.fillna(13.3)

    df.loc[(df.Honourific == 'Mr'), 'Age'] = df.loc[(df.Honourific == 'Mr'), 'Age'].fillna(32.8)
    df.loc[(df.Honourific == 'Mrs'),'Age'] = df.loc[(df.Honourific == 'Mrs'), 'Age'].fillna(37)
    df.loc[(df.Honourific == 'Miss'),'Age'] = df.loc[(df.Honourific == 'Miss'), 'Age'].fillna(21.8)
    df.loc[(df.Honourific == 'Master'), 'Age'] = df.loc[(df.Honourific == 'Master'), 'Age'].fillna(6.1)

    return df

#Use missing entries function on 'train' and 'test' DataFrames.
train_df = missing_entry(train_df)
test_df = missing_entry(test_df)

#Drop the column 'Honourific' in both dataframes.
train_df.drop(['Honourific'], axis=1, inplace=True)
test_df.drop(['Honourific'], axis=1, inplace=True)

#Print the total no. of Ticket in train dataframe only, test dataframe and both dataframes.
print('Only Train: ', len(set(train_df.Ticket.unique()).difference(set(test_df.Ticket.unique()))))
print('Only test: ', len(set(test_df.Ticket.unique()).difference(set(train_df.Ticket.unique()))))
print('Both Train & Test: ', len(set(train_df.Ticket.unique()).intersection(set(test_df.Ticket.unique()))))

#Concatenate & assign to 'df'.
df = pd.concat([train_df, test_df])

#
df['Ticket_Group'] = df.groupby('Ticket')['Ticket'].transform('count')
df.drop(['Ticket'], axis=1, inplace=True)

train_df = df.loc[train_df.index, :]
test_df = df.loc[test_df.index, :].drop(['Survived'], axis=1)

def encode(df):
    temp_1 = pd.get_dummies(df.Sex)
    temp_2 = pd.get_dummies(df.Embarked)
    df = df.join([temp_1, temp_2])
    df.drop(['Sex', 'Embarked'], axis=1, inplace=True)
    return df

df = pd.concat([train_df, test_df])
df = encode(df)
train_df = df.loc[train_df.index, :]
test_df = df.loc[test_df.index, :].drop(['Survived'], axis=1)
print(test_df)
#PREPROCESSING ENDS