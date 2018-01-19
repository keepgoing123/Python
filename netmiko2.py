from netmiko import ConnectHandler

iou_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.94',
    'username': 'notker',
    'password': 'cisco',
}
iou_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.95',
    'username': 'notker',
    'password': 'cisco',
}
iou_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.96',
    'username': 'notker',
    'password': 'cisco',
}

all_devices = [iou_l2_s1, iou_l2_s2, iou_l2_s3]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip int bri')
    print output
    config_command = ['int loop 3', 'ip address 3.3.3.3 255.255.255.0']
    output = net_connect.send_config_set(config_command)
    print output
    for n in range (2,31):
        print "Removing VLAN " + str(n)
        config_command = [' no vlan ' + str(n)]
        output = net_connect.send_config_set(config_command)
        print output
