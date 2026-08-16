from scapy.all import TCP

def analyze(pkts):
 syn=synack=ack=0
 for p in pkts:
  if p.haslayer(TCP):
   fl=int(p[TCP].flags)
   syn+=fl==2
   synack+=fl==18
   ack+=fl==16
 s=min(syn,synack,ack)
 return {'SYN':syn,'SYNACK':synack,'ACK':ack,'Successful Handshakes':s,'Failed Handshakes':max(syn-s,0)}
