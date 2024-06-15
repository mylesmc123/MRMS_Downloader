#%% 
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import xarray as xr
import glob

#%%
# Define the base URL
base_url = "https://mtarchive.geol.iastate.edu/{}/{:02d}/{:02d}/mrms/ncep/GaugeCorr_QPE_01H/"

# Define the start and end dates
start_date = datetime.strptime("2017/08/20", "%Y/%m/%d")
end_date = datetime.strptime("2017/09/05", "%Y/%m/%d")

# Define the directory to save the downloaded files
save_directory = "output"

# Ensure the save directory exists
os.makedirs(save_directory, exist_ok=True)

#%%
# Loop through each date in the range
current_date = start_date
while current_date <= end_date:
    # Format the URL for the current date
    url = base_url.format(current_date.year, current_date.month, current_date.day)
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links in the HTML
        for link in soup.find_all('a'):
            # Get the href attribute of the link
            file_url = link.get('href')
            
            # Check if the link is a file (ends with .gz)
            if file_url.endswith('.gz'):
                # Build the full file URL
                file_url = url + file_url
                
                # Define the path to save the file
                save_path = os.path.join(save_directory, os.path.basename(file_url))
                
                # Download and save the file
                with open(save_path, 'wb') as f:
                    f.write(requests.get(file_url).content)
                
                print(f"Downloaded {file_url} to {save_path}")
    else:
        print(f"Failed to access {url}")
    
    # Move to the next date
    current_date += timedelta(days=1)
    
# %%
# unzip the files in the output directory
os.system(f"gunzip {save_directory}/*.gz")

# %%
# Run through Vortex to get DSS 