import json
from elasticsearch import Elasticsearch

def conn_es():

    # Crea una connessione a Elasticsearch
    es = Elasticsearch(
        hosts=['http://localhost:9200'],
        basic_auth=('elastic', 'password')
    )

    # Verifica la connessione
    if es.ping():
        print("Connessione a Elasticsearch riuscita.")
    else:
        print("Connessione a Elasticsearch non riuscita.")

    return es

def create_index(index_name):
    # Definisci il mapping per i campi del tweet
    setting = {
        "settings": {
            "index.mapping.total_fields.limit": 3000,
        },
        "mappings": {
            "properties": {
                "coordinates": {
                    "type": "geo_point"
                },
                "created_at": {
                    "type": "date",
                    "format": "EEE MMM dd HH:mm:ss Z yyyy"
                }
            }
        }
    }

    # Crea l'indice con il mapping specificato
    response = es.indices.create(index=index_name, body=setting)

    # Controlla se l'operazione è andata a buon fine
    if response["acknowledged"]:
        print("Indice creato con successo!")
    else:
        print("Errore durante la creazione dell'indice:", response)


# Configurazione di Elasticsearch
es = conn_es()

# Nome dell'indice
index_name = "index_tweet"

# Percorso del file JSON da indicizzare
file_path = "path"

#creazione indice
if not es.indices.exists(index=index_name):
    create_index(index_name)
print("Indice già esistente!")


# Apri il file in modalità lettura
with open(file_path, 'r') as file:
    # Carica il contenuto del file come stringa JSON
    json_string = file.read()
    print("Contenuto caricato")
    # Converti la stringa JSON in un oggetto Python
    json_data = json.loads(json_string)
    print("Stringa convertita")

    # Itera sugli oggetti JSON uno per uno
    for oggetto in json_data:
         response = es.index(index=index_name, document=oggetto)















