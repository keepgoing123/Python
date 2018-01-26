import json
from pyntc import ntc_device as NTC
ios-r1 = NTC(host='1.1.1.1', username='notker', password='cisco', device_type='cisco_ios_ssh')
ios-r1.open()

ios_output = ios-r1.facts
print (json.dumps(ios_output, indent =2))

ios-r1.config_list(['hostname R1_Python', 'router ospf 2', 'network 0.0.0.0 255.255.255.255 area 0'])



