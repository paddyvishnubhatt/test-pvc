import time
from flask import Flask
app = Flask(__name__)

import sys
sys.path.append('/app/common')

from common import get_counter, get_file

def ROLL_counter():
    file  = get_file()
    counter = get_counter()
    counter += 1
    for count in range(9):
        file.write(str(counter) + "\n")
        counter += 1
        time.sleep(50 / 1000)
    return str(counter)

@app.route("/counter/roll/roll", methods=["PUT","POST"])
def app_roll_counter():
	return ROLL_counter()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
