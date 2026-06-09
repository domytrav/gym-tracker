import json

def caricaDati():
    with open("database.json", "r") as file:
        return json.load(file)

def salvaDati(dati):
    with open("database.json", "w") as file:
        json.dump(dati, file, indent=4)


