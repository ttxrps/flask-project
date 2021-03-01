from flask import Blueprint,render_template,redirect,url_for

# set Name Blueprint => views
views = Blueprint('views', __name__)

# this file for website page

@views.route('/')
def home():
    return render_template('index.html')
