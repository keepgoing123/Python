import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosr1 = driver('1.1.1.1', 'notker', 'cisco')
iosr1.open()

bgp_neighbors = iosr1.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

iosr1.close()

