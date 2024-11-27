import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsoncbv/'
resp = requests.post(BASE_URL+END_POINT)
data = resp.json()
print(data)
