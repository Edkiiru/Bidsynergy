import requests
import base64
import os
import glob
from datetime import datetime
import pytz

# API endpoint URL with query string parameter
url = 'https://api<your API>'

# Directory containing the CSV files
csv_directory = '<xxxCsv>'

# Function to fetch CSV files from the given directory
def fetch_csv_files(directory):
    csv_files = glob.glob(os.path.join(directory, "*.csv"))
    return csv_files

# Fetch the CSV files
csv_files = fetch_csv_files(csv_directory)

# Check if CSV files are found
if csv_files:
    print(f"Found CSV files: {csv_files}")

    # Process each CSV file
    for csv_path in csv_files:
        print(f"Processing file: {csv_path}")

        # Verify the file exists in the expected location
        if os.path.isfile(csv_path):
            print(f"File found: {csv_path}")

            # Generate new filename using Central Time (USA)
            central_time = datetime.now(pytz.timezone('US/Central'))
            current_time = central_time.strftime("%Y%m%d%H%M%S")
            new_filename = f"ContractOpportunities_{current_time}.csv"
            new_csv_path = os.path.join(os.path.dirname(csv_path), new_filename)
            
            # Rename the file
            os.rename(csv_path, new_csv_path)
            print(f"Renamed file to: {new_csv_path}")

            # Encode your CSV file to base64
            try:
                with open(new_csv_path, 'rb') as file:
                    encoded_csv = base64.b64encode(file.read()).decode('utf-8')

                # Define the data to be sent
                data = {
                    'name': new_filename,  # Use the new filename
                    'type': 'text/csv',
                    'base64Data': encoded_csv,  # Add your base64 encoded data here
                    'overwrite': True  # Indicate that the file should be overwritten
                }

                # Make the API call
                response = requests.post(url, json=data)

                # Check the response status
                if response.status_code == 200:
                    print("API call successful!")
                else:
                    print("API call failed with status code:", response.status_code)
                    print("Error message:", response.text)

            except FileNotFoundError:
                print(f"File not found: {new_csv_path}")
            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print(f"File not found: {csv_path}")

else:
    print(f"No CSV files found in the directory: {csv_directory}")
