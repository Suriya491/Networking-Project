from packet_builder import build_vlan_packet
from validator import validate_vlan

def demo():
    pkt = build_vlan_packet("ff:ff:ff:ff:ff:ff", 100)
    ok, msg = validate_vlan(pkt, 100)
    print(msg)

if __name__ == "__main__":
    demo()
