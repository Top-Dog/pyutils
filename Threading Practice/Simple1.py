'''
Created on 14/06/2015

@author: Sean O'Connor
@decription: Luanch the 'splitter' function n times, each time in a new thread.
'''
import threading, random

def splitter(words, index):
    mylist = words.split()
    newlist = []
    while (mylist):
        # pop a randomly indexed word from the list 
        newlist.append(mylist.pop(random.randrange(0, len(mylist))))
        # print a line that has each of the words seperated by a space
        print(' '.join(newlist), index)    
    
def main():
    sentance = "This is the main function. Running."
    numThreads = 5
    threadList = []
    
    print("Starting...\n")
    for i in range(numThreads):
        # create a new thread, pass in args (as a tuple)
        t = threading.Thread(target=splitter, args=(sentance, i+1))
        t.start()
        threadList.append(t)
    print("\nThread Count: ", str(threading.activeCount()))
    print("Exiting...\n")

if __name__ == '__main__':
    main()