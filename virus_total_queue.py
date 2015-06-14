#!/usr/bin/env python
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

apiurl = "https://www.virustotal.com/vtapi/v2/url/scan"

# paste your Virus Total API key here...
apikey = ""

for url in urls:
    params = {"url": url, "apikey": apikey}
    data = urllib.urlencode(params)
    req = urllib2.Request(apiurl, data)
    try:
        print("[*] Submitting %s to Virus Total..." % url)
        response = urllib2.urlopen(req)
        time.sleep(15) # public API allows 4 queries per minute  
    except:
        print("[*] Bad URL: %s" % url)

