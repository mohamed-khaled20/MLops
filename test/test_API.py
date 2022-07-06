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
  res_code = json.loads(res)['code']
  assert(res_code == 200)



