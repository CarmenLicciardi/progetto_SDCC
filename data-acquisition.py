from azure.storage.blob import BlobServiceClient
import json

STORAGEACCOUNTURL = "https://tweetarchive.blob.core.windows.net/"
STORAGEACCOUNTKEY = "key"
FILE_DIRECTORY = "path"
FILE_NAME = "tweet500.json"
LOCALFILENAME = FILE_DIRECTORY + "\\" + FILE_NAME
CONTAINERNAME = "carmen-tweet"
BLOBNAME = "tweet500.json"


try:
    blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
    blob_client_instance = blob_service_client_instance.get_blob_client(CONTAINERNAME, BLOBNAME, snapshot=None)

    # Download del file in memoria
    blob_data = blob_client_instance.download_blob()
    data = blob_data.readall()

    # Decodifica i dati in formato JSON
    decoded_data = data.decode("utf-8")

    # Carica i dati come oggetto JSON
    json_data = json.loads(decoded_data)

    # Salvataggio dei dati in formato JSON su un nuovo file locale
    with open(LOCALFILENAME, "w") as file:
        json.dump(json_data, file)

    print("Dati scaricati e salvati su file locale:", LOCALFILENAME)

except Exception as e:
    print("Si è verificato un errore durante il download dei dati:", str(e))
