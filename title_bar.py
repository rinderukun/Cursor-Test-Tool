import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QMouseEvent

class TitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        bar_height = 60
        button_size = 40

        # Создаем макет (вертикальный):
        layout = QVBoxLayout()

        self.test_widget = QWidget()
        self.test_widget.setObjectName("test_widget")
        self.test_widget.setFixedHeight(bar_height)

        # Создаем надпись:
        title_label = QLabel("Cursor Test Tool", self.test_widget)
        title_label.setGeometry(10, 15, 200, 30)  # x, y, ширина, высота
        title_label.setObjectName("title_label")

        # Создаем кнопки:
        close_button = QPushButton("X", self.test_widget)
        close_button.setGeometry(250, 10, button_size, button_size)  # x, y, width, height
        close_button.setObjectName("close_button")
        close_button.clicked.connect(self.close_window_clicked)

        minimaze_button = QPushButton("_", self.test_widget)
        minimaze_button.setGeometry(200, 10, button_size, button_size)  # x, y, width, height
        minimaze_button.setObjectName("minimaze_button")
        minimaze_button.clicked.connect(self.on_minimize_button_clicked)

        # Добавляем виджет с измененным цветом фона в главный макет
        layout.addWidget(self.test_widget)
        layout.setContentsMargins(0,0,0,0)
        
        # Устанавливаем макет:
        self.setLayout(layout)

        self.setStyleSheet("""
            QLabel#title_label {
                font-size: 14px;
                font-weight: bold;
                color: #FFCCCC;
            }

            QPushButton#close_button {
                background-color: #FF9999;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#close_button:hover {
                background-color: #FFCCCC;
            }
                           
            QPushButton#minimaze_button {
                background-color: #FF9999;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#minimaze_button:hover {
                background-color: #FFCCCC;
            }
                           
            QWidget#test_widget {
                background-color: #FF6666;
            }
                           
            """)

        # Переменные для перетаскивания окна
        self.isDragging = False
        self.dragStartPosition = QPoint()
        # Подключаем события мыши только к панели перемещения
        self.test_widget.installEventFilter(self)
    
    def close_window_clicked(self):
        QApplication.quit()

    def on_minimize_button_clicked(self):
        QApplication.activeWindow().showMinimized()

    def eventFilter(self, obj, event):
        if obj == self.test_widget:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = event  # Преобразование в QMouseEvent
                if mouseEvent.button() == Qt.LeftButton:
                    self.isDragging = True
                    self.dragStartPosition = mouseEvent.globalPosition().toPoint()
            elif event.type() == QEvent.MouseMove:
                if self.isDragging:
                    mouseEvent = event  # Преобразование в QMouseEvent
                    delta = mouseEvent.globalPosition().toPoint() - self.dragStartPosition
                    # Перемещение родительского окна, а не только test_widget
                    self.parent().move(self.parent().pos() + delta)
                    self.dragStartPosition = mouseEvent.globalPosition().toPoint()
            elif event.type() == QEvent.MouseButtonRelease:
                mouseEvent = event  # Преобразование в QMouseEvent
                if mouseEvent.button() == Qt.LeftButton:
                    self.isDragging = False
        return super().eventFilter(obj, event)