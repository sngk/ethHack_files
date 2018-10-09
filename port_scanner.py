#!/usr/bin/env python
import socket
import sys
from datetime import datetime

# The fucntion taht checks if the IPv4 address entered by user is valid
# if not -- shows an error.


def is_valid_ipv4_address(address, errorMessage='Please, enter the valid IPv4 address that loooks like x.x.x.x \nwhere x is digital number from 1 to 255.'):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        print(errorMessage)
        try:
            socket.inet_aton(address)
        except socket.error:
            print(errorMessage)
            return False
        return address.count('.') == 3
    except socket.error:
        print(errorMessage)
        return False
    return True


# Ask for input host IP, port range

while True:
    targetIP = input("Enter IP address to scan: ")
    if is_valid_ipv4_address(targetIP):
        try:
            startPort = int(input("Enter the port No to start a scan from: "))
            endPort = int(input("Enter the port No to end the scan: "))
            break

        except ValueError:
            print ("Invalid input - Try again. \nRemember to use numbers only.")
            continue

# format output
print("=" * 60)
print("Please wait, scanning remote host > ", targetIP)
print("=" * 60)

# Check what time the scan started
startTime = datetime.now()

# Scan all ports within the specified range.
try:
    for port in range(startPort, endPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
endTime = datetime.now()

# Calc total time needed to finish port scanning
totalTime = endTime - startTime
print("Scanning Completed in: ", totalTime)
