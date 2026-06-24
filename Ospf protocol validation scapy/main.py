import json
from ospf_validator import validate_device
from reporter import write_report

with open('config/devices.json') as f:
    devices=json.load(f)
results=[]
for d in devices:
    s=validate_device(d)
    results.append([d['host'],s])
    print(d['host'],s)
write_report(results)
print('Report Generated')
