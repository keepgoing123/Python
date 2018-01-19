#!/usr/bin/env python

import paramiko
import time

ip_address = "192.168.1.93"
username = "notker"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()
remote_connection.send("conf t\n")
remote_connection.send("int loop 0\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send("int loop 1\n")
remote_connection.send("ip address 2.2.2.2 255.255.255.255\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")
remote_connection.send("exit\n")


for n in range(21,26):
    print "Removing VLAN" + str(n)
    remote_connection.send("no vlan " + str(n) + "\n")
    time.sleep(1)
    
remote_connection.send("end\n")
time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close    

