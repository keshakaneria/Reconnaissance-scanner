import socket

# def get_port_number():
#     port_number=int(input("Enter Port Number: "))
#     return port_number

def Service_Name(port_number):
    port_number = int(port_number)
    output = ""
    service_name = ""
    #if port_number==67 or port_number==68 or port_number==69 or port_number==123 or port_number==138 or port_number==161 or port_number==162:
    try:
        service_name = socket.getservbyport(port_number, "tcp")
        output += f"Name of the service running at port number {port_number} : {service_name}\n"
    except Exception as e:
        print(e)
        try:
            service_name = socket.getservbyport(port_number,"udp")          #Getting service name of protocol
            output += f"Name of the service running at port number {port_number} : {service_name}\n"
        except Exception as e:
            print(e)
            output +="Sorry, Couldn't get Port Service Name!\n"
    # print(f"Name of the service running at port number {port_number} : {service_name}")
    return service_name

def Port_Service_Info(inp):
    output = "\n"
    # port_number=get_port_number()
    output+=Service_Name(inp)
    return output

# Port_Service_Info(80)
#check out Scrapy module
"""
Port 	Service name 	Transport protocol
 20, 21 	 File Transfer Protocol (FTP) 	 TCP
 22 	 Secure Shell (SSH) 	 TCP and UDP
 23 	 Telnet 	 TCP
 25 	 Simple Mail Transfer Protocol (SMTP) 	 TCP
 !50, 51 	 IPSec 	 
 53 	 Domain Name System (DNS) 	 TCP and UDP
 67, 68 	 Dynamic Host Configuration Protocol (DHCP) 	 UDP
 69 	 Trivial File Transfer Protocol (TFTP) 	 UDP  range=[20,22,23,25,67,69,80,110,135,161,443]
 80 	 HyperText Transfer Protocol (HTTP) 	 TCP
 110 	 Post Office Protocol (POP3) 	 TCP
 119 	 Network News Transport Protocol (NNTP) 	 TCP
 123 	 Network Time Protocol (NTP) 	 UDP
 135-139 	 NetBIOS 	 TCP and UDP !136
 143 	 Internet Message Access Protocol (IMAP4) 	 TCP and UDP
 161, 162 	 Simple Network Management Protocol (SNMP) 	 TCP and UDP
 389 	 Lightweight Directory Access Protocol 	 TCP and UDP
 443 	 HTTP with Secure Sockets Layer (SSL) 	 TCP and UDP
 989, 990 	 FTP over SSL/TLS (implicit mode) 	 TCP
 3389 	 Remote Desktop Protocol 	 TCP and UDP
"""
