# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # display area
        self.ui.result.setText("0")

        # buttons
        number_buttons = [
            self.ui.pushButton_1,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6,
            self.ui.pushButton_7,
            self.ui.pushButton_8,
            self.ui.pushButton_9,
            self.ui.pushButton_0,
        ]
        for button in number_buttons:
            button.clicked.connect(self.on_number_pressed)


    def on_number_pressed(self):
        buttonText = self.sender().text()
        print(f"number pressed: {buttonText}")
        currentText = self.ui.result.text()
        if currentText == "0":
            self.ui.result.setText(f"{buttonText}")
        else:
            self.ui.result.setText(f"{currentText}{buttonText}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
