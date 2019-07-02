'''
Created on 14/06/2015

@author: Sean O'Connor

UDP - no listening and no accepting connections
'''
import socket

def main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    
    print("UDP Server Started.")
    while True:
        data, addr = s.recvfrom(1024)
        print("message from: " + str(addr))
        print("from connect suer: " + str(data.decode("UTF-8")))
        data = str(data).upper()
        print("sending: " + str(data))
        s.sendto(bytes(data, "UTF-8"), addr)
    s.close()

if __name__ == '__main__':
    main()