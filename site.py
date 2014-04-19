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

@app.route('/<groupname>', methods=["POST", "GET"])
def show_grouppage(groupname):
	runners = []
	if groupname == "stats":
		return render_template('stats.html')
	elif groupname == "addgroup":
		first = request.form.get("first", "")
		last = request.form.get("last", "")
		matches = get_name_matches(first, last)
		return render_template('addgroup.html', matches=json.dumps(matches))
	else:
		first = request.form.get("first", "")
		last = request.form.get("last", "")
		matches = get_name_matches(first, last)
		return render_template('api.html', matches=json.dumps(matches))

if __name__ == '__main__':
    app.run(debug=DEBUG)