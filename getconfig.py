#!/usr/bin/env python

import getpass
import telnetlib

# Ask for username and passoword
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

# Open a file called myswitches
f = open('myswitches')

# Telnet to switches and get the running config
for line in f:
    print "Getting running configu from Switch " + (line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    
    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")
    
    readoutput =tn.read_all()
    saveoutput = open("switch" + "-[" + HOST + "]", "w")
    saveoutput.write(readoutput)
    saveoutput.close
    

