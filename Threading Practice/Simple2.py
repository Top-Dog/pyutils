'''
Created on 14/06/2015

@author: Sean O'Connor
@decription: A basic timer program 
All threads can access stdout at the same time - so printing can look mashed
'''
from threading import Thread
import time

def timer(timerName, delay, repeat):
    '''Print the system time for the number of 'repeat'
    with a delay of 'delay' between the successive thread running.'''
    print("Timer: " + timerName + " Started.")
    while repeat > 0:
        time.sleep(delay)
        print(timerName + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + timerName + " Completed.")
    
def main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    
    t1.start()
    t2.start()
    
    print("Main Completed!")

if __name__ == '__main__':
    main()