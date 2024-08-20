import json
import requests
import sys

""" if len(sys.argv) != 2:
    sys.exit("Too few arguments") """

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])