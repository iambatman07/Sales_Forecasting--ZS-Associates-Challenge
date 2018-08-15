The yds_train file that has been given contains sales per week this has to be summed up and the NAN's has to dealt with and merged with the respective holidays and expense prices (null values also dealt with)  and has been written to a new csv file ,same goes the case for test file, this has been done in the "extraction.py". 
The holidays.xls has also been altered to show the week number as per the date . 


The Prediction.py uses the ExtraTreesRegressor to predict the monthly sales as per the given features , country specifically and merges all the values and writes them to the final test file in that order and format . 
