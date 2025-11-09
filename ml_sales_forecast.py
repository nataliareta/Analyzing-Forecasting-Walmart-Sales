import pandas as pd
import numpy as np

def clean_and_prepare_data(df, test_split_ratio=0.8):
    
    # Ubah kolom 'Date' menjadi datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
    
    # Sort data by Toko, Tanggal
    df = df.sort_values(by=['Store', 'Date']).reset_index(drop=True)
    
    # Format CPI (menghapus titik/koma yang salah)
    df['CPI'] = df['CPI'].astype(str).str.replace(r'[.,]', '', regex=True)
    
    # Asumsi: format asli adalah XXX.YYYYYY, kita pisahkan 7 angka terakhir --> desimal
    df['CPI'] = df['CPI'].apply(lambda x: x[:-7] + '.' + x[-7:] if len(x) > 7 else x)
    df['CPI'] = pd.to_numeric(df['CPI'], errors='coerce')

    # Membuat Fitur Temporal (Musiman)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Week_of_Year'] = df['Date'].dt.isocalendar().week.astype(int)
    
    # Membuat Fitur Lagged (Keterlambatan Penjualan)
    lags = [1, 2, 3, 52]
    
    for lag in lags:
        # Groupby 'Store' --> lag hanya berlaku di dalam satu toko
        df[f'Sales_Lag_{lag}'] = df.groupby('Store')['Weekly_Sales'].shift(lag)
    
    # Konversi ID Toko ke String/Kategori sebelum OHE (One-Hot Encoding)
    df['Store'] = df['Store'].astype('category')

    # OHE untuk Store ID, Month, dan Week_of_Year
    categorical_cols = ['Store', 'Month', 'Week_of_Year']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Hapus semua baris yang mengandung NaN
    df_final = df.dropna().reset_index(drop=True)
    
    # Variabel Target (Y)
    Y = df_final['Weekly_Sales']

    # Variabel Prediktor (X)
    kolom_dibuang = [
        'Date',  
        'Weekly_Sales',
        'Year',
        'Day_of_Week'   
    ]

    # Re-check
    existing_cols_to_drop = [col for col in kolom_dibuang if col in df_final.columns]
    X = df_final.drop(existing_cols_to_drop, axis=1)

    # Bagi Data secara Temporal (Training/Testing)
    total_rows = len(df_final)
    split_index = int(total_rows * test_split_ratio) 
    
    # Split Data
    X_train = X.iloc[:split_index]
    Y_train = Y.iloc[:split_index]
    X_test = X.iloc[split_index:]
    Y_test = Y.iloc[split_index:]

    # Tambah kolom 'Weekly_Sales' ke X_train/X_test --> penyimpanan lebih mudah
    X_train['Weekly_Sales'] = Y_train
    X_test['Weekly_Sales'] = Y_test

    return X_train, X_test

file_path = 'Clean_Walmart_Sales.csv' 

try:
    df_raw = pd.read_csv(file_path)
    print(f"File {file_path}")
    
    train_data_final, test_data_final = clean_and_prepare_data(df_raw.copy(), test_split_ratio=0.8)
    
    # Save data
    train_data_final.to_csv('walmart_train_data.csv', index=False)
    test_data_final.to_csv('walmart_test_data.csv', index=False)
    
    print("\n Berhasi, Natalia!")
    print(f"Data Training (walmart_train_data.csv) siap: {train_data_final.shape}")
    print(f"Data Testing (walmart_test_data.csv) siap: {test_data_final.shape}")

except FileNotFoundError:
    print(f"\n ERROR: File '{file_path}'!")