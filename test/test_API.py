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
  res = requests.post('https://khaled-covid19-mlops.herokuapp.com/prediction', files=d)
  res_code = str(res.status_code)
  assert(res_code == "200")



