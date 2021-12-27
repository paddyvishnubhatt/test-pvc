from common import get_counter

def GET_counter():
	scnt = str(get_counter())
	return "Counter: /counter/get " + scnt
