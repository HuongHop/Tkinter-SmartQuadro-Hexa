import requests

data = 'teste'

post = requests.post("http://35.162.112.238:3000", timeout = 100)

print(post.status_code)