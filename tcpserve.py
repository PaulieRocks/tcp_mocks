import socket
HOST=socket.gethostname()
PORT=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

while True:
    print("Listening")
    clientsocket, address=s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the Server","utf-8"))
    

