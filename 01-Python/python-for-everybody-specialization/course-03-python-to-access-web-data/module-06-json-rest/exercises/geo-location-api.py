import json
import urllib.request, urllib.parse

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    params = dict()
    params['q'] = address

    url = serviceurl + urllib.parse.urlencode(params)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    print(json.dumps(js['features'][0]['properties']['plus_code'], indent=4))

 