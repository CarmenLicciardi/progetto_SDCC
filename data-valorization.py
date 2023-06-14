import json
import random

def get_lat() -> float:
    v1_lat = 24.396308
    v2_lat = 49.384358
    lat = random.uniform(v1_lat, v2_lat)
    return lat

def get_lon() -> float:
    v1_lon = -125.000000
    v2_lon = -66.934570
    lon = random.uniform(v1_lon, v2_lon)
    return lon

def create_geo_point(lat: float, lon: float) :
    geo_point = {
        "lat": lat,
        "lon": lon
    }
    return geo_point

input_file_path = "path"
output_file_path = "path"

# Apertura del file input
with open(input_file_path) as json_file:
    array_json = json.load(json_file)

# Modifica del campo "coordinates" per ogni oggetto JSON nell'array
for obj in array_json:
    # Verifica se il campo "coordinates" esiste nell'oggetto e se è un dizionario
    if obj.get('coordinates') is not None:
        print("Coordinates are populated")
    else:
        lat= get_lat()
        lon=get_lon()
        obj["coordinates"]=create_geo_point(lat,lon)


with open(output_file_path, "w") as tweetValorizzati:
    json.dump(array_json, tweetValorizzati, indent=4)

print("File creato e modificato con successo.")



