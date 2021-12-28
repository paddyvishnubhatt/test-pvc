import sys
sys.path.append('/app/common')

from common import get_counter, get_file

def RESET_counter():
    file = get_file()
    file.seek(0)
    file.truncate()
    scnt = str(get_counter())
    return "Counter: /counter/reset " + scnt
