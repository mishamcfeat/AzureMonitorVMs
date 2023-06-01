This project involves monitoring specific metrics of an Azure Virtual Machine and visualizing the metric data using Python.

Pre-requisites
•	An Azure account
•	Python installed locally (preferably Python 3.6 or later)
•	An Azure Virtual Machine
•	SSH access to the VM

Steps

Creating a VM
1.	Create a Linux virtual machine on Azure, noting down the VM name, subscription ID, and resource group for later.
2.	Set up SSH key authentication when creating the VM to allow secure access to the VM later.

Enabling Guest Level Monitoring
1.	Install the Azure Monitor extension for your VM to enable guest-level monitoring.
2.	Install the Azure diagnostics extension in your VM through the Azure portal.
3.	Enable 'Basic Metrics' in the 'Diagnostics settings' of your VM.

Installing Python Libraries on VM
1.	Connect to the Azure VM using SSH from your local machine.
2.	Once inside the VM, install Python 2 if not already installed.
3.	Install the azure-monitor Python library with pip install azure-monitor.

Setting up the Azure Monitor
1.	In the Azure portal, navigate to 'Monitor'.
2.	In the 'Metrics' section, add the metrics you're interested in. For this project, the metrics were 'Percentage CPU', 'Available Memory Bytes', 'Disk Read Bytes', 'Disk Write Bytes'.

Fetching Metrics with Python
1.	Install the necessary Python libraries locally with pip install azure-identity azure-monitor-query pandas matplotlib.
2.	Run the Python script to fetch the metrics from Azure Monitor and save them to a CSV file.

Data Processing and Analysis
1.	Use Pandas to read the CSV file.
2.	Transform the data if necessary, and analyze the metrics using the built-in functions of Pandas or with other Python libraries.
3.	Create visualizations for the metrics using matplotlib.
