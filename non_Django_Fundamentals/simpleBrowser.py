import socket                                                         # sockets allow you to send and receive data

                                                                
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            # creating so called socket
mySock.connect(('example.com', 80))                                 # dial this socket (connect) and connect to port 80
cmd = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'.encode()          # GET / URL / protocol / (r\n\r\n = return - newline - return -newline) / .encode() = utf8
mySock.send(cmd)                                                      # we talk first

                                    
while True:                                                           # We are supposed to receive data until the socket is closed
    data = mySock.recv(512)                                           # received data up until 512 characters
    if len(data) < 1:                                                 # checks to see if the socket hasn't received basically any data
        break                                                         # if the socket is hung up and not receiving data then, socket will close
    print(data.decode(),end='')                                       # decodes the utf8 data and converts it into unicode (encode when send, decode when receive)

mySock.close()
