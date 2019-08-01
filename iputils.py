import ipaddress

#zones
zone1 = []
zone2 = []

#environments
prod = []
nonprod = []

#takes a string as an input, runs IP address query to map it to a variable (one of the zones above)
def zonelookup(ip):
    for i in zone1:
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(i):
            return 'Zone1'
    for i in zone2:     
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(i):
            return 'Zone2'        

#takes a string as an input, runs IP address query to map it to a variable (one of the environemnts above)
def envlookup(ip):
    for i in prod:
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(i):
            return 'Production'
    for i in nonprod:
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(i):
            return 'Non-Production'    

#use this function to define permitted and not permitted flows
def flowlogic(source,dest):
    if source == dest:
        return 'Flow Permitted'
    else:
        return 'Flow NOT permitted!'
