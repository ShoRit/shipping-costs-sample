# if req.get("result").get("action") == 'get_action':
# 		result=req.get("result")
# 		parameters=result.get("parameters")
# 		try:
# 			contact_id=parameters.get("contact_types")
# 		except:
# 			contact_id=""
# 		try:		
# 			need_id=parameters.get("no_need")
# 		except:
# 			need_id=""
# 		try:		
# 			contact_id2=parameters.get("contact_types1")
# 		except:
# 			contact_id2=""	


contact_id="mail"
contact_id2="number"
need_id=""


speech=""	
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

print(speech)			

# return 
# {
# "speech": speech,
# "displayText": speech,
# #"data": {},
# # "contextOut": [],
# "source": "apiai-onlinestore-shipping"
# }
