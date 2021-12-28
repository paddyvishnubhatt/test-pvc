import os.path

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
