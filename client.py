import httpx

SERVER = "http://127.0.0.1:8000"

def pull(request):
    data = {"text": request}
    response = httpx.post(f"{SERVER}/process-data", json=data)
    return response.json()

result = pull("db['test']")
print(result)