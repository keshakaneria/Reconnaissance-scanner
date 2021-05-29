import nmap

# initialize the port scanner
nmScan = nmap.PortScanner()

def OS_Info(host_ip):
    output = "\n"
    os_deets = nmScan.scan(host_ip, arguments="-O")['scan'][host_ip]['osmatch'][1]
    for d in os_deets:
        if d == "osclass":
            output += "osclass :: \n"
            for i in os_deets[d]:
                for key in i:
                    output += f"{key} : {i[key]}"
        else:
            output += f"{d} : {os_deets[d]}\n"
    return output

#OS_Info("8.8.8.8")
