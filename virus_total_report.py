#!/usr//bin/env python
import simplejson
import urllib
import urllib2
import time
import sys

try:
    urls = open(sys.argv[1],"rb")
except:
    print("Usage: %s domains.txt" % sys.argv[0])
    sys.exit(1)

apiurl = "https://www.virustotal.com/vtapi/v2/url/report"

# paste Virus Total API key here...
apikey = ""

for url in urls:
    params = {"url": url, "apikey": apikey}
    data = urllib.urlencode(params)
    req = urllib2.Request(apiurl, data)
    try:
        response = urllib2.urlopen(req)
        json = response.read()
        print json
    except:
        print("[*] Failed to get report for %s" % url)
