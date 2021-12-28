from flask import Flask
app = Flask(__name__)

import requests

@app.route("/counter/reset", methods=["PUT","POST"])
def app_main_reset_counter():
    api_url = "http://reset-python-service:7000/counter/reset/reset"
    response = requests.put(api_url)
    return str(response.json())

@app.route("/counter/roll", methods=["PUT","POST"])
def app_main_roll_counter():
    api_url = "http://roll-python-service:8000/counter/roll/roll"
    response = requests.put(api_url)
    return str(response.json())

@app.route("/counter/main")
@app.route("/counter/get")
@app.route("/counter")
@app.route("/")
def app_main_get_counter():
    api_url = "http://get-python-service:6000/counter/get/get"
    response = requests.get(api_url)
    return str(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0')