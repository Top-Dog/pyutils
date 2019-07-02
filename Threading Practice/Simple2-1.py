'''
Created on 14/06/2015

@author: Sean O'Connor
@decription: A basic timer program 
Uses locks, only one thread can be in a lock at a time

A semaphore is like a lock, but more than 1 thread can take the semaphore at a time,
but you can limit the number of semaphores, for example, in this application there may
be 10 threads, but you only want three threads writing to stdout at time - a semaphore 
is the right way to achieve this.
'''
import threading, time

tLock = threading.Lock()

def timer(timerName, delay, repeat):
    '''Print the system time for the number of 'repeat'
    with a delay of 'delay' between the successive thread running.'''
    print("Timer: " + timerName + " Started.")
    # This thread now owns the lock, no other thread can use it.
    tLock.acquire()
    print(timerName + " has acquired the lock.")
    while repeat > 0:
        time.sleep(delay)
        print(timerName + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print(timerName + " is releasing the lock.")
    tLock.release()
    print("Timer: " + timerName + " Completed.")
    
def main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    
    t1.start()
    t2.start()
    
    print("Main Completed!")

if __name__ == '__main__':
    main()