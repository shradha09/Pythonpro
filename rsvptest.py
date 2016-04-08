import os
import json
import string
import csv
from flask import Flask, render_template, redirect, url_for, request, Response,make_response
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.rsvpdata


@app.route('/')
def rsvpdata():
	
	_items = db.rsvpdata.find()
	items = [item for item in _items]
	count = len(items)
	print(items)
	return render_template('profile.html',counter=count, items=items)
	

@app.route('/new', methods=['POST'])
def new():
	
	item_doc = {'name': request.form['name'],'email': request.form['email']
}
	db.rsvpdata.insert_one(item_doc)
	return redirect(url_for('rsvpdata'))


@app.route('/csvdata')
def csvdata():

	_items = db.rsvpdata.find()
	items = [item for item in _items]
	print(items)
	
		
	response = make_response(render_template('csvdata.html'))
	Response.header["Content-Disposition"] = "attahment; filename=%s"  
#The Content-Disposition response-header field has been proposed as a means for the origin server to suggest a default filename if the user requests that the content is saved to a file.
	
	return response




#def create_csv(data):
	






if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
