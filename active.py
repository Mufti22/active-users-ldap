import ldap3
from datetime import datetime

server = ldap3.Server('ldap://your-domain-controller')
connection = ldap3.Connection(server, user='your-username', password='your-password')

if not connection.bind():
    print(f"Failed to connect to the domain controller: {connection.result}")
    exit()

search_base = 'ou=Users,dc=your-domain,dc=com'
search_filter = '(&(objectCategory=person)(objectClass=user))'
attributes = ['sAMAccountName', 'lastLogonTimestamp']

connection.search(search_base, search_filter, attributes=attributes)

for entry in connection.entries:
    username = entry.sAMAccountName.value
    last_logon = entry.lastLogonTimestamp.value
    last_logon_date = datetime.utcfromtimestamp(last_logon / 10000000 - 11644473600).strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"User: {username}")
    print(f"Last Logon: {last_logon_date}")
    print()
