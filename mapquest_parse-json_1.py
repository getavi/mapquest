import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
# orig = "Washington, D.C."
# dest = "Baltimore, Md"
orig = "Roma, Italia"
dest = "Frascati, Italia"
key = "IL9V8SSG9WeztsjdMaS80zvdkEf5rl8M"

url = main_api + urllib.parse.urlencode({'key': key, "from": orig, 'to': dest})

json_data = requests.get(url).json()
print(json_data)
