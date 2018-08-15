import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor



train = pd.read_csv('/home/nandy/Documents/datasets/9555b456-8-dataset/dataset/yds_train2018.csv')
train_promo = pd.read_csv('/home/nandy/Documents/datasets/9555b456-8-dataset/dataset/promotional_expense.csv')
holidays = pd.read_excel('/home/nandy/Downloads/holidays.xlsx')
test = pd.read_csv('/home/nandy/Documents/datasets/9555b456-8-dataset/dataset/yds_test2018.csv')


test1 = test.drop(['S_No', 'Sales'], axis=1)
test1 =test1.merge(holidays, left_on=['Country', 'Month'], right_on=['Country','Month'], how ='left')
test1['counts'] = test1['counts'].fillna(0)
test1 = test1.merge(train_promo, left_on=['Year', 'Month', 'Product_ID','Country'], right_on=['Year', 'Month', 'Product_Type','Country'], how='left')
test1=test1.drop('Product_Type',axis=1)
test1.isnull().sum()
test1['Expense_Price'][(test1['Year']==2017) & (test1['Country']=='Columbia') & (test1['Product_ID']==3)] = 2414.13493
test1['Expense_Price'][(test1['Year']==2017) & (test1['Country']=='Argentina') & (test1['Product_ID']==3)] = 6472.0140
test1.isnull().sum()
test1[['Year', 'Month', 'Country', 'Product_ID', 'counts','Expense_Price']].to_csv("finaltestfile.csv", index=False)


train2 = train.drop(['S_No', 'Week'], axis=1)
train2 = train2.groupby(['Year', 'Month', 'Country', 'Product_ID'], as_index=False).sum()
train2_expense = train2.merge(train_promo, left_on=['Year', 'Month', 'Country', 'Product_ID'], right_on=['Year', 'Month', 'Country', 'Product_Type'], how='left')
train2_expense = train2_expense.drop(['Product_Type'], axis=1)
use=['Unnamed: 7','Unnamed: 8','Date','Datefor','WeekNum','Holiday']
holidays= holidays.drop(use, axis=1)
holidays= holidays.groupby(['Country','Month']).size().reset_index(name='counts')


prop =train2_expense.merge(holidays,left_on=[ 'Month', 'Country'], right_on=['Month', 'Country'], how= 'left' )
prop['counts'] =prop['counts'].fillna(0)

mean = prop.drop(['Sales','Month','counts'], axis=1)
mean = mean.groupby(['Year','Product_ID','Country'], as_index=False).mean()
median= mean.drop('Product_ID', axis=1)
median = median.groupby(['Year','Country'], as_index=False).mean()


def dothemean(row):
    if pd.isnull(row['Expense_Price']):
        return mean['Expense_Price'][ (mean['Year'] == row['Year']) 
        & (mean['Country'] == row['Country']) 
        & (mean['Product_ID'] == row['Product_ID'])]
    else:
        return row['Expense_Price']

prop['Expense_Price'] = prop.apply(dothemean, axis = 1)
prop[['Year','Month','Product_ID','Country','Sales','counts','Expense_Price']].to_csv("finaldataset.csv", index=False)
