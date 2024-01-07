#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import all libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Absenteeism Class to use to predict new data

class absenteeism_model():
    
    def __init__(self, model_file, scaler_file):
        # Reads the 'model' and 'scaler' files and initialise
        with open('model','rb') as model_file, open('scaler','rb') as scaler_file:
            self.reg = pickle.load(model_file)
            self.scaler = pickle.load(scaler_file)
            self.data = None
            
    # takes a data file ( *.csv) and preprocess (ID, Reasons for Absence, Date, Education, variables not needed)
    def load_and_clean_data(self, data_file):
        df = pd.read_csv(data_file, delimiter=',')
        self.df_with_predictions = df.copy()
        
        # ID column
        # drop ID column
        df = df.drop(["ID"], axis=1)
        
        df['Absenteeism Time in Hours'] = 'NaN'
        
        # Reason for Absence column
        # new dataframe to create dummy values for Reason for Absence for all available reasons
        reason_columns = pd.get_dummies(df['Reason for Absence'],dtype=int, drop_first=True)
        
        # grouping reasons to 4 types
        reason_type_1 = reason_columns.loc[:,1:14].max(axis=1)
        reason_type_2 = reason_columns.loc[:,15:17].max(axis=1)
        reason_type_3 = reason_columns.loc[:,18:21].max(axis=1)
        reason_type_4 = reason_columns.loc[:,22:].max(axis=1)
        
        # drop 'Reason for Absense' to avoid multicollinearity and concatenate both dataframes
        df = df.drop(['Reason for Absence'], axis=1)
        df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis=1)
        column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
                        'Daily Work Load Average', 'Body Mass Index', 'Education',
                        'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1',
                        'Reason_2' , 'Reason_3', 'Reason_4']
        df.columns = column_names
        
        # reorder columns
        column_names_reordered = ['Reason_1', 'Reason_2' , 'Reason_3', 'Reason_4', 
                                  'Date', 'Transportation Expense', 'Distance to Work', 'Age',
                                  'Daily Work Load Average', 'Body Mass Index', 'Education',
                                  'Children', 'Pets', 'Absenteeism Time in Hours' ]
        df = df[column_names_reordered]
        
        # Date column
        # convert 'Date' column into datetime
        df['Date'] = pd.to_datetime(df['Date'],format = '%d/%m/%Y')
        
        # create a list with months as %m from Date columns and append as a new column 'Month Value'
        list_months = []
        for i in range(df.shape[0]):
            list_months.append(df['Date'][i].month)
        df['Month Value'] = list_months
        
        # create new column 'Day of the Week'
        df['Day of the Week'] = df['Date'].apply(lambda x: x.weekday())
        
        # drop 'Date' column and reorder columns
        df = df.drop('Date', axis=1)
        reordered_columns = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4',
                             'Month Value', 'Day of the Week', 'Transportation Expense', 
                             'Distance to Work', 'Age', 'Daily Work Load Average', 'Body Mass Index',
                             'Education', 'Children', 'Pets', 'Absenteeism Time in Hours']
        df = df[reordered_columns]
        
        # Education column map as binary
        df['Education'] = df['Education'].map({1:0, 2:1, 3:1, 4:1})
        
        df = df.drop(['Absenteeism Time in Hours'], axis=1)
        
        # Drop other columns not needed
        df = df.drop(['Day of the Week', 'Daily Work Load Average', 'Distance to Work'], axis=1)
        
        self.preprocessed_data = df.copy()
        
        self.data = self.scaler.transform(df)
     
    # outputs the probability of a data point to be 1
    def predicted_probability(self):
        if (self.data is not None):
            pred = self.reg.predict_proba(self.data)[:,1]
            return pred
        
    # outputs 0 if not excessively abesent or 1 if excessively absent    
    def predicted_output_category(self):
        if (self.data is not None):
            pred_otuputs = self.reg.predict(self.data)
            return pred_outputs
        
    def predicted_outputs(self):
        if (self.data is not None):
            self.preprocessed_data['Probability'] = self.reg.predict_proba(self.data)[:,1]
            self.preprocessed_data['Prediction'] = self.reg.predict(self.data)
            return self_preprocessed_data

