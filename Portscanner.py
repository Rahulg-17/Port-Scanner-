
# Online Python - IDE, Editor, Compiler, Interpreter
#!/bin/python

import sys
import socket   
from datetime import datetime

#defining our target 
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #to translate host to IPv4
else:
    print("invalid amount of arguments")
    print ("Syntax: python3 scanner.py <ip>")
    
print("Scanning target "+target)
print("Time Started- "+str(datetime.now()))

try:
    for port in range (1,999):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.03)
        result = s.connect_ex((target,port)) #returns an error indicator
        # print ("Checking port {}".format(port)) (use it for checking each port)
        if result == 0:
            print ("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("Could not connect to server.")
    sys.exit()

    
    

