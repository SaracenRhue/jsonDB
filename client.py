import httpx

SERVER = 'http://127.0.0.1:8000'

def pull(request):
    data = {'text': request}
    response = httpx.post(f'{SERVER}/get-data', json=data)
    return response.json()

def push(request):
    data = {'text': request}
    response = httpx.post(f'{SERVER}/set-data', json=data)
    return response.json()

result = pull('test0.a[0]')
print(result)