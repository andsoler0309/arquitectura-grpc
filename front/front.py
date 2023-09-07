import requests

for i in range(0, 100):
    response = requests.get("http://localhost:5000/register")
    print(response.text)