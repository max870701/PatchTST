import pywt
import pandas as pd


def discrete_decomposition(df, level, wavelet='db1'):
    # Extract closing prices assuming the relevant data is in a column named 'Close'
    closing_prices = df['AdjClose']  

    # Decompose the signal
    coeffs = pywt.wavedec(closing_prices, wavelet, level=level)

    # Separate approximation and detail coefficients
    approx_coeffs = coeffs[0]
    detail_coeffs = coeffs[1:]

    # Generate a dataframe with the approximation and detail coefficients
    # Upsample the coefficients to match the length of the original data
    df['Approx'] = pywt.upcoef('a', approx_coeffs, wavelet, level=level, take=len(closing_prices))
    for i, detail_coeff in enumerate(detail_coeffs):
        df[f'D{i+1}'] = pywt.upcoef('d', detail_coeff, wavelet, level=level, take=len(closing_prices))

    return df

def get_null_cols(df):
    null_cols = [col for col in df.columns if df[col].isnull().any()]
    return null_cols

def fillna_numerical(df, cols):
    for col in cols:
        value = df[col].mode().get(0, df[col].iloc[0])  # Default to the first item if mode is empty
        df[col] = df[col].fillna(value)
    return df

def wrangle(df, level, wavelet='sym2'):
    new_df = discrete_decomposition(df, level, wavelet)
    # print(new_df.head())
    null_cols = get_null_cols(new_df)
    new_df = fillna_numerical(new_df, null_cols)
    new_df['Target'] = new_df['AdjClose'].shift(-1)
    return new_df


if __name__ == '__main__':
    df = pd.read_csv('sp500.csv')

    # Decompose the data using the db2 wavelet in level 2 and 3
    haar_lv2_df = wrangle(df.copy(), level=2, wavelet='db1')
    haar_lv3_df = wrangle(df.copy(), level=3, wavelet='db1')
    haar_lv4_df = wrangle(df.copy(), level=4, wavelet='db1')

    # Decompose the data using the sym2 wavelet in level 2 and 3
    sym_lv2_df = wrangle(df.copy(), level=2, wavelet='sym2')
    sym_lv3_df = wrangle(df.copy(), level=3, wavelet='sym2')
    sym_lv4_df = wrangle(df.copy(), level=4, wavelet='sym2')

    # Decompose the data using the db2 wavelet in level 2 and 3
    db_lv2_df = wrangle(df.copy(), level=2, wavelet='db2')
    db_lv3_df = wrangle(df.copy(), level=3, wavelet='db2')
    db_lv4_df = wrangle(df.copy(), level=4, wavelet='db2')

    drop_cols = ['Open', 'High', 'Low', 'Close', 'Volume']

    # drop the columns
    haar_lv2_df.drop(columns=drop_cols, axis=1, inplace=True)
    haar_lv3_df.drop(columns=drop_cols, axis=1, inplace=True)
    haar_lv4_df.drop(columns=drop_cols, axis=1, inplace=True)

    sym_lv2_df.drop(columns=drop_cols, axis=1, inplace=True)
    sym_lv3_df.drop(columns=drop_cols, axis=1, inplace=True)
    sym_lv4_df.drop(columns=drop_cols, axis=1, inplace=True)

    db_lv2_df.drop(columns=drop_cols, axis=1, inplace=True)
    db_lv3_df.drop(columns=drop_cols, axis=1, inplace=True)
    db_lv4_df.drop(columns=drop_cols, axis=1, inplace=True)

    # Save the dataframe to csv
    haar_lv2_df.to_csv('haar_lv2.csv', index=False)
    haar_lv3_df.to_csv('haar_lv3.csv', index=False)
    haar_lv4_df.to_csv('haar_lv4.csv', index=False)

    sym_lv2_df.to_csv('sym_lv2.csv', index=False)
    sym_lv3_df.to_csv('sym_lv3.csv', index=False)
    sym_lv4_df.to_csv('sym_lv4.csv', index=False)

    db_lv2_df.to_csv('db_lv2.csv', index=False)
    db_lv3_df.to_csv('db_lv3.csv', index=False)
    db_lv4_df.to_csv('db_lv4.csv', index=False)

    # Decompose sym2 wavelet in level 10
    sym_lv10_df = wrangle(df.copy(), level=10, wavelet='sym2')
    sym_lv10_df.drop(columns=drop_cols, axis=1, inplace=True)
    sym_lv10_df.to_csv('sym_lv10.csv', index=False)

    # Decompose db2 wavelet in level 10
    db_lv10_df = wrangle(df.copy(), level=10, wavelet='db2')
    db_lv10_df.drop(columns=drop_cols, axis=1, inplace=True)
    db_lv10_df.to_csv('db_lv10.csv', index=False)

    # Decompose haar wavelet in level 10
    haar_lv10_df = wrangle(df.copy(), level=10, wavelet='db1')
    haar_lv10_df.drop(columns=drop_cols, axis=1, inplace=True)
    haar_lv10_df.to_csv('haar_lv10.csv', index=False)
