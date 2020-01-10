import requests

# prints out the version of the requests library
print(requests.__version__)

# get the Google homepage
r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)

# downloads itself from GitHub and prints out its own source code from GitHub
r = requests.get("https://raw.githubusercontent.com/Whiteologist/CMPUT404/master/lab1.py")
print(r.status_code)
print(r.text)