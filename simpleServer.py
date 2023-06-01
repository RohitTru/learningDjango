from socket import *

def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)                             # This is an endpoint
    try:                                                                    # exception handling to make sure we dont have multiple apps listening on port our port
        serverSocket.bind(('localhost',9100))                               # opens port 90 to receive data
        serverSocket.listen(5)                                              # if computer is busy listening to one "phone call", you can queue four more
        while (1):
            (clientsocket, address) = serverSocket.accept()                 # Waits until a client connection is received

            rd = clientsocket.recv(5000).decode()                           # decodes the incoming data from client from utf8 to unicode
            pieces = rd.split("\n")                                         # split the code based on newlines (this is for headers)
            if (len(pieces) > 0):
                print(pieces[0])                                            # print Url to prove we got it

            #constructing a response
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())                             # encode before send
            clientsocket.shutdown(SHUT_WR)                                  # close the connection

    except KeyboardInterrupt:
        print('\nShutting down...\n');
    except Exception as exc:
        print("Error:\n");
        print(exc)

    serverSocket.close()

print('Access http://localhost:9100')
createServer()
