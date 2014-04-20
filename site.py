from flask import Flask, render_template
from marathon.scrape import search_for_bibs
from marathon.database import *
from flask import request
import json

app = Flask(__name__)

### DEBUG SHOULD BE OFF FOR PRODUCTION ###
DEBUG = True

@app.route('/')
def index():
	return render_template('index.html', message="Start tracking your friends!")

@app.route('/addgroup', methods=["POST", "GET"])
def addgroup():
	runners = []
	if request.method == "POST":
		print request.form
		first = request.form.get("first", "")
		last = request.form.get("last", "")
		print first, last
		runners = search_for_bibs(first, last)
	return render_template('addgroup.html', runners=runners)

@app.route('/groups/<groupname>', methods=["POST", "GET"])
def show_grouppage(groupname):
	runners = GetGroupMembers(groupname)
	return render_template('group.html', groupname=groupname, runners=runners)

if __name__ == '__main__':
    if DEBUG:
    	app.run(debug=DEBUG)
    else:
    	app.run(debug=DEBUG, port=80, host="0.0.0.0:80")