#!/usr/bin/env python3
# Author: Nic Jones (NicPWNs)
# port-scan-detector.py

import socket
from datetime import datetime

# Listen locally for an unsual port
host = "0.0.0.0"
port = 1023

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server.bind((host,port))

# Queue requests
server.listen(5)
print("Listening for TCP connections on: %s:%d..." % (str(host),port))

while True:
    client,addr = server.accept()

    print("Hmm, that's an odd port to be connecting to. PORT SCANNING DETECTED ON PORT " + str(port))
    print("Port scanning detected from: %s" % str(addr))

    bye = "ACK!\r\n"
    client.send(bye.encode('ascii'))
    client.close()