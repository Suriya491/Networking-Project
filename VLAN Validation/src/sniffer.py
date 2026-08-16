from scapy.all import sniff, wrpcap

def capture(interface: str, timeout: int = 5):
    packets = sniff(iface=interface, timeout=timeout)
    wrpcap("capture.pcap", packets)
    print(f"Captured {len(packets)} packets.")
    return packets
