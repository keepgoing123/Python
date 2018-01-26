import json
from pyntc import ntc_device as NTC
iosrouter = NTC(host='1.1.1.1', username='notker',password='cisco',device_type='cisco_ios_ssh')
iosrouter.open()

ios_output = iosrouter.facts
print (json.dumps(ios_output, indent =2))
