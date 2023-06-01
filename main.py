import os
from datetime import timedelta, datetime
import pytz
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.monitor.query import MetricsQueryClient

credential = DefaultAzureCredential()

metrics_uri = "/subscriptions/b632c94b-9639-44a4-bb4c-64ac99007e0e/resourceGroups/cloud-shell-storage-westeurope/providers/Microsoft.Compute/virtualMachines/projectTest"
metrics_client = MetricsQueryClient(credential)

bst = pytz.timezone('Europe/London')
start_time = datetime.now(tz=bst) - timedelta(minutes=60)
duration = timedelta(minutes=60)

response = metrics_client.query_resource(
    metrics_uri,
    ["Percentage CPU", "Available Memory Bytes"],
    timespan=(start_time, duration)
)

df = pd.DataFrame(columns=['Metric', 'Timestamp', 'Value'])

for metric in response.metrics:
    for time_series_element in metric.timeseries:
        for metric_value in time_series_element.data:
            df = df.append({
                'Metric': metric.name,
                'Timestamp': metric_value.timestamp,
                'Value': metric_value.average
            }, ignore_index=True)

# Save the DataFrame to a CSV file in the 'data' folder
df.to_csv('data/metrics_data.csv', index=False)
