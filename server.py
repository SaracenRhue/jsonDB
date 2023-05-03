from fastapi import FastAPI
from pydantic import BaseModel
import utils

app = FastAPI()
class InputData(BaseModel):
    text: str

db = utils.reload_db()
@app.post('/process-data')
async def process_data(data: InputData):
    query = data.text
    result = eval(query)              
    return result
