import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient
from azure.storage.filedatalake import DataLakeServiceClient
import os

# Replace with your connection strings
BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
DATA_LAKE_CONNECTION_STRING = os.getenv("DATA_LAKE_CONNECTION_STRING")


app = func.FunctionApp(http_auth_level=func.AuthLevel.ADMIN)

@app.route(route="http_trigger")
def http_trigger_copy(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP_trigger_copy function processed a request.')
    
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    datalake_service_client = DataLakeServiceClient.from_connection_string(DATA_LAKE_CONNECTION_STRING)

    blob_container_name = "azpierrealexstorage"
    blob_name = "flightdata"

    datalake_file_system_name = "azdatalakepalexfilesystem"
    datalake_file_path = "https://azdatalakepalex.blob.core.windows.net/flightradardatacontainer"

    try:
        # Download blob data
        blob_client = blob_service_client.get_blob_client(container=blob_container_name, blob=blob_name)
        blob_data = blob_client.download_blob().readall()

        # Upload data to Data Lake
        file_system_client = datalake_service_client.get_file_system_client(file_system=datalake_file_system_name)
        file_client = file_system_client.get_file_client(datalake_file_path)
        file_client.upload_data(blob_data, overwrite=True)

        return func.HttpResponse(f"Blob data copied to Data Lake successfully.", status_code=200)
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Failed to copy blob data to Data Lake.", status_code=500)