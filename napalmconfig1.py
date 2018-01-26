import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosr1 = driver('1.1.1.1', 'notker', 'cisco')
iosr1.open()

print ('Accessing 1.1.1.1 - R1')
iosr1.load_merge_candidate(filename='ACL1.cfg')
iosr1.commit_config()
iosr1.close()
