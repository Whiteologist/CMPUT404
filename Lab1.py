import requests

# prints out the version of the requests library
print(requests.__version__)

# get the Google homepage
r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)