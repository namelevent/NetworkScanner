import scapy.all as scapy
import optparse

def parse():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="Network Scanner")
    (user_input , argument) = parse_object.parse_args()
    if not user_input:
        print("Enter a Ip Address!!")
    return user_input

def network_scanner(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    (answer_list,unanswer_list) = scapy.srp(combined_packet,timeout = 20)
    answer_list.summary()

user_ip_address = parse()
network_scanner(user_ip_address.ip_address)