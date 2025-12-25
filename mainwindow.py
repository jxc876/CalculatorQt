# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
import Calculator

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):

    calculator = Calculator.Calculator()
    number_buttons = []
    operation_buttons = []
    other_buttons = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # display area
        self.ui.result.setText("0")
        self.setup_buttons()
        self.style_buttons()


    def setup_buttons(self):
        self.number_buttons = [
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

        self.operation_buttons = [
            self.ui.pushButton_add,
            self.ui.pushButton_minus,
            self.ui.pushButton_mult,
            self.ui.pushButton_div
        ]

        self.other_buttons= [
            self.ui.pushButton_eq,
            self.ui.pushButton_back,
            self.ui.pushButton_ce,
            self.ui.pushButton_ac,
            self.ui.pushButton_sign
        ]

        # connect signals
        for button in self.number_buttons:
            button.clicked.connect(self.on_number_pressed)

        # connect signals
        for button in self.operation_buttons:
            button.clicked.connect(self.on_number_pressed)

        # connect signals
        for button in self.other_buttons:
            button.clicked.connect(self.on_number_pressed)


    def style_buttons(self):
        for button in self.number_buttons:
            button.setStyleSheet("""
            QPushButton {
                border: 2px solid black;
                border-radius: 6px;
            }
            """)
        for button in self.operation_buttons:
            button.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 153, 107);
                border: 2px solid black;
                border-radius: 6px;
            }
            """)

    def on_number_pressed(self):
        # figure out which button was pressed
        buttonText = self.sender().text() # ex: "0", "1", "+"
        print(f"ui - button pressed: {buttonText}")

        # run logic
        self.calculator.put(buttonText)

        # update the display
        display_str = self.calculator.display_str
        self.ui.result.setText(display_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
