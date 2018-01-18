#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

for n in range (93,97):
    HOST = "192.168.1." + str(n)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    tn.write("conf t\n")
    for n in range (11,21):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" +str(n) + "\n")
    tn.write("end\n")
    tn.write("exit\n")
    print tn.read_all()

