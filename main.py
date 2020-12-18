import requests
import sys
import os
import time
from PyQt5 import *
from PyQt5.QtCore import Qt, QSize
from  PyQt5.QtGui import *
import json

API_KEY = '9bbada05362257f22ae6c1dd8222be26'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
#api.openweathermap.org/data/2.5/weather?q=Lviv,uk&APPID=9bbada05362257f22ae6c1dd8222be26
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Lvov,ua&appid={}'.format(API_KEY))
#language = requests.get('http://api.openweathermap.org/data/2.5/weather?id=524901&appid={9bbada05362257f22ae6c1dd8222be26}&lang={ua}')

params = {
        'appid': API_KEY,
        'q':    'Lvov',
        'units': 'metric',
        'lang': 'ua'
         }

r = requests.get(API_URL, params=params)
weather = r.json()
print(weather)
#print(r.status_code)
