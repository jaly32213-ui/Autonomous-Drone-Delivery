from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    from gui.main_menu import MainMenu
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())