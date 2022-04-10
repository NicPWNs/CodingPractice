#!/usr/bin/env python3
#Author: Nic Jones (NicPWNs)

import socket
import sys
from datetime import datetime

# Read options from command line
if len(sys.argv) == 3:
    # Translate hostname to IP address
    target = socket.gethostbyname(sys.argv[1])
    # Grab specified ports option
    ports = sys.argv[2]
else:
    print("USAGE: port-scanner.py <TARGET> <PORTS>")
    print("PORTS: \"common\" (1-1024) OR \"all\" (1-65535)")

# Create the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

# Determine desired ports
maxPort = 1024
if ports == "all":
        maxPort = 65535

# Announce port scan
print("Port scan started at " + str(datetime.now()))
print("Port scan started on " + target)
print("Port scan scanning " + ports + " ports.")

# Perform port scan
countClosed = 0
for port in range(1,maxPort):
    if client.connect_ex((target,port)) != 0:
        countClosed += 1

    else:
        print("Port " + str(port) + " open on " + target)

print("All other " + str(countClosed) + " ports scanned are closed on " + target)