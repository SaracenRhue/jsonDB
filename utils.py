import json
import os


PATH = 'data'
def reload_db():
    db = {}
    for file in os.listdir(PATH):
        with open(f'{PATH}/{file}', 'r') as f:
            db[file[:-5]] = json.load(f)
    return db