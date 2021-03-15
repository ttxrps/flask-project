import requests,datetime,json
from urllib.request import urlopen
from flask import request

def fetchAPOD():
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    api_key = 'PIQgwKgT5WieoxPWMksJNr1GtdtIktdVc01dc6Jr'
    # now = datetime.datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day - 1
    # date = str(year)+'-'+str(month)+'-'+str(day)
    date = '2018-11-14'
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

def fetchAsteroidNeowsFeed():
    URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
    api_key = '7UbkT3dVXEXJHRbZ7VV0J2eJ6aXMK7XGAgXba2UH'
    params = {
        'api_key': api_key,
        'start_date': '2021-03-09'
    }
    response = requests.get(URL_NeoFeed, params=params).json()
    NEO = response['near_earth_objects']['2021-03-09']
    ID = []
    name = []
    link = []
    for i in range(1,13):
        myNeoFeed = NEO[i]
        ID.append(myNeoFeed['id'])
        name.append(myNeoFeed['name'])
        link.append(myNeoFeed['nasa_jpl_url'])
    myFeed = zip(ID,name,link)
    return myFeed

def fetchInSightMars():
    URL_Mars = "https://api.nasa.gov/insight_weather/?api_key=7UbkT3dVXEXJHRbZ7VV0J2eJ6aXMK7XGAgXba2UH&feedtype=json&ver=1.0"
    url = urlopen(URL_Mars).read()
    parsed_mars = json.loads(url)
    mars = None
    first_UTC = parsed_mars['811']['First_UTC'] 
    last_UTC = parsed_mars['811']['Last_UTC']
    month_ordinal = parsed_mars['811']['Month_ordinal']
    northern_season = parsed_mars['811']['Northern_season']
    season = parsed_mars['811']['Season']
    southern_season = parsed_mars['811']['Southern_season']
        
    mars = {'first_UTC': first_UTC, 
            'last_UTC': last_UTC,
            'month_ordinal': month_ordinal,
            'northern_season': northern_season,
            'season': season,
            'southern_season': southern_season
            }
    return mars

def get_image():
    scr_date = request.args.get('date')
    if not scr_date:
        scr_date = '2019-05-30'
    url = 'https://api.nasa.gov/EPIC/api/natural/date/{0}?api_key=PIQgwKgT5WieoxPWMksJNr1GtdtIktdVc01dc6Jr'
    url_img = url.format(scr_date)
    data = urlopen(url_img).read()
    parsed = json.loads(data)
    img = []
    for i in range(6):
        earth = parsed[i]
        get_image =  earth['image']
        date = earth['date']
        date = date[0:10]
        date_fom = date.replace('-','/')
        img_link = fetchEPICImage(get_image,date_fom)
        img.append(img_link)
    mylist = img
    return mylist

def fetchEPICImage(get_image,date_fom):
    URL_EPIC = "https://epic.gsfc.nasa.gov/archive/natural/"
    URL_EPIC = URL_EPIC + date_fom
    URL_EPIC = URL_EPIC + '/png/'
    URL_EPIC = URL_EPIC + get_image + '.png'
    return URL_EPIC
