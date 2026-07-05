import pandas as pd
import numpy as np

def calculate_total_spending(df: pd.DataFrame) -> pd.DataFrame:
    spending_cols = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    df['TotalSpending'] = df[spending_cols].fillna(0).sum(axis=1)
    return df

def parse_cabin(df: pd.DataFrame) -> pd.DataFrame:
    split = df['Cabin'].str.split('/', expand=True)
    df['Deck'] = split[0]
    df['CabinNum'] = pd.to_numeric(split[1], errors='coerce')
    df['Side'] = split[2]
    return df

def filter_outliers_iqr(df: pd.DataFrame, column_name: str) -> pd.Series:
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask = (df[column_name] >= lower) & (df[column_name] <= upper)
    return df[mask]
