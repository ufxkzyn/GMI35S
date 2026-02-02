import requests
import json
import requests
import webbrowser



x = 0
while (x < 10):
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    data = response.json()
    webbrowser.open_new_tab(data['message'])
    x = x + 1

