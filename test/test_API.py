import flask
import requests
import json
import os
import magic
from flask import abort,jsonify
from werkzeug.exceptions import HTTPException
from gevent.pywsgi import WSGIServer
import sys

def test_alive():
  res = requests.get('https://khaled-covid19-mlops.herokuapp.com/alive')
  res_code = str(res.status_code)
  assert(res_code == "200")
  
def test_predict():
  img = open("NORMAL.png","rb")
  d   = {'file':img}
  res = requests.post('https://khaled-covid19-mlops.herokuapp.com/predict', files=d)
  res_code = str(res.status_code)
  assert(res_code == "200")
  
def test_wrong_endpoint():
  res = requests.get('https://khaled-covid19-mlops.herokuapp.com/alives')
  res_code = str(res.status_code)
  assert(res_code == "404")
  
def test_wrong_method():
  res = requests.post('https://khaled-covid19-mlops.herokuapp.com/alive')
  res_code = str(res.status_code)
  assert(res_code == "405")



