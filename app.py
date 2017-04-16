import requests, time, json

payload = {"result": {
    "source": "agent",
    "resolvedQuery": "beef",
    "action": "ingredients",
    "parameters": {
      "ingredients": "steak"
    }}}
r = requests.post('https://fathomless-basin-55854.herokuapp.com/webhook', data=json.dumps(payload))
print r.status_code
print r.content