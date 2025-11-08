import pandas as pd

# Read data
df = pd.read_csv('Walmart_Sales.csv')

# Set columns name
df.columns = ['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# Formatting date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

# Number - numeric
df['CPI'] = pd.to_numeric(df['CPI'], errors='coerce')
df['Unemployment'] = pd.to_numeric(df['Unemployment'], errors='coerce')

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Delete data (0 value)
df = df.dropna()

# Check Duplicate and Delete
df = df.drop_duplicates()

# Save File
df.to_csv('Clean_Walmart_Sales.csv', index=False)
print("Data disimpan!")

df = pd.read_csv('Clean_Walmart_Sales.csv')
print(df.head(10))