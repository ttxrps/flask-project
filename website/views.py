from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from urllib.parse import quote
from urllib.request import urlopen
from . import db
import json
import requests

URL_APOD = "https://api.nasa.gov/planetary/apod{0}"
api_key = 'PIQgwKgT5WieoxPWMksJNr1GtdtIktdVc01dc6Jr'

# create Blueprint name => views
views = Blueprint('views', __name__)

# this is home page website


@views.route('/', methods=['GET', 'POST'])
# if not login can't enter
@login_required
def home():
    APOD = fetchAPOD()
    return render_template("home.html", user=current_user, APOD=APOD)


def fetchAPOD():
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    api_key = 'PIQgwKgT5WieoxPWMksJNr1GtdtIktdVc01dc6Jr'
    date = '2021-02-13'
    params = {
        'api_key': api_key,
        'date': date,
        'hd': 'True'
    }
    response = requests.get(URL_APOD, params=params).json()
    APOD = {'title': response['title'],
                    'explanation': response['explanation'],
                    'daily': response['date'],
                    'hdurl': response['hdurl']
                    }

    return APOD


