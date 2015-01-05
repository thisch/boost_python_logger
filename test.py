import logging
import sys
import time

def set_level(level='WARNING'):
    for lname in ('', 'dolfin', 'mshr'):
        logging.getLogger(lname).setLevel(level)

rootlogger = logging.getLogger('')
try:
    from falafel.logger import Formatter
    set_level()
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(Formatter())
    rootlogger.addHandler(sh)
except ImportError:
    logging.basicConfig(level='DEBUG')

print("rootlogger level %s" % rootlogger.level)
print("dolfin level %s" % logging.getLogger('dolfin').level)
print("mshr level %s" % logging.getLogger('mshr').level)

import hello

for level in ['DEBUG', 'INFO', 'ERROR', 'WARNING']:
    print((" test.py: set loglevel to '%s' " % level).center(80, '#'))
    set_level(level)

    # whenever we update the loggers (from the python side) we need to call
    hello.setLogger()

    hello.say_hello('aaaa2')
    time.sleep(0.5)

    # hello.setLogger(a)
    hello.say_hello('aaaa3')

    hello.other()
