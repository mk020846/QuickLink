import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import send_file
import recieve_file
import threading
class Ui_MainWindow(object):
    def send_file(self):
        filename = self.lineEdit.text()
        filepath = self.lineEdit_2.text()
        process1 = threading.Thread(target=send_file.send,args=(filename,filepath))
        process1.start()
    def recv_file(self):
        host = self.lineEdit_3.text()
        port = int(self.lineEdit_4.text())
        process2 = threading.Thread(target=recieve_file.recv,args=(host,port))
        process2.start()

    def setupUi(self, QuickLink):
        QuickLink.setObjectName("QuickLink")
        QuickLink.resize(640, 480)
        QuickLink.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(QuickLink)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 0, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 34, 191, 31))
        self.lineEdit.setStyleSheet("font: 75 italic 10pt \"DejaVu Math TeX Gyre\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 181, 21))
        self.label.setStyleSheet("font: 10pt \"MathJax_AMS\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 10, 151, 20))
        self.label_2.setStyleSheet("font: 10pt \"MathJax_AMS\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.label_3.setStyleSheet("font: 75 italic 10pt \"DejaVu Math TeX Gyre\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.label_4.setStyleSheet("font: 75 italic 10pt \"DejaVu Math TeX Gyre\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 26, 62, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 30, 171, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 70, 62, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 64, 171, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 91, 31))
        self.pushButton.setStyleSheet("font: 10pt \"Monospace\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.send_file)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 114, 83, 31))
        self.pushButton_2.setStyleSheet("font: 10pt \"Monospace\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.recv_file)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 170, 291, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(340, 170, 281, 261))
        self.textBrowser_2.setObjectName("textBrowser_2")
        QuickLink.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QuickLink)
        self.statusbar.setObjectName("statusbar")
        QuickLink.setStatusBar(self.statusbar)

        self.retranslateUi(QuickLink)
        QtCore.QMetaObject.connectSlotsByName(QuickLink)

    def retranslateUi(self, QuickLink):
        _translate = QtCore.QCoreApplication.translate
        QuickLink.setWindowTitle(_translate("QuickLink", "QuickLink"))
        self.label.setText(_translate("QuickLink", "SEND FILE"))
        self.label_2.setText(_translate("QuickLink", "RECIEVE FILE"))
        self.label_3.setText(_translate("QuickLink", "FILENAME:"))
        self.label_4.setText(_translate("QuickLink", "FILEPATH:"))
        self.label_5.setText(_translate("QuickLink", "HOST :"))
        self.label_6.setText(_translate("QuickLink", "PORT:"))
        self.pushButton.setText(_translate("QuickLink", "SEND"))
        self.pushButton_2.setText(_translate("QuickLink", "RECIEVE"))
        self.textBrowser.setHtml(_translate("QuickLink", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># To use the send file functionality:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1 -&gt; Enter Filename and Filepath in respective fields.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2 -&gt; Press Send { It will start a small server on your machine from which</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                  the reciever can get the required file }</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3 -&gt; GOTO terminal and enter \'ip a\' to get your public ip ( not 127.0.0.1).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            Send this Ip to the reciever.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># NOTE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> 1 -&gt; In file path exclude filename</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> 2 -&gt; PORT IS 8080</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("QuickLink", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># To use recieve functionality</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1 -&gt; OBTAIN IP and PORT from the sender</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2 -&gt; ENTER IP AND PORT</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3 -&gt; PRESS RECIEVE BUTTON</p></body></html>"))
