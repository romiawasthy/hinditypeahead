#!/usr/bin/env python
# encoding: utf-8
import httplib
import json

file = open('hindi-eng.txt', 'r')
char_map = {}

for line in file:
    '''for part in line.split(','):
        part = unicode(part,encoding='utf-8')
        print part
    '''
    part = line.split(',')
    char_map[part[2].rstrip('\n').lower()] = unicode(part[1],encoding='utf-8')
   
file.close()

while True:
    user_input = raw_input("Enter something:")
    print user_input
    if user_input in char_map:
        print char_map[user_input]
    if user_input == "quit":
        break
   
