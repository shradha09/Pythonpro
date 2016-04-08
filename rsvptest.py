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


response = make_response(items)
        response.header["Content-Disposition"] = "attahment; filename=%s" % file_name

#The Content-Disposition response-header field has been proposed as a means for the origin server to suggest a default filename if the user requests that the content is saved to a file.

        return response


	

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)



#return Response(items,
        #               mimetype="text/plain",
        #               headers={"Content-Disposition":
        #                            "attachment;filename=test.txt"})
	
#	c = mongoexport -d rsvpdata -c rsvpdata --out rsvpdata.csv --fields name,email
# convert Json to CSV
     
     #rsvp_parsed = json.loads(items) 
     #rsvp_data = rsvp_parsed['rsvpdata']  #mongo-collection-name
	#open  a csv file for writing

		# data = open('/tmp/rsvp.csv', 'w')

		
	#create the csv writer object
	
	# csvwriter = csv.writer(filename)

	#count = 0

# for rsvp in rsvp_data
	# if count == 0 :
		# header = emp.keys()
		# csvwriter.writerow(header)
		# count += 1
	#csvwriter.writerow(rsvp.values())
#rsvp_data.close()


