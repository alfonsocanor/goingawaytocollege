from GoingAwayToCollegeApp import app
#import request
from flask import render_template, request
from controller import profileDML
from helper.view import forms

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/createProfile', methods=['GET', 'POST'])
def createProfile():
    form = forms.CreateProfile(request.form)
    if(request.method == 'POST'):
        profileDML.create(form.name.data)
    return render_template('createprofile.html', form=form)

@app.route('/login_alumni')
def login_alumni():
    return redirect(url_for('login'))