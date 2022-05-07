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
        super().__init__(parent)
        # Create and initialize UI elements:
        self.ui = MainFormUI()
        self.ui.setupUi(self)
        self.__current_form = None
        #start with form 1
        self.replace_form(FirstForm.get_instance())

    def __del__(self):
        self.ui = None

    def replace_form(self, new_form):
        # Replace and orpham current form if it's present
        if self.__current_form is None:
            self.ui.grid.addWidget(new_form)
        else:
            self.ui.grid.replaceWidget(self.__current_form, new_form)
            self.__current_form.setParent(None)
        # Set parent of a new form, update main window title, safe reference
        self.setWindowTitle(new_form.windowTitle())
        new_form.setParent(self)
        self.__current_form = new_form


class FirstForm(FirstFormBase):
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self, parent=None):
        # Singleton pattern
        if type(self).__instance is not None:
            raise Exception('attempt to create second instance')
        # Initialize base form:
        super().__init__(parent)
        # Create and initialize UI elements:
        self.ui = FirstFormUI()
        self.ui.setupUi(self)
        # Attach event handlers:
        self.ui.switch_button.clicked.connect(self.__switch_to_form_two)

    def __del__(self):
        self.ui = None

    def __switch_to_form_two(self):
        parent = self.parent()
        parent.replace_form(SecondForm.get_instance())

class SecondForm(SecondFormBase):
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self, parent=None):
        #singleton pattern
        if type(self).__instance is not None:
            raise Exception('attempt to create second instance')
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
        self.parent().replace_form(FirstForm.get_instance())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
