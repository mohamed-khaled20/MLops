# MLops - API

This is a simple API for Covid-19 detection based on x-ray image



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#endpoints">Endpoints</a></li>
      <ul>
        <li><a href="#alive">alive</a></li>
        <li><a href="#predict">predict</a></li>
      </ul> 
    <li><a href="#usage">Usage</a></li>
      <ul>
        <li><a href="#requests">requests</a></li>
          <ul>
            <li><a href="#curl">curl</a></li>
            <li><a href="#python">python</a></li>
          </ul> 
      </ul>
    <li><a href="#error-codes">Error Codes</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
The main purpose of this project is to design web server for covid-19 detection based on x-ray images. Server is deployed and exposed to the client on heroku.

* The server can be found in [app.py](app.py)
* Deployment was done on [heroku](https://www.heroku.com/) since it support continous deployment by providing the option to link the app to specific github repo
* Server can be found [https://khaled-covid19-mlops.herokuapp.com](https://khaled-covid19-mlops.herokuapp.com)

### Built With

* [flask](https://flask.palletsprojects.com/)
* [requests](https://requests.readthedocs.io/)
* [tensorflow](https://www.tensorflow.org/)
* [Pillow](https://pillow.readthedocs.io/)
* [Numpy](https://numpy.org/)

<!-- endpoints -->
## Endpoints
Server has the following endpoints:

### alive
This endpoint aims to check if the service is up or not, and return a status code 200 in case the server is up and running.

* output (JSON)

|  Key       |     Type      |       Value   |
| -----------| ------------- | ------------- |
| `message`  |  String | Server is alive! |


### predict
This endpoint return the prediction of input x-ray image beside output distribution

* input (JSON)

|  Key             |     Type      |       Value   |
| -----------      | ------------- | ------------- |
| `file`           |  bytes        | image bytes |

* output (JSON)

|  Key             |     Type      |       Value   |
| -----------      | ------------- | ------------- |
| `result`         |  String       | NORMAL or COVID-19 |
| `distribution`   |  JSON         | { "COVID-19" : "%(covid19_percentage)",  "NORMAL" : "%(Normal_percentage)" }|




<!-- usage -->
## Usage
In this section, instruction will be given on how to send requests to the app and what are the different responses you should expect

### Requests
You can send request to the application using **CURL** or **Python**, both methods are tested and working fine.

#### curl
To send request to "alive" endpoint you can do the following:
```
curl -X 'GET' 'https://khaled-covid19-mlops.herokuapp.com/alive'
```

To send request to "predict" endpoint you can do the following:
```
curl -X POST -F file=@"$$file" https://khaled-covid19-mlops.herokuapp.com/predict
```

#### python
To send request to "alive" endpoint you can do the following:
```
import requests

res = requests.get('https://khaled-covid19-mlops.herokuapp.com/alive')
print ('response from server:',res.json())
```

To send request to "predict" endpoint you can do the following:
```
import requests

img_path = ""  ## path to image
file=open(img_path,"rb")
dicttosend={'file':file}
res = requests.post('https://khaled-covid19-mlops.herokuapp.com/predict',files=dicttosend)
print ('response from server:',res.json())
```

## Error Codes

### 400
This error can occur in two scenarios 

* Empty File
```
{"ERROR": "file you send is empty !!!"}
```

* File is not an image
```
{"ERROR": "file you send is not an image !!!"}
```

### 404
This error occur when you try to access undefined endpoint
```
{"ERROR": "Not a valid endpoint, you only have /alive or /predict"}
```

### 405
This error occur when you try to access endpoint with not allowed method
```
{"ERROR": "Not a valid method"}
```

### 500
This error occur when an error is occured in server-side
```
{"ERROR": "Internal server error"}
```
