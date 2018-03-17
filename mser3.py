from jitpy import setup
setup('<path-to-pypy-home>')
import time
from jitpy.wrapper import *

start_time = time.time()


@jittify([int, float], float)
def func(count, no):
    s = 0
    for i in range(count):
        s += no
    return s


func(100000, 1.2)

print("--- %s seconds ---" % (time.time() - start_time))
