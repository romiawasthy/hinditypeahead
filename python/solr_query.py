#!/usr/bin/env python
# encoding: utf-8
from urllib2 import *
import urllib
import simplejson

#inputString = u"भरता"

inputString = "bharat"

for char in inputString:
  print char
  char = char.encode('utf8')
  urlString = "http://localhost:8983/solr/select?q=hindi:"+char+"&wt=json"
  conn = urlopen(urlString.encode('utf-8'))
  response = simplejson.load(conn)
  print response['response']['numFound'], "documents found."
# Print the name of each document.
  
# Print the name of each document.
 
  for document in response['response']['docs']:
    print "  Name =", document['hindi']

  
