#!/usr/bin/env python3
from Env import Env
import random

# note that there is no use of ros here anymore
if __name__=='__main__':
   
    env = Env()
    env.reset()
    
    # random wandering behaviour
    while not env.done:
        a = random.randint(0,3)
        env.step(a) # replace a by 1 to go forward for testing
    
    env.stop()
    

