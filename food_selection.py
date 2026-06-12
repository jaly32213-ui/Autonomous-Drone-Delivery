from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class FoodSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🍔 Select Your Food")
        self.setGeometry(100, 100, 500, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        title = QLabel("🍔 Choose Your Food")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)

        foods = ["Pizza", "Burger", "Pasta", "Sushi"]
        for food in foods:
            btn = QPushButton(food)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffaa00;
                    color: white;
                    font-size: 16px;
                    border-radius: 10px;
                    padding: 8px;
                }
                QPushButton:hover { background-color: #cc8800; }
            """)
            btn.clicked.connect(lambda checked, f=food: self.start_drone(f))
            layout.addWidget(btn)

        self.setLayout(layout)

    def start_drone(self, food_choice):
        from gui.drone_window import DroneWindowReal  # استيراد متأخر
        self.drone_window = DroneWindowReal(food_choice)
        self.drone_window.show()
        self.close()