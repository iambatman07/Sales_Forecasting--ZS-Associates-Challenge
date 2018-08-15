import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('/home/nandy/Documents/ZS/finaldataset.csv')
testfile = pd.read_csv('/home/nandy/Documents/ZS/finaltestfile.csv')
test = pd.read_csv('/home/nandy/Documents/ZS/yds_test2018.csv')

le =LabelEncoder()
dataset['Country'] = le.fit_transform(dataset['Country'])
testfile['Country'] = le.fit_transform(testfile['Country'])
dataset['counts'][ dataset['counts'] != 0 ] = 1 
testfile['counts'][ testfile['counts'] != 0 ] = 1 

data_0 = dataset[dataset['Country']=='Argentina'].drop('Country' , axis =1 )
testfile_0 = testfile[testfile['Country']=='Argentina' ].drop('Country' , axis =1 )

data_1 = dataset[dataset['Country']== 'Belgium'].drop('Country' , axis =1 )
testfile_1 = testfile[testfile['Country']== 'Belgium'].drop('Country' , axis =1 )

data_2 = dataset[dataset['Country']=='Columbia'].drop('Country' , axis =1 )
testfile_2 = testfile[testfile['Country']=='Columbia' ].drop('Country' , axis =1 )

data_3 = dataset[dataset['Country']=='Denmark'].drop('Country' , axis =1 )
testfile_3 = testfile[testfile['Country']=='Denmark' ].drop('Country' , axis =1 )

data_4 = dataset[dataset['Country']=='England'].drop('Country' , axis =1 )
testfile_4 = testfile[testfile['Country']=='England' ].drop('Country' , axis =1 )

data_5 = dataset[dataset['Country']=='Finland'].drop('Country' , axis =1 )
testfile_5 = testfile[testfile['Country']=='Finland' ].drop('Country' , axis =1 )

clf = ExtraTreesRegressor(n_estimators=99 , max_depth= 18,criterion='mae',min_samples_leaf=1,min_samples_split=2)
clf.fit(data_0.drop('Sales' , axis=1),data_0['Sales'])
testfile_0['Sales'] = clf.predict(testfile_0)

clf.fit(data_1.drop('Sales' , axis=1),data_1['Sales'])
testfile_1['Sales'] = clf.predict(testfile_1)

clf.fit(data_2.drop('Sales' , axis=1),data_2['Sales'])
testfile_2['Sales'] = clf.predict(testfile_2)

clf.fit(data_3.drop('Sales' , axis=1),data_3['Sales'])
testfile_3['Sales'] = clf.predict(testfile_3)

clf.fit(data_4.drop('Sales' , axis=1),data_4['Sales'])
testfile_4['Sales'] = clf.predict(testfile_4)

clf.fit(data_5.drop('Sales' , axis=1),data_5['Sales'])
testfile_5['Sales'] = clf.predict(testfile_5)

newtestfile = testfile_0 
newtestfile = newtestfile.append(testfile_1)
newtestfile = newtestfile.append(testfile_2)
newtestfile = newtestfile.append(testfile_3)
newtestfile = newtestfile.append(testfile_4)
newtestfile = newtestfile.append(testfile_5)

test['Sales'] = newtestfile['Sales']
test[['S_No', 'Year', 'Month', 'Country', 'Product_ID', 'Sales']].to_csv("countrywise4.csv", index=False)

