from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from urllib.parse import quote
from urllib.request import urlopen
from . import db
from .function import fetchAPOD

# create Blueprint name => views
views = Blueprint('views', __name__)

# this is home page website
@views.route('/', methods=['GET', 'POST'])
# if not login can't enter
@login_required
def home():
    APOD = fetchAPOD()
    return render_template("home.html", user=current_user, APOD=APOD)


@views.route('/team', methods=['GET', 'POST'])
@login_required
def team():
    return render_template('team.html',user=current_user)
