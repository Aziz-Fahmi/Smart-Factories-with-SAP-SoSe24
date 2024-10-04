import pandas as pd
import re

# Function to count null values in each column
def count_null_values(dataframe):
    null_counts = dataframe.isnull().sum()
    return null_counts

# Function to count duplicate rows
def count_duplicates(dataframe):
    duplicate_count = dataframe.duplicated().sum()
    return duplicate_count

# Function to remove timezone from the saledate
def remove_timezone(date_str):
    return re.sub(r' GMT[^\)]*\)', '', date_str)

# Define state abbreviation to full name mapping
state_mapping = {
    'ca': 'California',
    'tx': 'Texas',
    'mn': 'Minnesota',
    'az': 'Arizona',
    'wi': 'Wisconsin',
    'tn': 'Tennessee',
    'md': 'Maryland',
    'pa': 'Pennsylvania',
    'fl': 'Florida',
    'ne': 'Nebraska',
    'oh': 'Ohio',
    'mi': 'Michigan',
    'nj': 'New Jersey',
    'va': 'Virginia',
    'sc': 'South Carolina',
    'in': 'Indiana',
    'il': 'Illinois',
    'co': 'Colorado',
    'ut': 'Utah',
    'mo': 'Missouri',
    'ga': 'Georgia',
    'nv': 'Nevada',
    'ma': 'Massachusetts',
    'pr': 'Puerto Rico',
    'nc': 'North Carolina',
    'ny': 'New York',
    'or': 'Oregon',
    'la': 'Louisiana',
    'wa': 'Washington',
    'hi': 'Hawaii',
    'ok': 'Oklahoma',
    'ms': 'Mississippi',
    'nm': 'New Mexico',
    'al': 'Alabama'
}

# Load the dataset
df = pd.read_csv("C:/Users/Aziz/PycharmProjects/CarSales/car_prices_with_issues.csv")

# Replace state abbreviations with full names
df['state'] = df['state'].apply(lambda x: state_mapping.get(x.lower(), x))

# Remove null and NA values
df.dropna(inplace=True)

# Handle duplicates
df.drop_duplicates(inplace=True)

# Remove timezone information from 'saledate'
df['saledate'] = df['saledate'].apply(remove_timezone)

# Convert 'saledate' to a standard date format (MM/DD/YYYY)
df['saledate'] = pd.to_datetime(df['saledate'], format='%a %b %d %Y %H:%M:%S').dt.strftime('%m/%d/%Y')

# Save the cleaned data to a new CSV file
df.to_csv("C:/Users/Aziz/PycharmProjects/CarSales/clean_car_sales_data.csv", index=False)

print("Data cleaning complete. Cleaned data saved to 'clean_car_sales_data.csv'.")

# Get the number of null values in each column
null_values = count_null_values(df)
print("Number of null values in each column:")
print(null_values)

# Get the number of duplicate rows
duplicates = count_duplicates(df)
print(f"Number of duplicate rows: {duplicates}")
