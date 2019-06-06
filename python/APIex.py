from dpla.api import DPLA
import os
my_api_key = os.getenv('API_KEY')
dpla_connection = DPLA(my_api_key)
result = dpla_connection.search('austen')
print(type(result))
#print(str(result.__dict__)[:1000])
item = result.items[0]
item
print(item['sourceResource']['stateLocatedIn'])
#result.items[0]['sourceResource']
item.keys()

for item in result.items[:9]:
    if 'stateLocatedIn'in item['sourceResource']:
        print(item['sourceResource']['stateLocatedIn'])
    else:print(item['sourceResource']['format'])
