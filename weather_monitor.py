import sys
import math

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from data import db_session
from config import API_KEY
from weather_api import *
from recommendation import *


class WeatherMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        db_session.global_init("data/db.sqlite3")
        uic.loadUi('main_window.ui', self)
        self.searchButton.clicked.connect(self.search_city)


    def search_city(self):
        data = get_weather(city=self.searchInput.text(), api_key=API_KEY)

        self.cityLabel.setText(get_name(data))
        self.tempLabel.setText(F"{get_temp(data)}°C")
        self.descriptionLabel.setText(get_desc(data))
        self.humidityLabel.setText(F"{get_humidity(data)}%")
        self.feelsLikeLabel.setText(F"{get_temp(data)}°C")
        self.windLabel.setText(F"{get_wind(data)}м/с")
        self.pressureLabel.setText(F"{get_pressure(data)}мм")
        self.clothingAdvice.setText(get_clothing_advice(get_temp(data)))

        activity_text = ""
        for activity in get_activity_advice(get_temp(data), get_desc(data), get_wind(data)):
            activity_text += activity + '\n'
        self.activityAdvice.setText(activity_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherMonitor()
    ex.show()
    sys.exit(app.exec())