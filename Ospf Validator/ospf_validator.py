from netmiko import ConnectHandler
import json

with open("devices.json") as f:
    devices = json.load(f)

print("=" * 50)
print("OSPF VALIDATION REPORT")
print("=" * 50)

for device in devices:
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show ip ospf neighbor")

        if "FULL" in output:
            print(f"{device['host']} : PASS")
        else:
            print(f"{device['host']} : FAIL")

        conn.disconnect()

    except Exception as e:
        print(f"{device['host']} : ERROR {e}")
