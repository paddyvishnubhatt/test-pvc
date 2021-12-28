from common import get_counter

def GET_counter():
	scnt = str(get_counter())
	return "Counter: /counter/get " + scnt

if __name__ == "__main__":
    app.run(host='0.0.0.0')
