import socket
import sys

HOST = '127.0.0.1'  # localhost
PORT = int(sys.argv[1])   
OPS = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: int(a / b))
}

def findVal(expression):
    tokens = expression.split()
    try:
        return str(OPS[tokens[2]](int(tokens[0]), int(tokens[1])))
    except:
        return("ERROR 400")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

any_connection = False
while True:
    try:
        conn, addr = sock.accept()
        any_connection = True
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            print("Server Received: \"" + data + "\"")
            ans = findVal(data)
            conn.sendall(ans.encode())
        conn.close()
    except:
        break
print("Closing connection")
if any_connection:
    conn.close()