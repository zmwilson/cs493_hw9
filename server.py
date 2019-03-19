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
genres = []
artists = []
albums = []
songs = []

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

@app.route('/genres', methods=['GET'])
@cross_origin(supports_credentials=True)
def genres():
    genre1 = request.args.get('genre1')
    genre2 = request.args.get('genre2')
    genres.append(genre1)
    genres.append(genre2)
    resp = jsonify(genres)
	resp.status_code = 200
	return resp

@app.route('/artists/for/genre', methods=['GET'])
@cross_origin(supports_credentials=True)
def genres():
    artist1 = request.args.get('Artist1')
    artist2 = request.args.get('Artist2')
    artists.append(artist1)
    artists.append(artist2)
    resp = jsonify(artists)
	resp.status_code = 200
	return resp

@app.route('/albums/for/artist', methods=['GET'])
@cross_origin(supports_credentials=True)
def genres():
    album1 = request.args.get('album1')
    album2 = request.args.get('album2')
    albums.append(genre1)
    albums.append(genre2)
    resp = jsonify(albums)
	resp.status_code = 200
	return resp

@app.route('/songs/for/album', methods=['GET'])
@cross_origin(supports_credentials=True)
def genres():
    song1 = request.args.get('song1')
    song2 = request.args.get('song2')
    songs.append(genre1)
    songs.append(genre2)
    resp = jsonify(songs)
	resp.status_code = 200
	return resp

#@app.route('/<filename>')
#def api_file(filename):
	#return send_file(x)