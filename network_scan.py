import scapy.all as scapy 
import optparse
print(""" 
┏┓┏┓┏┓┏┳┓  ┳┓┳┏┓┓ ┏┓             
┣┫┏┛┣┫ ┃   ┃┃┃┃ ┃ ┣              
┛┗┗┛┛┗ ┻   ┻┛┻┗┛┗┛┗┛             
┳┓┏┓┏┳┓┓ ┏┏┓┳┓┓┏┓  ┏┓┏┓┏┓┳┓┳┓┏┓┳┓
┃┃┣  ┃ ┃┃┃┃┃┣┫┃┫   ┗┓┃ ┣┫┃┃┃┃┣ ┣┫
┛┗┗┛ ┻ ┗┻┛┗┛┛┗┛┗┛  ┗┛┗┛┛┗┛┗┛┗┗┛┛┗
         @azatmurg
      Network Scanner      
      """)
def get_user_input():
    parse_input=optparse.OptionParser()
    parse_input.add_option("-i","--ipaddress",dest="ip_address",help="Enter ip Address")
    (user_input,argument)=parse_input.parse_args()
    if not user_input.ip_address:
        print("Please Enter the ip address")
    return user_input
        
def scan_my_network(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    brodcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinebacket=brodcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combinebacket,timeout=1)
    answered_list.summary()
    
user_ip_address = get_user_input()
scan_my_network=(user_ip_address.ip_address)
