#!/usr/bin/python
import json
import re
with open("./output") as fd:
  xlist = json.load(fd)

for x in xlist:
  domain=x['domain']
  domain=re.sub(r"[.]", "\\.", domain)
  print "(.*\.)?"+domain

