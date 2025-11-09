import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def clean_and_prepare_data(df, test_split_ratio=0.8):

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
    df = df.sort_values(by=['Store', 'Date']).reset_index(drop=True)
    df['CPI'] = df['CPI'].astype(str).str.replace(r'[.,]', '', regex=True)
    df['CPI'] = df['CPI'].apply(lambda x: x[:-7] + '.' + x[-7:] if len(x) > 7 else x)
    df['CPI'] = pd.to_numeric(df['CPI'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Week_of_Year'] = df['Date'].dt.isocalendar().week.astype(int)

    lags = [1, 2, 3, 52]
    for lag in lags:
        df[f'Sales_Lag_{lag}'] = df.groupby('Store')['Weekly_Sales'].shift(lag)


    df['Store'] = df['Store'].astype('category')
    categorical_cols = ['Store', 'Month', 'Week_of_Year']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Hapus NaN dan tentukan X, Y
    df_final = df.dropna().reset_index(drop=True)
    Y = df_final['Weekly_Sales']
    
    kolom_dibuang = ['Date', 'Weekly_Sales', 'Year', 'Day_of_Week']
    existing_cols_to_drop = [col for col in kolom_dibuang if col in df_final.columns]
    X = df_final.drop(existing_cols_to_drop, axis=1)
    
    scaling_cols = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

    total_rows = len(df_final)
    split_index = int(total_rows * test_split_ratio) 
    
    X_train_raw = X.iloc[:split_index].copy()
    X_test_raw = X.iloc[split_index:].copy()
    Y_train = Y.iloc[:split_index]
    Y_test = Y.iloc[split_index:]

    scaler = StandardScaler()
    scaler.fit(X_train_raw[scaling_cols])
    
    X_train_raw[scaling_cols] = scaler.transform(X_train_raw[scaling_cols])
    X_test_raw[scaling_cols] = scaler.transform(X_test_raw[scaling_cols])

    X_train_raw['Weekly_Sales'] = Y_train
    X_test_raw['Weekly_Sales'] = Y_test

    return X_train_raw, X_test_raw

file_path = 'Clean_Walmart_Sales.csv' 

try:
    df_raw = pd.read_csv(file_path)
    print(f"File {file_path} berhasil dimuat.")

    train_data_final, test_data_final = clean_and_prepare_data(df_raw.copy(), test_split_ratio=0.8)

    train_data_final.to_csv('walmart_train_data.csv', index=False)
    test_data_final.to_csv('walmart_test_data.csv', index=False)

    print(f"Data Training (walmart_train_data.csv) siap: {train_data_final.shape}")
    print(f"Data Testing (walmart_test_data.csv) siap: {test_data_final.shape}")

except FileNotFoundError:
    print(f"\n ERROR: File '{file_path}'!")