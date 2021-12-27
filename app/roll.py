import time

from common import get_counter, get_file

def ROLL_counter():
    file  = get_file()
    counter = get_counter()
    counter += 1
    for count in range(9):
        file.write(str(counter) + "\n")
        counter += 1
        time.sleep(50 / 1000)
    scnt = str(counter)
    return "Counter: /counter/roll  " + scnt
