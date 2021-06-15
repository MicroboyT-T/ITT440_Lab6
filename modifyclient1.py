import socket
import signal
import sys

c = socket.socket()
host = '192.168.56.102'
port = 8888

print('Waiting for connection...')
try:
    c.connect((host, port))
except socket.error as e:
    print(str(e))

Response = c.recv(1024)
print(Response.decode("utf-8"))
while True:
    print("What kind mathematical function Do you want to use? :")
    print("Log statement(l)")
    print("Square Root(s)")
    print("Exponential(e)")
    Input = input('\nEnter function code here: ')

    if Input == 'l' or Input == 's' or Input == 'e':
        n = input("Enter any number: ")
        Input = Input + ":" + n
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'exit':
        break

    else:
        print("I think your functional code not available only available is l,s,e and exit only. Please try again...")
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

c.close()
