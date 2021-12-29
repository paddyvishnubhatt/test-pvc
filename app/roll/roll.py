import time
from flask import request, Flask
app = Flask(__name__)

import sys
sys.path.append('/app/common')
import logging
logging.basicConfig(level=logging.INFO)

from common import get_counter, get_file

def ROLL_counter(increment):
    file  = get_file()
    counter = get_counter()
    counter += 1
    for count in range(increment-1):
        file.write(str(counter) + "\n")
        counter += 1
        time.sleep(50 / 1000)
    return str(counter)

@app.route("/counter/roll/roll", methods=["PUT","POST"])
def app_roll_counter():
    data = request.form
    increment = 10
    #app.logger.info("In app_roll_counter " + str(data))    
    if data is not None:
        inc = data.get("increment")
        if inc is not None:
            increment = int(inc)
    app.logger.info("In app_roll_counter " + str(increment))
    return ROLL_counter(increment)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
