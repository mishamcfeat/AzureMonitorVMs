import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MinuteLocator, DateFormatter
from matplotlib.ticker import AutoMinorLocator

# Read the data from the CSV file
df = pd.read_csv('N:\CODE_MAIN\AZURE_MONITOR\data\metrics_data.csv')

# Convert the Timestamp column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set the Timestamp column as the index
df.set_index('Timestamp', inplace=True)

# Define the metrics of interest
metrics_of_interest = ['Percentage CPU', 'Available Memory Bytes']

# Create a single figure with two side-by-side subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# For each metric of interest
for i, metric in enumerate(metrics_of_interest):
    if metric in df['Metric'].unique():
        ax = axs[i]  # Use each subplot for plotting

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
        ax.legend()

        # Rotate x-axis labels for better visibility
        ax.tick_params(axis='x', rotation=45)

# Display the plots
plt.tight_layout()  # Adjust layout for better appearance
plt.show()