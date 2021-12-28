from flask import Flask
app = Flask(__name__)

import sys
sys.path.append('/app/reset')
sys.path.append('/app/get')
sys.path.append('/app/roll')

from reset import RESET_counter
from get import GET_counter
from roll import ROLL_counter

@app.route("/counter/reset")
def app_reset_counter():
    return RESET_counter()

@app.route("/counter/roll")
def app_roll_counter():
	return ROLL_counter()

@app.route("/counter/main")
@app.route("/counter/get")
@app.route("/counter")
@app.route("/")
def app_get_counter():
	return GET_counter()

if __name__ == "__main__":
    app.run(host='0.0.0.0')