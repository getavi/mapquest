import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "IL9V8SSG9WeztsjdMaS80zvdkEf5rl8M"

while True:
    orig = input("Starting Location: ")
    if orig == 'q' or orig == 'quit':
        break
    dest = input("Destination: ")
    if dest == 'q' or dest == 'quit':
        break
    
    url = main_api + urllib.parse.urlencode({'key': key, "from": orig, 'to': dest})
    print('URL: ' + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        # print("Miles:           " + str(json_data["route"]["distance"]))
        # print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")

