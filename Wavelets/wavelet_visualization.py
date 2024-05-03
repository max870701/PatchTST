import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Visualizing the signal time series in a dataframe
    df = pd.read_csv('db_lv2.csv')

    # Create a 2x2 grid of subplots
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    # Plot the original signal, approximation, and detail coefficients
    df['AdjClose'].plot(ax=ax[0, 0], title='Original Signal')
    df['Approx'].plot(ax=ax[0, 1], title='Approximation Coefficients')
    df['D1'].plot(ax=ax[1, 0], title='Detail Coefficients D1')
    df['D2'].plot(ax=ax[1, 1], title='Detail Coefficients D2')

    # Calculate the MSE and MAE between the original signal and the approximation
    mse = ((df['AdjClose'] - df['Approx']) ** 2).mean()
    mae = (df['AdjClose'] - df['Approx']).abs().mean()

    print(f'MSE: {mse:.2f}')
    print(f'MAE: {mae:.2f}')

    # Display the plot
    # plt.show()