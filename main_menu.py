from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 Drone Delivery")
        self.setGeometry(100, 100, 500, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        title = QLabel("🚀 Welcome to Drone Delivery")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.order_button = QPushButton("Order")
        self.order_button.setStyleSheet("""
            QPushButton {
                background-color: #00aaff;
                color: white;
                font-size: 18px;
                border-radius: 12px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #0088cc; }
        """)
        self.order_button.clicked.connect(self.open_food_selection)
        layout.addWidget(self.order_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #ff5555;
                color: white;
                font-size: 18px;
                border-radius: 12px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #cc4444; }
        """)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def open_food_selection(self):
        from gui.food_selection import FoodSelection  # استيراد متأخر لتجنب circular import
        self.food_selection_window = FoodSelection()
        self.food_selection_window.show()
        self.close()