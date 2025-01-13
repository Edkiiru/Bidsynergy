import requests
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Basecamp API credentials
basecamp_token = "YOUR_BASECAMP_TOKEN"
basecamp_project_id = "YOUR_BASECAMP_PROJECT_ID"
basecamp_upload_url = f"https://3.basecampapi.com/xxxxxxx/uploads.json"

# Azure Blob Storage credentials
azure_storage_connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
azure_container_name = "YOUR_AZURE_CONTAINER_NAME"
azure_blob_name = "YOUR_AZURE_BLOB_NAME"

# Authenticate with Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)

# Get the blob container and blob
container_client = blob_service_client.get_container_client(azure_container_name)
blob_client = container_client.get_blob_client(azure_blob_name)

# Download the blob from Azure Blob Storage
downloaded_blob = blob_client.download_blob()

# Upload the blob to Basecamp docs and files
upload_headers = {
    "Authorization": f"Bearer {basecamp_token}",
    "Content-Type": "application/octet-stream",
    "Content-Disposition": f"attachment; filename={azure_blob_name}"
}
upload_data = downloaded_blob.readall()
response = requests.post(basecamp_upload_url, headers=upload_headers, data=upload_data)

# Check the response status
if response.status_code == 201:
    print("File uploaded successfully to Basecamp.")
else:
    print("Failed to upload file to Basecamp.")
