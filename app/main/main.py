from flask import request,Flask
app = Flask(__name__)

import requests
import json

@app.route("/counter/reset", methods=["PUT","POST"])
def app_main_reset_counter():
    api_url = "http://reset-python-service:5000/counter/reset/reset"
    response = requests.put(api_url)
    return str(response.json())

@app.route("/counter/roll", methods=["PUT","POST"])
def app_main_roll_counter():
    api_url = "http://roll-python-service:5000/counter/roll/roll"
    print("In 2.0")
    response = requests.put(api_url, data=request.form)
    return str(response.json())
    

@app.route("/counter/main", methods=["GET"])
@app.route("/counter/get", methods=["GET"])
@app.route("/counter", methods=["GET"])
@app.route("/")
def app_main_get_counter():
    api_url = "http://get-python-service:5000/counter/get/get"
    response = requests.get(api_url)
    return str(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0')