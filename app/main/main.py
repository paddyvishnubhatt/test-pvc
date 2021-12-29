from flask import request,Flask
app = Flask(__name__)

import requests
import logging
import json
logging.basicConfig(level=logging.INFO)

@app.route("/counter/reset", methods=["PUT","POST"])
def app_main_reset_counter():
    api_url = "http://reset-python-service:5000/counter/reset/reset"
    response = requests.put(api_url)
    return str(response.json())

@app.route("/counter/roll", methods=["PUT","POST"])
def app_main_roll_counter():
    api_url = "http://roll-python-service:5000/counter/roll/roll"
    body = {"increment": "2"}
    response = requests.post(api_url, data=body)
    return str(response.json())
    

@app.route("/counter/main", methods=["GET"])
@app.route("/counter/get", methods=["GET"])
@app.route("/counter", methods=["GET"])
@app.route("/")
def app_main_get_counter():
    app.logger.info("In app_main_get_counter v2")
    api_url = "http://get-python-service:5000/counter/get/get"
    response = requests.get(api_url)
    return str(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0')