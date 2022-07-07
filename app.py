import flask
import requests
import json
import os
import magic
import tensorflow as tf

from tensorflow.keras.models import load_model
from flask import abort,jsonify
from predict import predict
from werkzeug.exceptions import HTTPException
from gevent.pywsgi import WSGIServer

os.environ["CUDA_VISIBLE_DEVICES"]="-1" 

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Welcome to X-ray covid-19 detection service"

@app.route("/alive", methods=["GET"])
def alive_endpoint():
    js={"message":"Server is alive!"}
    return js


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    global model
    img = flask.request.files['file'].read()

    check = magic.from_buffer(img,mime=True)
    if 'empty' in check:
        abort(400,"file you send is empty !!")
    elif check.split('/')[0].strip() != 'image':
        abort(400,"file you send is not an image !!!")


    result,dist = predict(model,img)
    response = {"result":result,"distribution":dist}
    return response


@app.errorhandler(Exception)
def handle_errors(e):
    if (e.code==400):  ## invliad endpoint 
        return {"ERROR":e.description},400
    if (e.code==404):  ## invliad endpoint 
        return {"ERROR":"Not a valid endpoint, you only have /alive or /predict"},404
    if (e.code==405):  ## invliad endpoint 
        return {"ERROR":"Not a valid method"},405
    if (e.code==500):  ## invliad endpoint 
        return {"ERROR":"Internal server error"},500

model_rel_path = "model_0.944.h5"
model_abs_path = os.path.abspath(model_rel_path)

model = load_model(model_abs_path)


