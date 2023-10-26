from scapy.all import *
packets = rdpcap("/home/yassine/pyscrits/example.pcap")
for i in range(len(packets)):
	if len(packets[i])>900 :
		frags=fragment(packets[i],fragsize=900)
		send(frags,iface="enp0s3")
	else:
		send(packets[i],iface="enp0s3")
