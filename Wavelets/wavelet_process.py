import pywt
import pandas as pd


def mra(df, level, wavelet='db2'):
    # Mutli-resolution analysis
    coeffs = pywt.wavedec(df['Adj Close'], wavelet, level=level)

    # Create a new dataframe
    for i in range(len(coeffs)):
        if i == 0:
            df[f'A{i}'] = list(coeffs[i]) + [None] * (len(df) - len(coeffs[i]))
        else:
            df[f'D{i}'] = [None] * (len(df) - len(coeffs[i])) + list(coeffs[i])

    return df

def get_null_cols(df):
    null_cols = [col for col in df.columns if df[col].isnull().any()]
    return null_cols

def fillna_numerical(df, cols):
    for col in cols:
        value = df[col].mode()[0]
        df[col].fillna(value, inplace=True)
    return df

def wrangle(df, level, wavelet='sym2'):
    new_df = mra(df, level, wavelet)
    null_cols = get_null_cols(new_df)
    new_df = fillna_numerical(new_df, null_cols)
    new_df['Target'] = new_df['Adj Close'].shift(-1)
    return new_df


if __name__ == '__main__':
    df = pd.read_csv('sp500.csv')

    # Decompose the data using the db2 wavelet in level 2 and 3
    db_lv2_df = wrangle(df.copy(), level=2, wavelet='db2')
    db_lv3_df = wrangle(df.copy(), level=3, wavelet='db2')

    # Decompose the data using the sym2 wavelet in level 2 and 3
    sym_lv2_df = wrangle(df.copy(), level=2, wavelet='sym2')
    sym_lv3_df = wrangle(df.copy(), level=3, wavelet='sym2')

    target = 'Target'
    drop_cols = [target, 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    # drop the columns
    db_lv2_df.drop(columns=drop_cols, axis=1, inplace=True)
    db_lv3_df.drop(columns=drop_cols, axis=1, inplace=True)

    sym_lv2_df.drop(columns=drop_cols, axis=1, inplace=True)
    sym_lv3_df.drop(columns=drop_cols, axis=1, inplace=True)

    # Save the dataframe to csv
    db_lv2_df.to_csv('db_lv2.csv', index=False)
    db_lv3_df.to_csv('db_lv3.csv', index=False)
    sym_lv2_df.to_csv('sym_lv2.csv', index=False)
    sym_lv3_df.to_csv('sym_lv3.csv', index=False)

