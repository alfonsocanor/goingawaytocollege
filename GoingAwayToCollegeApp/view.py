from GoingAwayToCollegeApp import app
from flask import render_template, request, flash
from sqlalchemy.exc import IntegrityError
from controller import session, profileDML
from helper.view import forms

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/createProfile', methods=['GET', 'POST'])
def createProfile():
    form = forms.CreateProfile(request.form)
    if(request.method == 'POST'):
        try:
            print('try?')
            profileDML.create(form.name.data)
            flash('The profile ' + str(form.name.data) + 'has been Successfuly created')
        except IntegrityError:
            print('except?')
            session.rollback()
            print(session)
            flash('The profile ' + str(form.name.data) + 'already exist. ')
    return render_template('createprofile.html', form=form)

@app.route('/login_alumni')
def login_alumni():
    return redirect(url_for('login'))