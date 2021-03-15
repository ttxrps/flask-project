from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website.models import User
from .function import fetchAPOD,fetchAsteroidNeowsFeed,fetchInSightMars,get_image



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
    return render_template('team.html',user=current_user,teams = User.query.all())
    
@views.route('/neo', methods=['GET', 'POST'])
@login_required
def neo():
    myFeed = fetchAsteroidNeowsFeed()
    return render_template('neo.html', user=current_user, myFeed=myFeed)

@views.route('/mars', methods=['GET', 'POST'])
@login_required
def Mars():
    mars = fetchInSightMars()
    return render_template('mars.html', user=current_user,mars=mars)

@views.route('/earth', methods=['GET', 'POST'])
@login_required
def earth():
    mylist = get_image()
    return render_template('earth.html',user=current_user,list = mylist)
