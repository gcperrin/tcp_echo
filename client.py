# Client

import socket
import json
from dotenv import dotenv_values

# Load env
config = dotenv_values(".env")

fd = open('./data.json')
data = json.load(fd)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8089)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = json.dumps(data).encode("ascii")
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(2048)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
