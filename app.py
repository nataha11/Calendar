#!/usr/bin/python3

import os.path as op
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def load_form(form_name):
    return uic.loadUiType(op.join(op.dirname(__file__), form_name))

MainFormUI, MainForm = load_form('main.ui')
FirstFormUI, FirstFormBase = load_form('form_one.ui')
SecondFormUI, SecondFormBase = load_form('form_two.ui')

class MainWindow(MainForm):
    def __init__(self, parent=None):
        # Initialize base form:
        super().__init__()
        # Create and initialize UI elements:
        self.ui = MainFormUI()
        self.ui.setupUi(self)

    def __del__(self):
        self.ui = None

class FirstForm(FirstFormBase):
    def __init__(self, parent=None):
        # Initialize base form:
        super().__init__()
        # Create and initialize UI elements:
        self.ui = FirstFormUI()
        self.ui.setupUi(self)
        # Attach event handlers:
        self.ui.switch_button.clicked.connect(self.__switch_to_form_two)

    def __del__(self):
        self.ui = None

    def __switch_to_form_two(self):
        return

class SecondForm(SecondFormBase):
    def __init__(self, parent=None):
        # Initialize base form:
        super().__init__()
        # Create and initialize UI elements:
        self.ui = SecondFormUI()
        self.ui.setupUi(self)
        # Attach event handlers:
        self.ui.switch_button.clicked.connect(self.__switch_to_form_one)

    def __del__(self):
        self.ui = None

    def __switch_to_form_one(self):
        return

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
