from fastapi import FastAPI
from pydantic import BaseModel
import utils

app = FastAPI()
class InputData(BaseModel):
    text: str


@app.post('/get-data')
async def get_data(data: InputData):
    query = data.text
    if query == 'tables': 
        return utils.list_tables()
    else:
        query = utils.convert_string(query)
        table = query.split('[', 1)[0]
        query = query.replace(table, '')
        table = utils.get_table(table)
        result = eval('table'+query)              
        return result


@app.post('/set-data')
async def set_data(data: InputData):
    query = data.text

    query = utils.convert_string(query)
    table = query.split('[', 1)[0]
    query = query.replace(table, '')
    table = utils.get_table(table)
    result = 'updated'             
    return result
