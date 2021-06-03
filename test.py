import requests
import json


response = requests.get("https://v2.jokeapi.dev/joke/Any")
data = json.loads(response.text)
joke = "**" + data["setup"] + "**" + "\n ~ " + "*" + data["delivery"] + "*"
print(joke)
    


