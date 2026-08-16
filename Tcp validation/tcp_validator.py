from scapy.all import sniff
from config.settings import INTERFACE,PACKET_COUNT

def capture_packets():
 return sniff(iface=INTERFACE,filter='tcp',count=PACKET_COUNT)
