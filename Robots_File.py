import urllib.request

def Robots_File(domain_name):
    output = ""
    try:
        page = urllib.request.urlopen(f'http://{domain_name}/robots.txt')  #opening robot.txt file of mentioned domainname #or try /sitemap.xml
        Lines = page.readlines()        #reading lines of gotten web page
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            output+=line.strip().decode('utf-8')   #sepraing lines by strip() function and removing prefix b' by decode() function
    except Exception as e:
        output="Sorry, Robots.txt file may not exist for this host! :("
    return output

"""
from geekforgeeks.com check out RobotParser()
"""
