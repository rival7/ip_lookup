import ipaddress
import csv

#create variables from a csv
zone = {}
environment = {}

def zoneparse(csvfile):
    with open(csvfile,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader, None)
        for row in csvreader:
            if row[1] in zone:
                zone[row[1]].append(row[0])
            else:
                zone[row[1]] = [row[0]]

def envparse(csvfile):
    with open(csvfile,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader, None)                    
        for row in csvreader:
            if row[2] in environment:
                environment[row[2]].append(row[0])
            else:
                environment[row[2]] = [row[0]]  

#takes a string as an input, runs IP address query to map it to a variable (one of the zones above)
def zonelookup(ip):
    for i in zone:
        result = zone.get(i)
        for b in result:
            if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(b):
                return(i)
           

#takes a string as an input, runs IP address query to map it to a variable (one of the environemnts above)
def envlookup(ip):
     for i in environment:
        result = environment.get(i)
        for b in result:
            if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(b):
                return(i)    
        

#use this function to define permitted and not permitted flows
def flowlogic(source,dest):
    if source == dest:
        return 'Flow Permitted'
    else:
        return 'Flow NOT permitted!'
