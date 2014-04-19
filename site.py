from flask import Flask, render_template
from marathon.scrape import get_name_matches
from marathon.database import *
from flask import request
import json

app = Flask(__name__)

### DEBUG SHOULD BE OFF FOR PRODUCTION ###
DEBUG = True

@app.route('/')
def index():
	return render_template('index.html', message="Start tracking your friends!")

@app.route('/addgroup')
def addgroup():
	first = request.args.get("first", "")
	last = request.args.get("last", "")
	runners = get_name_matches(first, last)
	return render_template('addgroup.html', runners=runners)

@app.route('/groups/<groupname>', methods=["POST", "GET"])
def show_grouppage(groupname):
	runners = GetGroupMembers(groupname)
	return render_template('group.html', groupname=groupname, runners=runners)

if __name__ == '__main__':
    app.run(debug=DEBUG)