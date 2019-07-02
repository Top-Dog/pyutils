Concept: 
communication of two or more programs communicating over a LAN or Internet network. The communication
is between either two or more clients, or a client and a server.

Model 1:
Client/server model. This is the most common, where a client connects to a server.

Model 2:
Peer/peer model. More complex, but more secure. Useful for accessing a service that doesn't have to be available all the time.
This is really the client/server model, but where the one user acts a both a client and server.

Terminoligy:
Address - for example - IPV4 127.0.0.1 as the loopback address
Ports - for example - 5000 as 'pigeon hole' on the networking card/hardware (ports 1 - 1024 are reserved for protocols, use ports in the range 1024 < port < 65535)
Sockets - abstracted concept for connections between machines. Handle both TCP and UDP
 * socket(socket_family, socket_type)
 * bind((hostname, port))
 * listen()
 * accept() returns new socket object
 * connect((hostname, port))
 * recv(buffer) tries to get data from TCP connection, blcoking
 * send(bytes)
 * close()
 TCP - reliable, ordered, error checked, slower
 UDP - more unreliable, no resending/error checks, only send information - if no one is listening the information is lost (point and send)