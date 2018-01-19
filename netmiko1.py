from netmiko import ConnectHandler

iou_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.93',
    'username': 'notker',
    'password': 'cisco',
}
net_connect = ConnectHandler(**iou_l2)
output = net_connect.send_command('show ip int bri')
print output

config_command = ['int loop 3', 'ip address 3.3.3.3 255.255.255.0']
output = net_connect.send_config_set(config_command)
print output

for n in range (21,26):
    print "Creating VLAN " + str(n)
    config_command = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_command)
    print output
