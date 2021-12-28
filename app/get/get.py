from flask import Flask
app = Flask(__name__)

import sys
sys.path.append('/app/common')

from common import get_counter

def GET_counter():
	return str(get_counter())

@app.route("/counter/get/get")
def app_get_counter():
	return GET_counter()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
