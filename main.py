from fastapi import FastAPI, File, UploadFile
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = FastAPI()

connection_string="DefaultEndpointsProtocol=https;AccountName=bhavs222;AccountKey=T6QjWXTRBFqHG6rAZQ2dpuXP+zqMANaktqbCm1EpFChHvGoSyVS6Q/L7HsU0A+A+HnsYc5MnMDqU+AStPusBaw==;EndpointSuffix=core.windows.net"

container_name="input"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

@app.post("/uploadfile/")
def create_upload_file(uploadedFile: UploadFile):
    # Upload the created file
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=uploadedFile.filename)
    blob_client.upload_blob(uploadedFile.file.read())
    return {"filename": uploadedFile.filename}