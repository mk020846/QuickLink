import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from quicklink_ui import Ui_MainWindow

class QuickLink(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
while True:
    try:
        if __name__ == '__main__' :
            app = QtWidgets.QApplication(sys.argv)
            window = QuickLink()
            window.show()
            sys.exit(app.exec())
    except Exception as e:
        print(e)