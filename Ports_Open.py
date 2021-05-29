import nmap
# initialize the port scanner
nmScan = nmap.PortScanner()

#def portScan(ip""", range"""):
def portScan(ip):
    range = '75-80'   #21,22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 136, 138, 139, 134, 161, 162, 389, 443, 989,990, 3389]
    output=""
    #for i in range:
    nmScan.scan(ip, range)
    for host in nmScan.all_hosts():
        output+=f"Host : {host} ({nmScan[host].hostname()})\n"
        output+=f"State : {nmScan[host].state()}\n"
        for proto in nmScan[host].all_protocols():
            output+="----------\n"
            output+=f"Protocol : {proto}\n"
            lport = list(nmScan[host][proto].keys())
            lport.sort()
            for port in lport:
                output+=f"port : {port}\tstate : {nmScan[host][proto][port]['state']}\n"
    return output

def Ports_Open(host_ip):
    output = "\n"
    try:
        output += portScan(host_ip)
    except Exception as e:
        output += "Sorry, Something went wrong!\n"
    return output

# Ports_Open('8.8.8.8')
#have to download packages: ipinfo and python-nmap
#range=[20,21,22,23,25,53,67,68,69,80,110,119,123,135,136,138,139,134,161,162,389,443,989,990,3389]
#range=[]
"""
OS detection
print(scanner.scan("198.143.164.252", arguments="-O")['scan']['198.143.164.252']['osmatch'][1])
 """