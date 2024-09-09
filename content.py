import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QCursor

class ContentPlace(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        styleButton = """
            QPushButton {
                background-color: lightblue;  /* Цвет кнопки по умолчанию */
                border: 0px;      /* Граница кнопки */
                padding: 10px;                /* Отступы внутри кнопки */
            }
            QPushButton:hover {
                background-color: lightgreen; /* Цвет кнопки при наведении */
            }
        """

        # Создание кнопок
        self.button = []
        self.button.append(QPushButton("Arrow Cursor"))
        self.button.append(QPushButton("Whats This Cursor"))
        self.button.append(QPushButton("Busy Cursor"))
        self.button.append(QPushButton("Wait Cursor"))
        self.button.append(QPushButton("Cross Cursor"))
        self.button.append(QPushButton("I Beam Cursor"))
        self.button.append(QPushButton("Forbidden Cursor"))
        self.button.append(QPushButton("Size Ver Cursor"))
        self.button.append(QPushButton("Size Hor Cursor"))
        self.button.append(QPushButton("Size BDiag Cursor"))
        self.button.append(QPushButton("Size FDiag Cursor"))
        self.button.append(QPushButton("Size All Cursor"))
        self.button.append(QPushButton("Up Arrow Cursor"))
        self.button.append(QPushButton("Pointing Hand Cursor"))

        self.button_args = {
            self.button[0]: Qt.ArrowCursor,
            self.button[1]: Qt.WhatsThisCursor,
            self.button[2]: Qt.BusyCursor,
            self.button[3]: Qt.WaitCursor,
            self.button[4]: Qt.CrossCursor,
            self.button[5]: Qt.IBeamCursor,
            self.button[6]: Qt.ForbiddenCursor,
            self.button[7]: Qt.SizeVerCursor,
            self.button[8]: Qt.SizeHorCursor,
            self.button[9]: Qt.SizeBDiagCursor,
            self.button[10]: Qt.SizeFDiagCursor,
            self.button[11]: Qt.SizeAllCursor,
            self.button[12]: Qt.UpArrowCursor,
            self.button[13]: Qt.PointingHandCursor,
        }

        # Создание layout
        grid_layout = QGridLayout()

        col = 0
        row = 0
        for i in range(0, len(self.button)):
            # Установка растягивающихся размеров для кнопок
            self.button[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # Установка растягивающихся стиля
            self.button[i].setStyleSheet(styleButton)
            # Установка поведения при наведении курсора
            self.button[i].installEventFilter(self)
            # Размещение кнопок в сетке 2x2
            grid_layout.addWidget(self.button[i], row, col)
            col+=1
            if col>1:
                col = 0
                row+=1

        # Установка layout для главного
        self.setLayout(grid_layout)

    # наведение курсора:
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            # Установка курсора загрузки при наведении на кнопку
            self.setCursor(QCursor(self.button_args[obj]))
        elif event.type() == QEvent.Leave:
            # Восстановление обычного курсора, когда курсор покидает кнопку
            self.setCursor(QCursor(Qt.ArrowCursor))
        # Метод eventFilter в PyQt/PySide позволяет фильтровать события
        # перед тем, как они достигнут целевого виджета
        return super().eventFilter(obj, event)

        

