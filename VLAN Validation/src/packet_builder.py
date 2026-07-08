from scapy.all import Ether, Dot1Q, Raw

def build_vlan_packet(dst_mac: str, vlan_id: int, priority: int = 0):
    """
    Build a simple 802.1Q tagged Ethernet frame.
    """
    return (
        Ether(dst=dst_mac) /
        Dot1Q(vlan=vlan_id, prio=priority) /
        Raw(load=b"VLAN Validation Test")
    )

if __name__ == "__main__":
    pkt = build_vlan_packet("ff:ff:ff:ff:ff:ff", 100)
    pkt.show()
