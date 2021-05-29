import socket as sk                             #importing socket module

def get_IP(host_name):
    output = "\n"
    host_ip = 0
    try:
        host_ip = sk.gethostbyname(host_name)           #Converting URL/Hostname to IP Address, gives alias name and if more than ip present
        output += "The IPaddress found are : "+host_ip
        #print(f'IP of {host_name} is {host_ip}')      #Printing final values
    except Exception as e:
        output += "Sorry, Something went wrong! \nCheck again your Domain name! :(\n"
    return output, host_ip

def IP_checker(host_ip):
    output = ""
    output += "Let's check if IP address of mentioned Hostname/Domainname::\n"
    try:
        HostName = sk.gethostbyaddr(host_ip)  # Checking if the ip is of mentioned hostname only
        output += "IP address {} is {}\n".format(host_ip,[i for i in HostName])
        output += "If the Host name and your entered Domain Name matches, It's a right IP!\n"
        output += "It can be an alias name, too! :)\n"
    except Exception as e:
        output += "Sorry, IP address may not be the right one! :(\n"
    return output

def IP_Address(host_name):
    ip_output1, ip = get_IP(host_name)
    if ip==0:
        return ip_output1
    ip_output2 = IP_checker(ip)
    return ip_output1+"\n"+ip_output2, ip
