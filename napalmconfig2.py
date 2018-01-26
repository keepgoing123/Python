import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosr1 = driver('1.1.1.1', 'notker', 'cisco')
iosr1.open()

print ('Accessing 1.1.1.1 - R1')
iosr1.load_merge_candidate(filename='ACL1.cfg')

diffs = iosr1.compare_config()
if len(diffs) > 0:
	print(diffs)
	iosr1.commit_config()
else:
	print('No changes required.')
	iosr1.discard_config()
iosr1.close()
