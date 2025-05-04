import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

respose = requests.get("https://itunes.apple.com/search?entity=song&limit=&term=" + sys.argv[1])
"print(json.dumps(respose.json(), indent = 2))"

o = respose.json()
for result in o["results"]:
    print(result["trackName"])
