import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosr1 = driver('1.1.1.1', 'notker', 'cisco')
iosr1.open()

ios_output = iosr1.get_mac_address_table()
print (json.dumps(ios_output,indent=4))

ios_output = iosr1.get_arp_table()
print (json.dumps(ios_output,indent=4))

ios_output = iosr1.ping('2.2.2.2')
print (json.dumps(ios_output,indent=4))

