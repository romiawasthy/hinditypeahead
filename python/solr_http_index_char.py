#!/usr/bin/env python
# encoding: utf-8
import httplib
import json

file = open('hindi-eng.txt', 'r')
char_map = []

for line in file:
    '''for part in line.split(','):
        part = unicode(part,encoding='utf-8')
        print part
    '''
    part = line.split(',')
    char_map.append({'id':part[0], 'hindi':unicode(part[1],encoding='utf-8'), 'english':part[2].rstrip('\n')})
   
file.close()

'''
print char_map

for char_i in char_map:
    for ch in char_i:
        print ch + char_i[ch]
        
'''

conn= httplib.HTTPConnection('localhost:8983')


#params = json.dumps([{"id":"3","english":"change.me"}])
params = json.dumps(char_map)

print params

headers = {"Content-type": "application/json"}

conn.request("POST", "/solr/update?commit=true", params, headers);
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()


