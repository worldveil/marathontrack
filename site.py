from flask import Flask, render_template
from marathon.scrape import get_name_matches
from marathon.database import *

app = Flask(__name__)

### DEBUG SHOULD BE OFF FOR PRODUCTION ###
DEBUG = True

@app.route('/')
def index():
	return render_template('index.html', message="Start tracking your friends!")
    
@app.route('/<groupname>')
def show_grouppage(groupname):
	runners = []
	if groupname == "stats":
		return render_template('stats.html')
	else:
		runners = GetGroupMembers(groupname)
		return render_template('group.html', groupname=groupname, runners=runners)

if __name__ == '__main__':
    app.run(debug=DEBUG)