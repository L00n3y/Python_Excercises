import requests
import json
import argparse


#Argparse stuk
parser = argparse.ArgumentParser()
parser.add_argument("ip", help="voer ip adres in")
parser.add_argument("-v","--verbose",help="jemoeder", action='store_true')
args = parser.parse_args()

print(args.ip)

if(args.verbose):
    print("V switch set")

params = (
    ('62af19e73bf8c0', '$TOKEN'),
)

response = requests.get("http://ipinfo.io/{}/geo".format(args.ip), params=params)
data = json.loads(response.text)
if(args.verbose):
    for k, v in data.items():
        print("{} = {}".format(k, v))


