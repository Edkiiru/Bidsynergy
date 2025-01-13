import requests
import base64
import os

# API endpoint URL with query string parameter
url = 'https://api.<xxx>'
 
#Path to the CSV file in the lakehouse
csv_path = '<xxx.csv>'

# Verify the file exists in the expected location
if os.path.isfile(csv_path):
    print(f"File found: {csv_path}")

    # Encode your CSV file to base64
    try:
        with open(csv_path, 'rb') as file:
            encoded_csv = base64.b64encode(file.read()).decode('utf-8')

        # Define the data to be sent
        data = {
            'name': 'xxxx.csv',
            'type': 'text/csv',
            'base64Data': encoded_csv  # Add your base64 encoded data here
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
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"File not found: {csv_path}")
