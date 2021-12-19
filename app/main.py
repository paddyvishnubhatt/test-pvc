import time
import os.path
import flask

from flask import Flask
app = Flask(__name__)

def get_file():
	fname = '/mnt/counters/counter.txt'
	file_exists = os.path.exists(fname)
	mode = 'a+'
	if file_exists:
		mode = 'r+'
	file = open(fname, mode)
	return file

def get_counter():
	file  = get_file()
	counter = 0
	lines = file.readlines()
	if lines:
		last_line = lines[-1]
		counter = int(last_line) 
	return counter +  1

def run_counter():
	file  = get_file()
	counter = get_counter()
	counter += 1
	for count in range(9):
		file.write(str(counter) + "\n")
		counter += 1
		time.sleep(50 / 1000)

@app.route("/")
def hello():
	scnt = str(get_counter())
	run_counter()
	return "Pady is great " + scnt

if __name__ == "__main__":
    app.run(host='0.0.0.0')