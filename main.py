from iputils import *
import argparse

parser = argparse.ArgumentParser(description='lookup source and destination against subnet lists')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-csv',action='store',help='Specify csv file to look ip addresses up against',required=True)
parser.add_argument('-source',action='store',help='Specify source IP to look up')
parser.add_argument('-dest',action='store',help='Specify destination IP to look up')
args=parser.parse_args()

#set source/dest inputs
ipsource = args.source
ipdestination = args.dest

#generate zones and environments
zoneparse(args.csv)
envparse(args.csv)

#lookup zones and environments
source_zone = zonelookup(ipsource)
source_env = envlookup(ipsource)
destination_zone = zonelookup(ipdestination)
destination_env = envlookup(ipdestination)

#print statements as outputs
print('-'*20)
print('Address Mapping')
print('-'*20)
print('Source Queried: ' + ipsource + '\nZone: ' + source_zone + '\nEnvironment: ' + source_env)
print('\nDestination Queried: ' + ipdestination + '\nZone: ' + destination_zone + '\nEnvironment: ' + destination_env) 
print('\n' + ('-'*20))
print('Flow analysis')
print('-'*20)    
print('Environment Flow: ' + source_env + ' -> ' + destination_env + ' - ' + flowlogic(source_env,destination_env))
print('Zone Flow: ' + source_zone + ' -> ' + destination_zone + ' - ' + flowlogic(source_zone,destination_zone))
