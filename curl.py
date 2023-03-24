import requests, json

response = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/Dolphin')
variable = json.loads(response.text)
variable = json.dumps(variable, indent = 2)
print(variable)
