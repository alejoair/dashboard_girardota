
from dotenv import load_dotenv
load_dotenv()
from os import environ
import requests
import numpy as np
import time

def req(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': address, "key": environ["GOOGLE_API_KEY"]}

    r = requests.get(url, params=params)
    results = r.json()['results']
    time.sleep(0.021)
    try:
        location = results[0]['geometry']['location']
        return [location['lat'], location['lng']]
    except:
        return [np.nan, np.nan]
