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
  res = requests.get('https://127.0.0.1:5000')
  res_code = str(res).split('[')[1].split(']')[0]
  assert(res_code == 200)



