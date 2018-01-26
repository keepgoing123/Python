import json
from pyntc import ntc_device as NTC
ios-r1 = NTC(host='1.1.1.1', username='notker', password='cisco', device_type='cisco_ios_ssh')
ios-r1.open()

ios_run = ios-r1.running_config
#print (ios_run)

HOST = '1.1.1.1'
saveoutput = open('switch-' + HOST, 'w')
saveoutput.write(ios_run)
saveoutput.close



