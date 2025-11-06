import sys
import math

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from data import db_session


class WeatherMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        db_session.global_init("data/db.sqlite3")
        uic.loadUi('main_window.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherMonitor()
    ex.show()
    sys.exit(app.exec())