import urllib2
import json
import sys,os

url= "https://www.zenduty.com/api/integration/splunk_legacy/{}/".format(os.environ.get('ZENDUTY_KEY'))
message= "{} - {}".format(sys.argv[5], "Crossed threshold") # Trigger reason. For example, "The number of events was greater than 1." 
summary= sys.argv[2]  # Returns terms which you have searched to set alert like " source='/var/log/kern.log' failed stop"
entity_id= sys.argv[2] 
splunk_url= sys.argv[6] # Browser URL to view the report.  
no_of_event= sys.argv[1] # Number of events returned for searched term
data={"message": message,
    "summary": summary,
    "entity_id": entity_id,
    "status": "open",
    "splunk_url": splunk_url,
    "No of Event":no_of_event }

json_data= json.dumps(data) # JSON data which will be sent by http request

req = urllib2.Request(url)
response = urllib2.urlopen(req,json_data)    
