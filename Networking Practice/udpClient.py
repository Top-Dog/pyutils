'''
Created on 14/06/2015

@author: Sean O'Connor
@description: UDP is connectionless, just point and send
'''
import socket

def main():
    host = '127.0.0.1'
    port = 5001 # this must be different to server (UDP only)

    server = ('127.0.0.1', 5000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    
    message = input("-> ")
    while message != 'q':
        s.sendto(bytes(message, "UTF-8"), server)
        data, addr = s.recvfrom(1024)
        print("Received from server: " + str(data.decode("UTF-8")))
        message = input("-> ")
    s.close()
    
if __name__ == '__main__':
    main()