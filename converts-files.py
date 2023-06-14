import json

def crea_array_da_file_json(input_file_path, output_file_path):
    array_json = []

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line:
                try:
                    obj = json.loads(line)
                    array_json.append(obj)
                except json.JSONDecodeError:
                    print(f"Errore nella decodifica della riga JSON: {line}")

    array_json_str = json.dumps(array_json, indent=4)

    with open(input_file_path, 'w') as output_file:
        output_file.write(array_json_str)

    print("Array JSON creato con successo.")

input_file_path = "path"
output_file_path = "path"
crea_array_da_file_json(input_file_path, output_file_path)