import pandas as pd
import numpy as np
import os

# Extract function is already implemented for you 
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

# Call the extract() function and store it as the "merged_df" variable
merged_df = extract(grocery_sales, "extra_data.parquet")

# Create the transform() function with one parameter: "raw_data"
def transform(raw_data):
    # ['index', 'Store_ID', 'Date', 'Dept', 'Weekly_Sales', 'IsHoliday',
    # 'Temperature', 'Fuel_Price', 'MarkDown1', 'MarkDown2', 'MarkDown3',
    # 'MarkDown4', 'MarkDown5', 'CPI', 'Unemployment', 'Type', 'Size']
    
    raw_data.fillna({
        'Weekly_Sales': raw_data['Weekly_Sales'].mean(),
        'Fuel_Price': raw_data['Fuel_Price'].mean(),
        'Temperature': raw_data['Temperature'].mean(),
        'Unemployment': raw_data['Unemployment'].mean(),
        'Date': raw_data['Date'].mode(),
        'CPI':  raw_data['CPI'].mean()
    }, inplace = True)
    
    # filter for rows with weekly sales > 10000
    filter = raw_data['Weekly_Sales'] > 10000
    raw_data = raw_data[filter]
    
    # add a new column "Month"
    raw_data['Month'] = raw_data['Date'].dt.month
    raw_data['Month'] = raw_data['Month'].astype('Int64')
    
    # keep only the necessary columns 
    columns = ['Store_ID', 'Weekly_Sales', 'CPI', 'Unemployment', 'Month']
    raw_data = raw_data.loc[:, columns]
    
    return raw_data

# Call the transform() function and pass the merged DataFrame
clean_data = transform(merged_df)


# Create the avg_weekly_sales_per_month function that takes in the cleaned data from the last step
def avg_weekly_sales_per_month(clean_data):

    # remove records wihout Month
    clean_data = clean_data.dropna(subset=['Month'], how='any')
    
    # group data by month, calculate the mean, reset the index, and round the avg sales 
    agg_df = clean_data.groupby(['Month']).mean().reset_index().round()

    return agg_df

# Call the avg_weekly_sales_per_month() function and pass the cleaned DataFrame
avg_df = clean_data[['Weekly_Sales', 'Month']]
avg_df.rename(columns={"Weekly_Sales": "Avg_Sales"}, inplace = True)

agg_data = avg_weekly_sales_per_month(avg_df)

# Create the load() function that takes in the cleaned DataFrame and the aggregated one with the paths where they are going to be stored
def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    full_data.to_csv(full_data_file_path, index=False)
    agg_data.to_csv(agg_data_file_path, index=False)

# Call the load() function and pass the cleaned and aggregated DataFrames with their paths
cd_data_path = 'clean_data.csv'
agg_data_path = 'agg_data.csv'

load(clean_data, cd_data_path, agg_data, agg_data_path)


# Create the validation() function with one parameter: file_path - to check whether the previous function was correctly executed
def validation(file_path):
    return os.path.exists(file_path)

validation(cd_data_path)
validation(agg_data_path)

