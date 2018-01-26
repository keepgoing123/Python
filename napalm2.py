import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosr1 = driver('1.1.1.1', 'notker', 'cisco')
iosr1.open()

ios_output = iosr1.get_facts()
print (json.dumps(ios_output,indent=4))

ios_output = iosr1.get_interfaces()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosr1.get_interfaces_counters()
print (json.dumps(ios_output, sort_keys=True, indent=4))


