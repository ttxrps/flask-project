import requests

def fetchAPOD():
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    api_key = 'PIQgwKgT5WieoxPWMksJNr1GtdtIktdVc01dc6Jr'
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