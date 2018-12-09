import socket
import sys

HOST = '127.0.0.1'  
PORT = int(sys.argv[1])      
expression = sys.argv[2]

OPS = ["+","-","*","/"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
except:
    print('Cannot open connection, please try later.')
    sys.exit()
tokens = expression.split()
if not tokens:
    print("Empty input")
    sys.exit()
stack = []
i=0
try:
    for token in tokens:
        i += 1
        if token in OPS:
            arg2 = stack.pop()
            arg1 = stack.pop()
            exp = str(arg1) + " " + str(arg2) + " " + token
            sock.send(exp.encode())
            result = sock.recv(1024)
            result = result.decode()
            if(result == "ERROR 400"):
                print("Malformed input")
                sys.exit()
            if i!=len(tokens):
                print("Client Received: " + result)
            stack.append(int(result))
        else:
            stack.append(int(token))
except Exception as e:
    print('Malformed Input')
    sys.exit()

ans = stack.pop()
if not stack:
    print("Client Received Final: "+ str(ans))
else:
    print('Malformed Input')