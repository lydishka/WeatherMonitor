import sys
import math

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class WeatherMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherMonitor()
    ex.show()
    sys.exit(app.exec())