

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(req, indent=4))

	res = makeWebhookResult(req)

	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def makeWebhookResult(req):

	if req.get("result").get("action") == 'get_action':
		speech="At the very beginning\n"+req.get("result").get("action")+"\n"
		result=req.get("result")
		parameters=result.get("parameters")
		try:
			contact_id=parameters.get("contact_types")
			speech=speech+contact_id+"\n"
		except:
			contact_id=""
			speech=speech+"1\n"
		try:		
			need_id=parameters.get("no_need")
			speech=speech+need_id+"\n"
		except:
			need_id=""
			speech=speech+"2\n"
		try:		
			contact_id2=parameters.get("contact_types1")
			speech=speech+contact_id2+"\n"
		except:
			contact_id2=""
			speech=speech+"3\n"	

		speech="speech\n"	
		if contact_id=="mail":
			speech=speech+"Here you go. My mail id is : mailme@anirbansaha.com\n"	
		elif contact_id=="number":
			speech=speech+"My contact number is: 1234567890\n"
		elif contact_id=="contact":
			speech=speech+"My email is mailme@anirbansaha.com and my phone number is 1234567890\n"
		else:
			speech=speech+""		
		
		if contact_id2=="mail":
			speech=speech+"Here you go. My mail id is : mailme@anirbansaha.com\n"	
		elif contact_id2=="number":
			speech=speech+"My contact number is: 1234567890\n"
		elif contact_id2=="contact":
			speech=speech+"My email is mailme@anirbansaha.com and my phone number is 1234567890\n"
		else:	
			speech=speech+""

		if "mail" in need_id:
			speech=speech+"No mailid for you\n"	
		elif "number" in need_id:
			speech=speech+"No phone number for you\n"
		elif "contact" in need_id:
			speech=speech+"No contact for you\n"
		else:
			speech=speech+""				

		return 
		{
			"speech": speech,
			"displayText": speech,
			"data": {},
			"contextOut": [],
			"source": "apiai-onlinestore-shipping"
		}
	else:
		
		speech="I am flag one in get_action module\n"+str(req.get("result").get("action"))
		return {
			"speech": speech,
			"displayText": speech,
			#"data": {},
			# "contextOut": [],
			"source": "apiai-onlinestore-shipping"
		}

			
	
if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print("Starting app on port %d" % port)

	app.run(debug=True, port=port, host='0.0.0.0')

#!/usr/bin/env python