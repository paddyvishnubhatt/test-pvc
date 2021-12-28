from flask import Flask
app = Flask(__name__)

import sys
sys.path.append('/app/common')

from common import get_counter, get_file

def RESET_counter():
    file = get_file()
    file.seek(0)
    file.truncate()
    scnt = str(get_counter())
    return scnt

@app.route("/counter/reset/reset", methods=["PUT","POST"])
def app_reset_counter():
	return RESET_counter()

if __name__ == "__main__":
    app.run(host='0.0.0.0')