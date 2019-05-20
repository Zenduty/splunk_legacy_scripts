import urllib2
import json
import sys,os

url= "https://www.zenduty.com/api/integration/splunk_legacy/{}/".format(os.environ.get('ZENDUTY_KEY'))
message= "{} - {}".format(sys.argv[5], "Crossed threshold")
summary= sys.argv[2]
entity_id= sys.argv[2]
splunk_url= sys.argv[6]
no_of_event= sys.argv[1]
data={"message": message,
    "summary": summary,
    "entity_id": entity_id,
    "status": "open",
    "splunk_url": splunk_url,
    "No of Event":no_of_event }

json_data= json.dumps(data)

req = urllib2.Request(url)
response = urllib2.urlopen(req,json_data)    
