#!/usr/bin/env python

from netmiko import ConnectHandler

ios_r1 = {
    'device_type': 'cisco_ios', 
    'ip': '1.1.1.1', 
    'username': 'notker', 
    'password': 'cisco',
}

net_connect = ConnectHandler(**ios_r1)
output = net_connect.send_command('show ip int brief')
print(output)
