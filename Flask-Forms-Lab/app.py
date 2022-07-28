from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


accounts = {"omar16":"omar2006", "loay18": "loay2004", "qais11": "qais2011"}
facebook_friends=["Eran H","Loay","Qais", "Samer", "Farid", "Zain"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')

	else:
		name = request.form['username']
		password1 = request.form['password']
	if name.lower() in accounts and password1 in accounts[name.lower()]:
		return redirect(url_for('homepage'))

@app.route('/home', methods=['GET', 'POST'])
def homepage():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:friend>', methods=['GET', 'POST'])
def friendspage(friend):
	if friend in facebook_friends:
		return render_template('friend_exists.html', name=friend, myfriend= True)
	else:
		return render_template('friend_exists.html', name=friend, myfriend= False)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)