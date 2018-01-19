#!/usr/bin/env python

from netmiko import ConnectHandler

iou_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.91',
    'username': 'notker',
    'password': 'cisco',
}
iou_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.92',
    'username': 'notker',
    'password': 'cisco',
}
iou_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.93',
    'username': 'notker',
    'password': 'cisco',
}
iou_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.94',
    'username': 'notker',
    'password': 'cisco',
}
iou_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.95',
    'username': 'notker',
    'password': 'cisco',
}

with open('iou_l2_config') as f:
    lines = f.read().splitlines()
print lines

all_devices = [iou_l2_s1, iou_l2_s2, iou_l2_s3, iou_l2_s4, iou_l2_s5]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print output
    