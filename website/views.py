from flask import Blueprint,render_template,request,flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

# create Blueprint name => views
views = Blueprint('views', __name__)

# this is home page website
@views.route('/', methods=['GET', 'POST'])
# if not login can't enter
@login_required
def home():
    return render_template("home.html", user=current_user)


