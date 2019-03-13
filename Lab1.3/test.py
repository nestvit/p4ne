from pysnmp.hlapi import * # Импортировать только High-level API

community_name = "public"
ipaddr_string = "10.31.70.107"
port_int = 161

snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

result_sysDescr = getCmd(SnmpEngine(),
	CommunityData(community_name, mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(snmp_object))

print(result_sysDescr)
x = 0
for i in result_sysDescr:
    print(i)
    print(i[3])
    for x in i[3]:
        print(x)

snmp_object1 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной

result_Interfaces = nextCmd(SnmpEngine(),
	CommunityData(community_name, mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(snmp_object1), lexicographicMode=False)

print(result_Interfaces)

for i in result_Interfaces:
    #print(i)
    #print(list(i[3]))
    for x in list(i[3]):
        print(type(x))
        print(x)
#result_List = nextCmd (…, lexicographicMode=False) # Не идти в глубину
