from scapy.all import *

def smtp_sniffer(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 25:
        if packet[TCP].payload:
            print(packet[TCP].payload.load.decode(errors="ignore"))

print("Listening...")
sniff(iface="eth0", prn=smtp_sniffer, filter="tcp port 25", store=0)
