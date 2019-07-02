'''
Created on 14/06/2015

@author: Sean O'Connor
'''
import socket

def main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.connect((host, port))
    
    message = input("-> ")
    # use the letter q to quit
    while message != 'q':
        s.send(bytes(message, "UTF-8"))
        data = s.recv(1024)
        print("Received from server: " + str(data.decode("UTF-8")))
        message = input("-> ")
    s.close()
        
if __name__ == '__main__':
    main()