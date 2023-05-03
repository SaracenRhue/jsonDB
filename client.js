const SERVER = 'http://127.0.0.1:8000';

async function pull(request) {
  const fetch = await import('node-fetch');
  const data = { text: request };
  const response = await fetch.default(`${SERVER}/process-data`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return response.json();
}

(async () => {
  const result = await pull("test.a");
  console.log(result);
})();
