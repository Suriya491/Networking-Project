from scapy.all import Dot1Q

def validate_vlan(packet, expected_vlan: int):
    if not packet.haslayer(Dot1Q):
        return False, "No VLAN tag present"

    tag = packet[Dot1Q]

    if tag.vlan != expected_vlan:
        return False, f"Expected VLAN {expected_vlan}, got {tag.vlan}"

    return True, "PASS"
