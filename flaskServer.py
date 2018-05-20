from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

import json

from datetime import datetime
from datetime import timedelta 

app = Flask(__name__)

@app.route("/getToken/")
@cross_origin() 
def getToken():
	code = request.args.get('code')
	state= request.args.get('state')

	data ={}
	data["client_id"]= "" #add your client Id here 
	data["scope"]="calender.read"
	data["redirect_uri"]="http://localhost:5000/getToken/" # change your server address
	data["grant_type"]="authorization_code"
	data["client_secret"]="" # add your client secret
	data["code"] = code
    # token validation
	return requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token",data=data).content

@app.route("/getCalData/")
@cross_origin() 
def getCalendarData():
    responseContent = getToken()
	jsonDataObj = json.loads(responseContent)
	header={}
	header["Authorization"] = "Bearer " + jsonDataObj["access_token"]
	header["Prefer"] = "outlook.timezone=\"Europe/Berlin\""
	nextDay= datetime.now() + timedelta(days=1) 

    # getting required data
	return requests.get("https://graph.microsoft.com/v1.0/me/events?$select=organizer,start,end,location",headers= header).content
	
