from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class ReorderPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order Again?")
        self.setGeometry(100, 100, 500, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        title = QLabel("🛒 Do you want to reorder?")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)

        yes_btn = QPushButton("Yes")
        yes_btn.setStyleSheet("""
            QPushButton {
                background-color: #00aa00;
                color: white;
                font-size: 18px;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover { background-color: #007700; }
        """)
        yes_btn.clicked.connect(self.reorder)
        layout.addWidget(yes_btn)

        no_btn = QPushButton("No")
        no_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff5555;
                color: white;
                font-size: 18px;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover { background-color: #cc4444; }
        """)
        no_btn.clicked.connect(self.close)
        layout.addWidget(no_btn)

        self.setLayout(layout)

    def reorder(self):
        from gui.food_selection import FoodSelection
        self.food_selection_window = FoodSelection()
        self.food_selection_window.show()
        self.close()