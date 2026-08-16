from netmiko import ConnectHandler

def validate_device(device):
    try:
        c=ConnectHandler(**device)
        out=c.send_command('show ip ospf neighbor')
        c.disconnect()
        return 'PASS' if 'FULL' in out else 'FAIL'
    except Exception:
        return 'ERROR'
