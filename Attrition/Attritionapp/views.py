from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.db import connection
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.svm import SVC

#import tensorflow as tf
import seaborn as sns
#import keras
import random as rnd
import csv
import pandas as pd
data=pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
data
print(data)
data.head()
data.describe()
data.info()
print (data.apply(lambda col:col.unique))
data = pd.DataFrame(data)
data=data.select_dtypes(include='object')
for i in data:
    #plt.figure(figsize=(15,15))
    sns.catplot(data=data,x=i,kind='count')
    #plt.show(data)
    print(i)

k=1
#plt.figure(figsize=(40,40))
for col in data:
    if col == "Attrition":
        continue
        yes=data[data['Attrition'=='Yes']] [col]
        no=data[data['Attrition'=='No']] [col]
        plt.subplot(6,6,k)
        plt.hist(yes,bins=25,alpha=0.5,label='yes',color='b')
        plt.hist(no,bins=25,alpha=0.5,label='no',color='r')
        plt.legend(loc='upper right')
        plt.title(col)
        k+=1

    sns.catplot(data=data,x="Attrition",kind='count')
    colors=sns.color_palette("husl",2)
    plt.pie(data['Attrition'].value_counts(),labels=['No','Yes'],autopct='%.0f%%')
    plt.show()

    table=pd.crosstab(data.JobSatisfaction,data.Attrition)
    table.div(table.sum(1).astype(flout),axis=0)
    plot(kind='bar',stacked=True)
    plt.title('Stacked Bar Chart of Job satisfaction vs attirition')
    Text(0.5, 1.0, 'Stacked Bar Chart of Job satisfaction vs attrition')

    table=pd.crosstab(data.OverTime,data.Attrition)
    table.div(table.Sum(1).astype(float),axis=0).plot(kind='bar',stacked=True)
    [plt.title('Stacked Bar chart of Overtime Vs attrition')]
    Text(0.5, 1.0, 'Stacked Bar Chart of Overtime vs attrition')

    table=pd.crosstab(data.BusinessTravel, data.Attrition)
    table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
    plt.title('Stacked Bar Chart of Business Travel vs attrition')
    Text(0.5, 1.0, 'Stacked Bar Chart of Business Travel vs attrition')

    table=pd.crosstab(data.YearsSinceLastPromotion, data.Attrition)
    table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
    plt.title('Stacked Bar Chart of Business Travel vs attrition')
    Text(0.5, 1.0, 'Stacked Bar Chart of Business Travel vs attrition')

    f,ax=plt.subplots(figsize=(20,20))
    sns.heatmap(df.corr(),annot=True,linewidth=.5,fmt='.1f')
    matplotlib.axes._subplots.AxesSubplot
    a4_dims = (25, 8.27)
    fig, ax = plt.subplots(figsize=a4_dims)
    sns.countplot(data=df,x="JobRole",hue="Attrition", ax=ax )
    matplotlib.axes._subplots.AxesSubplot 
    plt.show()

data.drop(['EmployeeNumber','Over18','StandardHours','EmployeeCount'],axis=1,inplace=True)


# data['Attrition'] = data['Attrition'].apply(lambda x:1 if x == "Yes" else 0 )
# data['OverTime'] = data['OverTime'].apply(lambda x:1 if x =="Yes" else 0 )

# attrition = data[data['Attrition'] == 1]
# no_attrition = data[data['Attrition']==0]

# def categorical_column_viz(col_name):
    
#     f,ax = plt.subplots(1,2, figsize=(10,6))
  
#     # Count Plot
#     data[col_name].value_counts().plot.bar(cmap='Set2',ax=ax[0])
#     ax[1].set_title(f'Number of Employee by {col_name}')
#     ax[1].set_ylabel('Count')
#     ax[1].set_xlabel(f'{col_name}')
    
#     # Attrition Count per factors
#     sns.countplot(col_name, hue='Attrition',data=data, ax=ax[1], palette='Set2')
#     ax[1].set_title(f'Attrition by {col_name}')
#     ax[1].set_xlabel(f'{col_name}')
#     ax[1].set_ylabel('Count')

# categorical_column_viz('BusinessTravel')

# categorical_column_viz('Department')

# categorical_column_viz('EducationField')

# categorical_column_viz('Education')

# categorical_column_viz('EnvironmentSatisfaction')

# categorical_column_viz('Gender')
# categorical_column_viz('JobRole')

# categorical_column_viz('JobInvolvement')

# categorical_column_viz('MaritalStatus')

# categorical_column_viz('NumCompaniesWorked')

# categorical_column_viz('OverTime')
# categorical_column_viz('StockOptionLevel')
# categorical_column_viz('TrainingTimesLastYear')
# categorical_column_viz('YearsWithCurrManager')

# def numerical_column_viz(col_name):
#     f,ax = plt.subplots(1,2, figsize=(18,6))
#     sns.kdeplot(attrition[col_name], label='Employee who left',ax=ax[0], shade=True, color='palegreen')
#     sns.kdeplot(no_attrition[col_name], label='Employee who stayed', ax=ax[0], shade=True, color='salmon')
    
#     sns.boxplot(y=col_name, x='Attrition',data=df, palette='Set3', ax=ax[1])
# numerical_column_viz("Age")

# numerical_column_viz("Age")

# numerical_column_viz("DailyRate")

# numerical_column_viz("DistanceFromHome")

# numerical_column_viz("MonthlyIncome")

# numerical_column_viz("HourlyRate")

# numerical_column_viz("JobInvolvement")

# numerical_column_viz("PercentSalaryHike")

# numerical_column_viz("Age")
# numerical_column_viz("DailyRate")
# numerical_column_viz("TotalWorkingYears")
# numerical_column_viz("YearsAtCompany")
# numerical_column_viz("YearsInCurrentRole")
# numerical_column_viz("YearsSinceLastPromotion")
# numerical_column_viz("YearsWithCurrManager")

# def categorical_numerical(numerical_col, categorical_col1, categorical_col2):
    

#     f,ax = plt.subplots(1,2, figsize=(20,8))
    
#     g1= sns.swarmplot( categorical_col1, numerical_col,hue='Attrition', data=data, dodge=True, ax=ax[0], palette='Set2')
#     ax[0].set_title(f'{numerical_col} vs {categorical_col1} separeted by Attrition')
#     g1.set_xticklabels(g1.get_xticklabels(), rotation=90) 

    
#     g2 = sns.swarmplot( categorical_col2, numerical_col,hue='Attrition', data=data, dodge=True, ax=ax[1], palette='Set2')
#     ax[1].set_title(f'{numerical_col} vs {categorical_col1} separeted by Attrition')
#     g2.set_xticklabels(g2.get_xticklabels(), rotation=90) 

# categorical_numerical('Age','Gender','MaritalStatus')

# categorical_numerical('Age','JobRole','EducationField')

# categorical_numerical('MonthlyIncome','Gender','MaritalStatus')

# data['Total_Satisfaction'] = (data['EnvironmentSatisfaction'] + 
#                             data['JobInvolvement'] + 
#                             data['JobSatisfaction'] + 
#                             data['RelationshipSatisfaction'] +
#                             data['WorkLifeBalance']) /5 

# data.drop(['EnvironmentSatisfaction','JobInvolvement','JobSatisfaction','RelationshipSatisfaction','WorkLifeBalance'], axis=1, inplace=True)
# categorical_column_viz('Total_Satisfaction')
# data.Total_Satisfaction.describe()

# data['Total_Satisfaction_bool'] = data['Total_Satisfaction'].apply(lambda x:1 if x>=2.8 else 0 ) 
# data.drop('Total_Satisfaction', axis=1, inplace=True)


# # It can be observed that the rate of attrition of employees below age of 35 is high

# data['Age_bool'] = data['Age'].apply(lambda x:1 if x<35 else 0)
# data.drop('Age', axis=1, inplace=True)
# # It can be observed that the employees are more likey the drop the job if dailtRate less than 800

# data['DailyRate_bool'] = data['DailyRate'].apply(lambda x:1 if x<800 else 0)
# data.drop('DailyRate', axis=1, inplace=True)
# # Employees working at R&D Department have higher attrition rate

# data['Department_bool'] = df['Department'].apply(lambda x:1 if x=='Research & Development' else 0)
# data.drop('Department', axis=1, inplace=True)
# # Rate of attrition of employees is high if DistanceFromHome > 10

# data['DistanceFromHome_bool'] = data['DistanceFromHome'].apply(lambda x:1 if x>10 else 0)
# data.drop('DistanceFromHome', axis=1, inplace=True)
# # Employees are more likey to drop the job if the employee is working as Laboratory Technician

# data['JobRole_bool'] = data['JobRole'].apply(lambda x:1 if x=='Laboratory Technician' else 0)
# data.drop('JobRole', axis=1, inplace=True)
# # Employees are more likey to the drop the job if the employee's hourly rate < 65

# data['HourlyRate_bool'] = data['HourlyRate'].apply(lambda x:1 if x<65 else 0)
# data.drop('HourlyRate', axis=1, inplace=True)
# # Employees are more likey to the drop the job if the employee's MonthlyIncome < 4000

# data['MonthlyIncome_bool'] = data['MonthlyIncome'].apply(lambda x:1 if x<4000 else 0)
# data.drop('MonthlyIncome', axis=1, inplace=True)
# # Rate of attrition of employees is high if NumCompaniesWorked < 3

# data['NumCompaniesWorked_bool'] = data['NumCompaniesWorked'].apply(lambda x:1 if x>3 else 0)
# data.drop('NumCompaniesWorked', axis=1, inplace=True)
# # Employees are more likey to the drop the job if the employee's TotalWorkingYears < 8

# data['TotalWorkingYears_bool'] = data['TotalWorkingYears'].apply(lambda x:1 if x<8 else 0)
# data.drop('TotalWorkingYears', axis=1, inplace=True)

# # Employees are more likey to the drop the job if the employee's YearsAtCompany < 3

# data['YearsAtCompany_bool'] = data['YearsAtCompany'].apply(lambda x:1 if x<3 else 0)
# data.drop('YearsAtCompany', axis=1, inplace=True)
# # Employees are more likey to the drop the job if the employee's YearsInCurrentRole < 3

# data['YearsInCurrentRole_bool'] = data['YearsInCurrentRole'].apply(lambda x:1 if x<3 else 0)
# data.drop('YearsInCurrentRole', axis=1, inplace=True)


# data['YearsSinceLastPromotion_bool'] = data['YearsSinceLastPromotion'].apply(lambda x:1 if x<1 else 0)
# data.drop('YearsSinceLastPromotion', axis=1, inplace=True)


# data['YearsWithCurrManager_bool'] = data['YearsWithCurrManager'].apply(lambda x:1 if x<1 else 0)
# data.drop('YearsWithCurrManager', axis=1, inplace=True)
# data['Gender'] = data['Gender'].apply(lambda x:1 if x=='Female' else 0)
# data.drop('MonthlyRate', axis=1, inplace=True)
# data.drop('PercentSalaryHike', axis=1, inplace=True)
# convert_category = ['BusinessTravel','Education','EducationField','MaritalStatus','StockOptionLevel','OverTime','Gender','TrainingTimesLastYear']
# for col in convert_category:
#     data[col] = data[col].astype('category')
    



def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def userpage(request):
    return render(request,'userpage.html')
def loginaction(request):
    cursor=connection.cursor()
    u=request.GET['loginid']
    p=request.GET['password']
    s="select*from login where  userid='%s' and password = '%s' "%(u,p)
    cursor.execute(s)
    rs=cursor.fetchall()
    for rw in rs:
        request.session['uid']=rw[1]
        request.session['usertype']=rw[4]
        if(request.session['usertype']=='HR'):
            return render(request,'userpage.html')
        else:
            html="<script>alert('invalid username or password');window.location='/index/';</script>"
    return HttpResponse(html)
def userpage(request):
    return render(request,'userpage.html')

