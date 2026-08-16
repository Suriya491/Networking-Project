from src.packet_builder import build_vlan_packet
from src.validator import validate_vlan

def test_vlan():
    pkt = build_vlan_packet("ff:ff:ff:ff:ff:ff",100)
    ok,msg = validate_vlan(pkt,100)
    assert ok
