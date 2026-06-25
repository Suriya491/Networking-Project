from tcp_validator import capture_packets
from packet_analyzer import analyze
from reporter import write_report
pkts=capture_packets();summary=analyze(pkts);write_report(summary)
print(summary)
