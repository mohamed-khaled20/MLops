import os
import io
import numpy as np

from PIL import Image,ImageOps
from flask import abort

def convert_probs(prob):
    return round(prob * 100,2)

def load_image(img):
    img = io.BytesIO(img)
    img = Image.open(img)
    resized_img = img.resize((256,256),resample=Image.BILINEAR)
    grayscale_resize_img = ImageOps.grayscale(resized_img)

    return grayscale_resize_img

def predict(model,img):
    try:
        loaded_img = load_image(img)
        loaded_img = np.asarray(loaded_img).reshape(1,256,256,1)
        probs = model.predict(loaded_img)[0][0]
    except:
        abort(500)

    result = "NORMAL" if probs >= 0.5 else "COVID19"

    return result,{"NORMAL":str(convert_probs(probs))+"%","COVID-19":str(convert_probs(1-probs))+"%"}


