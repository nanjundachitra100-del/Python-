import numpy as np
import pandas as pd

#reating the dataframe
data={
    'name':['chitra','karthik','hamsa','riya'],
    'age':[18, 18, 19, 19],
    'salary':[15,20,30,14],
    'department':['IT', 'IT', 'HR', 'HR'],
    'city':['bangalore','bangalore','hebbal','cross']
}
df=pd.DataFrame(data)
print("Original dataframe:")
print(df)
print("\n"+"="*30 + "\n")

#cleaning dataframes
print("Befor cleaning dataframe:")
print(df.isnull().sum())

#filling missing'age'values
df['age'].fillna(df['age'].mean(),inplace=True)
df['salary'].fillna(0,inplace=True)
df = df[df['city'] != '']
print("Data after cleaning")
print(df)
print("\n"+"="*30 + "\n")

#handle duplicates
df_dup=pd.DataFrame ({ 'A': [1, 2, 2, 3],
    'B': ['x', 'y', 'y', 'z']})
print("Before handling the duplicates")
print(df_dup)
df_dup.drop_duplicates(inplace=True)
print("After handling duplicates")
print(df_dup)
print("\n"+"="*30 + "\n")

#change the data type
df['age']=df['age'].astype(int)
print("Dataframe after changing the datatype")
print(df.head())

#removing the columns
df.rename(columns={'Department':'Dept'},inplace=True)
print(df.head())

#string manipulation
df['name'] = df['name'].str.upper()

print(df.head())
print("\n"+"="*30 + "\n")

#filtering the data
it_employees = df[df['Dept'] == 'IT']
print(it_employees)
          
      
