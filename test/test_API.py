import flask
import requests
import json
import os
import magic
from flask import abort,jsonify
from werkzeug.exceptions import HTTPException
from gevent.pywsgi import WSGIServer
import sys

os.chdir("/home/runner/work/MLops/MLops")
from app import app

app.run(debug=True)

def test_alive():
  res = requests.get('0.0.0.0:5000')
  res_code = str(res).split('[')[1].split(']')[0]
  assert(res_code == 200)



