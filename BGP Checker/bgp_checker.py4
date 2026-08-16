from netmiko import ConnectHandler
import json

with open("devices.json") as f:
    devices = json.load(f)

print("=" * 50)
print("BGP HEALTH CHECK")
print("=" * 50)

for device in devices:
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show ip bgp summary")

        if "Idle" in output:
            print(f"{device['host']} : FAIL")
        else:
            print(f"{device['host']} : PASS")

        conn.disconnect()

    except Exception as e:
        print(f"{device['host']} : ERROR {e}")
