"""
Website using Flask to summarize text using an API
"""

from pickle import TRUE
import random
import re
from webbrowser import get
from click import argument
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
from cgitb import html
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import *
import API
load_dotenv(find_dotenv())

app = Flask(__name__)

app.secret_key = os.getenv('secret_key')

app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')


db = SQLAlchemy(app)
db.init_app(app)

lm = LoginManager()
lm.login_view = 'auth.login'
lm.init_app(app)

#this databse will keep track of all the users and will be used later for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),  nullable = True)
    
    def __repr__(self):
        return '<Comments %r>' % self.username
    def __str__(self):
        return f'{self.username}'
    
    def is_authenticated(self):
        return super().is_authenticated
    def is_anonymous(self):
        return super().is_anonymous

#this databse will keep track of all the summaries each user made 
class Summeries(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),  nullable = True)
    summary_title = db.Column(db.String(100), nullable = True)
    summary = db.Column(db.String(None), nullable = True)
    
    def __str__(self):
       return f'{self.username} {self.summary}'
    def is_authenticated(self):
        return super().is_authenticated
    def is_anonymous(self):
        return super().is_anonymous

@lm.user_loader
def load_user(username):
    return User.query.get(int(username))

@lm.unauthorized_handler
def unauth():
    flash('INVALID URL OR LOG IN TO ACCESS THIS PAGE')
    return redirect(url_for('login'))  

with app.app_context():
    db.create_all()

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/handle_login', methods = ['POST'])
def handle_login_submission():
    form_data = request.form
    username = form_data['username']
    if username == '':
        flash("enter a username")
        return redirect(url_for('login'))

    user = User.query.filter_by(username = username).first()
    #global current_user; current_user = username
    global current_username; current_username = username
    if user:
        login_user(user)
        return redirect(url_for('index'))
    else:
        flash ('please try again')
        return redirect(url_for('login'))
        

@app.route('/signup')
def signup():
    return render_template('signup.html')

#adding the user to the user database in this one 

@app.route('/handle_signup',methods = ['POST'])
def handle_signup_submission():
    form_data = request.form
    username = form_data['username']
    if username == '':
        flash("enter a username")
        return redirect(url_for('signup'))
    auth_user = User(username = username)
    db.session.add(auth_user)  
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/main') 
def index():
    return render_template('main_page.html')

@app.route('/')
def log_out():
    logout_user()
    return redirect(url_for('index'))

@app.route('/summerize_text', methods = ['POST'])
def summerize_text():
    form_data = request.form
    initial_text = form_data['initial_text']
    global summary_title; summary_title = form_data['summary_title']
    global summary; summary = API.get_model_data(initial_text)
    return redirect(url_for('summary_maker'))


@app.route('/summary')
def summary_maker():
    #will return the summary of the initial text 
    return render_template(
        'summary_page.html', 
        html_summary = summary
    )

@app.route('/view_summeries', methods = ['POST'])
@login_required
def view_summeries():
    saved_summary = Summeries(username = current_username, summary = summary, summary_title = summary_title)
    db.session.add(saved_summary)  
    db.session.commit()   
    return redirect(url_for('your_summeries'))


@app.route('/your_summaries')
@login_required
def your_summeries():
    database_data = Summeries.query.filter_by(username = current_username).all()
    return render_template(
        'your_summeries.html', 
        html_entries = database_data,  
        username = current_username
        )

#app.run() 