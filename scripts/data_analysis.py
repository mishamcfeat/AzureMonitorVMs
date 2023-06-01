import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MinuteLocator, DateFormatter
from matplotlib.ticker import AutoMinorLocator

# Read the data from the CSV file
df = pd.read_csv('../data/metrics_data.csv')

# Convert the Timestamp column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set the Timestamp column as the index
df.set_index('Timestamp', inplace=True)

# Define the metrics of interest
metrics_of_interest = ['Percentage CPU', 'Available Memory Bytes']

# For each metric of interest
for metric in metrics_of_interest:
    if metric in df['Metric'].unique():
        # Create a figure and a set of subplots
        fig, ax = plt.subplots()

        # Add labels and title
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.set_title(f'{metric} Over Time')

        # Create grid and configure X axis
        ax.grid(True, which='both', linestyle='-', linewidth=0.5)
        ax.xaxis.set_major_locator(MinuteLocator(interval=5))  # Major ticks every 5 minutes
        ax.xaxis.set_minor_locator(MinuteLocator(interval=1))  # Minor ticks every minute
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))  # Format timestamp as HH:MM

        # Create minor ticks on Y axis
        ax.yaxis.set_minor_locator(AutoMinorLocator())

        # Add a box around the plot
        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(True)

        # Plot the data for the current metric
        df[df['Metric'] == metric]['Value'].plot(ax=ax, label=metric)
        plt.legend()

        # Rotate x-axis labels for better visibility
        plt.xticks(rotation=45)

        plt.show()
