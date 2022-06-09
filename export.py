from random import randrange
import time
from prometheus_client import start_http_server, Gauge

RANDOM_NUMBER_GAUGE = Gauge('random_number_gauge','Nb entre 1 et 100')

def generation():
    while True:
        random_number = randrange(100)
        RANDOM_NUMBER_GAUGE.set(random_number)
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(9888)
    generation()