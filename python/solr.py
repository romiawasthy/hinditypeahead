#!/usr/bin/env python
# encoding: utf-8
#import solr
#s = solr.Solr('http://localhost:8983/solr')

# add a document to the index
#s.add(id=1, enslish='some')
#s.commit()

#u'\u0900'
import repr

start = int('0900', 16)
end = int('097F', 16)
hindiList = []
charMap = {"A":"अ", "Bh":"भ", "B":"ब"}

for i in xrange(start, end + 1):
	#print "u'\u0"+format(i, 'x') + "'"
	hindiList.append("u'\u0"+format(i, 'x') + "'")

string = u"भ"
string2 = u"भरता"


for str in hindiList:
    #str = str.decode('unicode-escape')
   # print str
    if (str in string):
            print "success";

    
    
   


string = u"भारत भरता"

print string
parts = []
for part in string.split():
    if (part.find(string)):
        print "found " +part
    parts.extend(part.split(u"।"))
print "No of Parts: %d" % len(parts)
print "Parts: %s" % parts
	
 


 
 
 
 
 
 
 
 
 
 
 
