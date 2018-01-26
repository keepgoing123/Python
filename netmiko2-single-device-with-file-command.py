#!/usr/bin/env python

from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios', 
    'ip': '1.1.1.1', 
    'username': 'notker', 
    'password': 'cisco',
}

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    print(output)

