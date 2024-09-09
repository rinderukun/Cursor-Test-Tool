import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtGui import QIcon
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PySide6.QtWidgets import QSystemTrayIcon
from PySide6.QtGui import QIcon

from title_bar import TitleBar
from content import ContentPlace

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'rinderu.cursorTestTool.subproduct.1.0.0.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


# Главное окно системы и главный виджет:
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 400) # Устанавливаем размер окна
        self.setWindowFlags(Qt.FramelessWindowHint)  # Убираем стандартный заголовок

        self.setStyleSheet("""
            outline: none;
            padding: 0px;
            margin: 0px;
            border: 0px;
            """)

        # Создаем экземпляры пользовательских виджетов
        title_bar = TitleBar(self)
        self.setMenuWidget(title_bar) # Делаем виджет шапкой

        main_contest = ContentPlace(self)
        self.setCentralWidget(main_contest)

# Основной блок
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icon.ico')))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())