'''
Created on 14/06/2015

@author: Sean O'Connor

@decription: Producer produces items and Consumer takes items, 
from a queue.

Share information using a queue
'''
import threading, time, random
# Version dependancy for 2.7 and 3.4
try:
    import Queue
except:
    import queue as Queue

class Producer:
    '''Puts plates of food on the table'''
    def __init__(self):
        self.food = ["ham", "soup", "salad"]
        self.nextTime = 0 # This is variable for the effective delay
    
    def run(self):
        global q
        # Loop for 10 seconds
        while(time.clock() < 10):
            # Only progress if the 'effective delay' time is up
            if (self.nextTime < time.clock()):
                # randomly choose an item from the list of foods
                f = self.food[
                              random.randrange(len(self.food))]
                q.put(f)
                print("Adding " + f)
                # reset the delay timer to somewhere between 0 and 1
                self.nextTime += random.random()
                
class Consumer:
    '''Takes plates of food off the table'''
    def __init__(self):
        self.nextTime = 0
    
    def run(self):
        global q
        # Loop for 10 seconds
        while (time.clock() < 10):
            # Only progress if the 'effective delay' time is up
            if (self.nextTime < time.clock() and not q.empty()):
                # get one item from the front of the queue
                f = q.get()
                print("Removing " + f)
                # reset the delay timer to somewhere between 0 and 2
                # so the consumer is (on average) twice as slow as the producer
                self.nextTime += random.random()*2
def main():
    p = Producer()
    c = Consumer()
    pt = threading.Thread(target=p.run, args=())
    ct = threading.Thread(target=c.run, args=())
    pt.start()
    ct.start()
    
if __name__ == '__main__':
    # define the queue here, or else it only has scope in the 'main' function
    q = Queue.Queue(10)
    main()