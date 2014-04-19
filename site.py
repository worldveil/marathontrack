from flask import Flask, render_template
app = Flask(__name__)

### DEBUG SHOULD BE OFF FOR PRODUCTION ###
DEBUG = True

@app.route('/')
def index():
	return render_template('index.html', message="Start tracking your friends!")
    
@app.route('/<groupname>')
def show_grouppage(groupname):
    return 'Page for group %s' % groupname

if __name__ == '__main__':
    app.run(debug=DEBUG)