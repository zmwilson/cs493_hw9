# $env:FLASK_APP = "server.py"
# flask run
from __future__ import print_function
import boto3
import os
import sys
from flask import Flask, url_for, send_file, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

session = boto3.Session(profile_name='s3-access')
s3 = session.resource('s3')
client = session.client('s3')
bucket = s3.Bucket('zmwilson.cs493bucket')
contents = {}

@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def api_root():
	print("Contents of bucket:\n")
	for o in bucket.objects.all():
		url = client.generate_presigned_url(
			ClientMethod='get_object',
			Params={
			    'Bucket': 'zmwilson.cs493bucket',
			    'Key': o.key
			}
		)
		contents[o.key] = url
	resp = jsonify(contents)
	resp.status_code = 200
	return resp

#@app.route('/<filename>')
#def api_file(filename):
	#return send_file(x)