#!/home/zkno/Documents/Proyectos/Going-Away-To-College/GoingAwayToCollegeApp/gatcEnv
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsAnOpenSource'

import GoingAwayToCollegeApp.model
import GoingAwayToCollegeApp.view
import GoingAwayToCollegeApp.controller

from GoingAwayToCollegeApp import *

if __name__ == '__main__':
    app.run(debug=True)