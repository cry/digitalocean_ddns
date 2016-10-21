import urllib, urllib2
import json
import sys

# General details

ip_resolver = "https://api.ipify.org"

domain = 'YOUR_DOMAIN'
subdomain = 'YOUR_SUBDOMAIN' # Replace me with @ if not using a subdomain

full_domain = "%s.%s" % (subdomain, domain)

def retrieve(url):
    "Retrieves url contents"
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_header)
    return urllib2.urlopen(req).read()

def put(url, value):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, data=value)
    request.add_header('Authorization', auth_header)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT'
    url = opener.open(request)

# DigitalOcean API details

token = "YOUR_DIGITALOCEAN_TOKEN"
auth_header = "Bearer %s" % (token)

domain_api = {
    "list": "https://api.digitalocean.com/v2/domains",
    "records": "https://api.digitalocean.com/v2/domains/%s/records" % (domain),
    "update": "https://api.digitalocean.com/v2/domains/%s/records/%s" % (domain, '%s')
}

# Resolve current IP

ip = retrieve(ip_resolver)

# Get record information

d_list = json.loads(retrieve(domain_api['records']))['domain_records']
d_id = None
d_ip = None

for d in d_list:
    if d['data'] != subdomain:
        pass
    d_id = d['id']
    d_ip = d['data']

if d_id == None:
    raise RuntimeError("Subdomain doesn't exist.")

# Update if differing, if not do nothing

if d_ip == ip:
    sys.exit()

put(domain_api['update'] % (d_id), json.dumps({'data': ip}))