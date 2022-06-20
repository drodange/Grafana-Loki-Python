from operator import truediv
import requests
import time
import math
import random 
    
# store the random numbers in a list 
mu = 100
sigma = 50
    
while True:
    temp = random.gauss(mu, sigma) 
    response = requests.post('http://localhost:3000/api/live/push/custom_stream_id2', data='sma,sma=cpu5,host=smar usage_softirq='+str(temp), headers={'Authorization':'Bearer '+ 'eyJrIjoiZVFMU0ZXRlBoNk1qeWJNSmE2NkxQN2l1VEZFbmJkb1ciLCJuIjoiYWRtaW4yIiwiaWQiOjF9'})
    print(response)
    #time.sleep(0.2)