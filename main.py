import requests
import sys
import os
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from  PyQt5.QtGui import *
import json
import style

API_KEY = '9bbada05362257f22ae6c1dd8222be26'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Lvov,ua&appid={}'.format(API_KEY))


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Погода')
        self.setGeometry(450, 150, 370, 370)
        self.setStyleSheet(style.displayLabelStyle())
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('icons/world.ico'))
        self.UI()
        self.show()

    def UI(self):
        self.searchLine = QLineEdit()
        self.searchLine.setPlaceholderText('Введіть запит міста')
        self.searchBtn = QPushButton('Запит')
        self.searchBtn.setStyleSheet(style.btnStyle())
        self.searchBtn.clicked.connect(self.getValue)
        self.displayLabel = QLabel()
        self.displayLabel.setAlignment(Qt.AlignLeft)

        self.mainLayout = QVBoxLayout()
        self.topLayout = QFormLayout()
        self.bottomLayout = QHBoxLayout()
        self.topLayout.addRow(self.searchLine, self.searchBtn)
        self.bottomLayout.addWidget(self.displayLabel)

        self.mainLayout.addLayout(self.topLayout, 15)
        self.mainLayout.addLayout(self.bottomLayout, 85)
        self.setLayout(self.mainLayout)

    def getValue(self):
        global city
        global info
        city = self.searchLine.text()
        self.displayLabel.setText(getWeather())
        if city == "":
            self.displayLabel.setText(info)

def displayWeather(weather):
    city = weather['name']
    country = weather['sys']['country']
    temp = weather['main']['temp']
    temp = float(round(temp))
    temp = str(temp)
    press = weather['main']['pressure']
    humidity = weather['main']['humidity']
    wind = weather['wind']['speed']
    desc = weather['weather'][0]['description']
    sunriseTs = weather['sys']['sunrise']
    sunsetTs = weather['sys']['sunset']
    sunriseTsLocal = time.localtime(sunriseTs)
    sunsetTsLocal = time.localtime(sunsetTs)
    sunrise = time.strftime('%H:%M:%S', sunriseTsLocal)
    sunset = time.strftime('%H:%M:%S', sunsetTsLocal)
    return 'Погода в {}-{}\nТемпература: {} °C\nАтм. тиск: {}гПа\nВологість: {}%\nШвидкість вітру: {}м/c\nПогодні умови: {}\nСхід: {}\nЗахід: {}'.format(city, country, temp, press, humidity, wind, desc, sunrise, sunset)

def getWeather():
    global city
    global info
    try:
        if 'q' != '' or 'apid' != API_KEY:
            params = {
            'appid': API_KEY,
            'q': city,
            'units': 'metric',
            'lang': 'ua'
                }
            r = requests.get(API_URL, params=params)
            weather = r.json()
            return displayWeather(weather)
        else:
            info = 'Problem with internet connection!'
    except:
        info = 'Не коректне введення данних!'


def main():
    APP= QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()