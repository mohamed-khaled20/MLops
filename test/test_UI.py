import requests

URL = "https://khaled-covid19-mlops.herokuapp.com"

def test_server():
  res = requests.get(URL + '/alive').json()
  assert(res)
  
  
  
  
