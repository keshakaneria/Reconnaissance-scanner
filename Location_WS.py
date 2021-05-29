import ipinfo

########## LOCATION ############
def Location_WS(ipaddress):
    output ="\n"
    access_token = 'e44d39b81c7ef7'# my token inserted  #every user will need to initilize their token on ipinfo
    ip_port=[80]
    handler = ipinfo.getHandler(access_token)
    for ipport in ip_port:
        details = handler.getDetails(ipaddress)
        for d in details.all:
            output+=f"{d} : {details.all[d]}\n"
        #print(details.city, details.all)
    return output