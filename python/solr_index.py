#!/usr/bin/env python
# encoding: utf-8
import solr
s = solr.SolrConnection('http://localhost:8983/solr')

# add a document to the index
s.add(id=1, enslish='some')
s.commit()

