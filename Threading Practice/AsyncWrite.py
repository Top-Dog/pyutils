'''
Created on 14/06/2015

@author: Sean O'Connor
@decription: write to a file in the background and
wait for all threads to finish before ending the program
'''
import threading, time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
    
    def run(self):
        f = open(self.out, "a") # append to file
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished background file write to: " + self.out)
        
def main():
    message = input("Enter a string to store: ")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program is continuing with a background task")
    
    # Wait for all background threads to finish before continuing
    background.join()
    print("All threads have finished")
    
    

if __name__ == '__main__':
    main()