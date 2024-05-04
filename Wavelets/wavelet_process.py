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

def assign_filename(wavelet):
    if wavelet == 'db1':
        filename = 'haar'
    elif wavelet == 'sym2':
        filename = 'sym'
    elif wavelet == 'db2':
        filename = 'db'
    else:
        filename = wavelet
    
    return filename

def process_multiple_levels(df, levels, wavelet):
    results = {}
    filename = assign_filename(wavelet)
    for level in levels:
        processed_df = wrangle(df.copy(), level=level, wavelet=wavelet)
        processed_df.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)
        results[f'{filename}_lv{level}'] = processed_df
    return results


if __name__ == '__main__':
    df = pd.read_csv('sp500.csv')
    levels = range(2, 11)
    wavelets = ['db1', 'sym2', 'db2']

    for wavelet in wavelets:
        results = process_multiple_levels(df, levels, wavelet)
        for key, result_df in results.items():
            result_df.to_csv(f'{key}.csv', index=False)
