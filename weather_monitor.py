import sys
import math
from datetime import datetime

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from data import db_session
from data.cities import Cities
from data.history import History
from config import API_KEY
from weather_api import *
from recommendation import *


class WeatherMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        db_session.global_init("data/db.sqlite3")
        uic.loadUi('main_window.ui', self)

        self.clearHistoryButton.clicked.connect(self.clear_history)
        self.searchButton.clicked.connect(self.search_city)
        self.addFavoriteButton.clicked.connect(self.add_favorite)
        self.removeFavoriteButton.clicked.connect(self.delete_favorite)

        self.load_weather_history()
        self.first_load_favorite_cities()
        self.favoriteCitiesCombo.currentTextChanged.connect(self.on_favorite_selected)

    def search_city(self):
        try:
            if self.searchInput.text() == "":
                return


            data = get_weather(city=self.searchInput.text(), api_key=API_KEY)

            if data["cod"] == "404":
                QMessageBox.warning(self, "Ошибка", "Такого города не существует")
                return

            self.cityLabel.setText(get_name(data))
            self.tempLabel.setText(F"{get_temp(data)}°C")
            self.descriptionLabel.setText(get_desc(data))
            self.humidityLabel.setText(F"{get_humidity(data)}%")
            self.feelsLikeLabel.setText(F"{get_temp(data)}°C")
            self.windLabel.setText(F"{get_wind(data)}м/с")
            self.pressureLabel.setText(F"{get_pressure(data)}мм")
            self.weatherIcon.setText(get_smile(data))

            self.add_to_history(data)
            self.take_advice(data)
            self.display_table()

        except Exception as e:
            print(e)


    def take_advice(self, data):
        advice_text = get_clothing_advice(get_temp(data), get_desc(data), get_wind(data),
                            get_humidity(data))
        activity_text = get_activity_advice(get_temp(data), get_desc(data), get_wind(data),get_humidity(data),get_pressure(data))
        self.activityAdvice.setText(activity_text)
        self.clothingAdvice.setText(advice_text)


    def display_table(self):
        try:
            data, days = get_weather_five_days(city=self.searchInput.text(), api_key=API_KEY)
            self.table.clear()
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels([
                '00:00', '03:00', '06:00', '09:00',
                '12:00', '15:00', '18:00', '21:00'
            ])
            self.table.setRowCount(len(data['temp']))

            for i in range(len(days)):
                if i < self.table.rowCount():
                    self.table.setVerticalHeaderItem(i, QTableWidgetItem(days[i]))

            for day_idx, day_temps in enumerate(data['temp']):
                day_times = data['dt'][day_idx]

                start_column = 0
                if day_times:
                    first_time = day_times[0]
                    hour = int(first_time.split(' ')[1].split(':')[0])

                    for col, time_slot in enumerate(
                            ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']):
                        slot_hour = int(time_slot.split(':')[0])
                        if slot_hour == hour:
                            start_column = col
                            break

                for temp_idx, temp in enumerate(day_temps):
                    column = start_column + temp_idx
                    if column < 8:
                        item = QTableWidgetItem(f"{temp:.1f}°C")
                        item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
                        self.table.setItem(day_idx, column, item)
        except Exception as e:
            print(f"Ошибка отображения прогноза на 5 дней: {e}")


    def add_favorite(self):
        try:
            session = db_session.create_session()
            city_name = self.searchInput.text().strip()
            if session.query(Cities).filter(Cities.city_name==city_name).first() is not None:
                QMessageBox.warning(self, "Ошибка", "Такой город уже есть в избранных!")
                return

            if not city_name:
                QMessageBox.warning(self, "Ошибка", "Введите название города")
                return

            favorite_city = Cities(city_name=city_name)
            session.add(favorite_city)
            session.commit()
            session.close()
            QMessageBox.information(self, "Успешно", F"Город {city_name} был успешно добавлен!")
            self.load_favorite_cities()
        except Exception as e:
            print(f"Ошибка добавления избранного: {e}")


    def delete_favorite(self):
        try:
            session = db_session.create_session()
            city_name = self.favoriteCitiesCombo.currentText()

            if not city_name:
                QMessageBox.warning(self, "Ошибка", "Введите название города")
                return

            favorite_city = session.query(Cities).filter(Cities.city_name == city_name).first()
            session.delete(favorite_city)
            session.commit()
            session.close()
            QMessageBox.information(self, "Успешно", F"Город {city_name} был успешно удален!")
            self.load_favorite_cities()
        except Exception as e:
            print(f"Ошибка удаления избранного: {e}")


    def first_load_favorite_cities(self):
        try:
            session = db_session.create_session()
            cities = session.query(Cities).all()
            session.close()

            self.favoriteCitiesCombo.clear()
            for city in cities:
                self.favoriteCitiesCombo.addItem(city.city_name)

            first_city = session.query(Cities).first()
            self.searchInput.setText(str(first_city.city_name))

        except Exception as e:
            print(f"Ошибка первой загрузки избранного: {e}")


    def load_favorite_cities(self):
        try:
            session = db_session.create_session()
            cities = session.query(Cities).all()
            session.close()

            self.favoriteCitiesCombo.clear()
            for city in cities:
                self.favoriteCitiesCombo.addItem(city.city_name)

        except Exception as e:
            print(f"Ошибка загрузки избранного: {e}")


    def on_favorite_selected(self, city_name):
        try:
            self.searchInput.setText(str(city_name))
        except Exception as e:
            print(f"Ошибка выбора избранного: {e}")


    def add_to_history(self, weather_data):
        try:
            session = db_session.create_session()

            obj = History(
                city_name=get_name(weather_data),
                city_temp=get_temp(weather_data),
                city_humidity=get_humidity(weather_data),
                city_pressure=get_pressure(weather_data),
                city_wind_speed=get_wind(weather_data),
                city_weather_desc=get_desc(weather_data),
                city_weather_data=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            )

            session.add(obj)
            session.commit()
            session.close()
            self.load_weather_history()

        except Exception as e:
            print(f"Ошибка добавления в историю: {e}")


    def load_weather_history(self):
        try:
            session = db_session.create_session()
            history = session.query(History).all()
            session.close()

            self.historyTable.setRowCount(0)
            for row, record in enumerate(history):
                self.historyTable.insertRow(row)
                self.historyTable.setItem(row, 0, QTableWidgetItem(record.city_name))
                self.historyTable.setItem(row, 1, QTableWidgetItem(f"{record.city_temp}°C"))
                self.historyTable.setItem(row, 2, QTableWidgetItem(f"{record.city_humidity}%"))
                self.historyTable.setItem(row, 3, QTableWidgetItem(f"{record.city_pressure}мм"))
                self.historyTable.setItem(row, 4, QTableWidgetItem(f"{record.city_wind_speed}м/с"))
                self.historyTable.setItem(row, 5, QTableWidgetItem(f"{record.city_weather_desc}"))
                self.historyTable.setItem(row, 6, QTableWidgetItem(f"{record.city_weather_data}"))

        except Exception as e:
            print(f"Ошибка загрузки истории: {e}")


    def clear_history(self):
        try:
            reply = QMessageBox.question(
                self, 'Подтверждение',
                'Вы уверены, что хотите очистить историю запросов?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                session = db_session.create_session()
                history = session.query(History).all()
                for i in history:
                    session.delete(i)
                session.commit()
                session.close()

                self.load_weather_history()
                QMessageBox.information(self, "Успех", "История очищена")

        except Exception as e:
            print(f"Ошибка удаления истории: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherMonitor()
    ex.show()
    sys.exit(app.exec())