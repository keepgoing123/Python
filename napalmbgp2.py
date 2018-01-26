import json
from napalm import get_network_driver

bgplist = ['1.1.1.1','2.2.2.2']

for ip_address in bgplist:
	print ("Connecting to " + str(ip_address))
	driver = get_network_driver('ios')
	iosrouter = driver(ip_address, 'notker', 'cisco')
	iosrouter.open()
	bgp_neighbors = iosrouter.get_bgp_neighbors()
	print (json.dumps(bgp_neighbors, indent=4))
	iosrouter.close()

