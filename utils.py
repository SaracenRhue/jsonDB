import json
import os

PATH = 'data'

def get_table(table):
    with open(f'{PATH}/{table}.json', 'r') as f:
        return json.load(f)

def list_tables():
    return [x[:-5] for x in os.listdir(PATH)]

def reload_db():
    db = {}
    for file in os.listdir(PATH):
        with open(f'{PATH}/{file}', 'r') as f:
            db[file[:-5]] = json.load(f)
    return db

def convert_string(input_str):
    output_str = ""
    parts = input_str.split(".")
    
    for i, part in enumerate(parts):
        if i > 0:
            output_str += "['"
        
        if "[" in part:
            sub_parts = part.split("[", 1)
            output_str += sub_parts[0]
            
            if i > 0:
                output_str += "']"
                
            output_str += f"[{sub_parts[1]}"
        else:
            output_str += part
    
    return output_str