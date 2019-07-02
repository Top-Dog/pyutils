'''
Created on 14/06/2015

@author: Sean O'Connor
@decription: client sends text to server and comes back capitilised
'''
import socket

def main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.bind((host, port))
    
    s.listen(1) # listen for 1 connection
    c, addr = s.accept()
    print("We have recieved a connection from: " + str(addr))
    while True:
        data = c.recv(1024) # 1024 sized buffer
        if not data:
            # server ends connection if the client closed connection so no data comes through
            print('Client closed connection. Disconnecting.')
            break
        print("From connected user: " + str(data))
        data = str(data.decode("UTF-8")).upper()
        print("Sending: " + str(data))
        c.send(bytes(data, "UTF-8"))
    c.close()

if __name__ == '__main__':
    main()