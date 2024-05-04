import pandas as pd
import matplotlib.pyplot as plt


def plot_raw_and_wavelet(wavelet_df, wavelet_name, level):
    # Create a 2x2 grid of subplots
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    # Plot the original signal, approximation, and detail coefficients
    wavelet_df['AdjClose'].plot(ax=ax[0, 0], title='Original Signal')
    wavelet_df['Approx'].plot(ax=ax[0, 1], title='Approximation Coefficients')

    for i in range(level):
        wavelet_df[f'D{i+1}'].plot(ax=ax[1, i], title=f'Detail Coefficients D{i+1}')

    # Set the title of the plot
    fig.suptitle(f'Using {wavelet_name} Wavelet at Level {level}')

    # Show the MSE, MAE on the plot
    mse = ((wavelet_df['AdjClose'] - wavelet_df['Approx']) ** 2).mean()
    mae = (wavelet_df['AdjClose'] - wavelet_df['Approx']).abs().mean()

    # Display the MSE and MAE on the plot
    fig.text(0.5, 0.05, f'MSE: {mse:.2f}', ha='center')
    fig.text(0.5, 0.02, f'MAE: {mae:.2f}', ha='center')

    # Display the plot
    plt.show()


if __name__ == "__main__":
    # Visualizing the signal time series in a dataframe
    df = pd.read_csv('haar_lv2.csv')

    # Plot the raw signal and wavelet coefficients
    plot_raw_and_wavelet(
        wavelet_df=df,
        wavelet_name='db1',
        level=2
    )