from iputils import *

#grab source/dest inputs
ipsource = input('Source? ')
ipdestination = input('Destination? ')
#lookup zones and environments
source_zone = zonelookup(ipsource)
source_env = envlookup(ipsource)
destination_zone = zonelookup(ipdestination)
destination_env = envlookup(ipdestination)
#print statements as outputs
print('\nSource Queried: ' + ipsource + '\nZone: ' + source_zone + '\nEnvironment: ' + source_env)
print('\nDestination Queried: ' + ipdestination + '\nZone: ' + destination_zone + '\nEnvironment: ' + destination_env) 
print('\nFlow Analysis\n-------------\nZone Flow: ' + source_zone + ' -> ' + destination_zone + ' - ' + flowlogic(source_zone,destination_zone))
print('Environment Flow: ' + source_env + ' -> ' + destination_env + ' - ' + flowlogic(source_env,destination_env))
