import sys
from sympy import *


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


zn = '+-=></*\n},'
cfr = '0123456789.'


def preobr(a):
    a = a.replace(' ', '')
    a = a.replace('^', '**')
    a = a.replace('log', ' - - - - - - - - -')
    a = a.replace('asin', ' - - - - - - - -')
    a = a.replace('acos', ' - - - - - - -')
    a = a.replace('atag', ' - - - - - -')
    a = a.replace('acot', ' - - - - -')
    a = a.replace('sin', ' - - - -')
    a = a.replace('cos', ' - - -')
    a = a.replace('tan', ' - -')
    a = a.replace('cot', ' -')
    a = a.replace('×', '*')
    s = 0
    i = 0
    while i < len(a):
        if a[i] == '√':
            k = '**(1/2)'
            if i != 0 and a[i - 1] == '}':
                g = i - 2
                h = 1
                while h != 0:
                    if a[g] == '}':
                        h += 1
                    elif a[g] == '{':
                        h -= 1
                    g -= 1
                k = '**(1/(' + a[g + 2:i - 1] + '))'
                a = a[:g + 1] + a[i + 1:]
                i -= len(k) - 6
            else:
                a = a[:i] + a[i + 1:]
            if a[i] == '(':
                g = i + 1
                h = 1
                while h != 0:
                    if a[g] == '(':
                        h += 1
                    elif a[g] == ')':
                        h -= 1
                    g += 1
            else:
                g = i + 1
                while a[g] in cfr and a[i] in cfr + '-':
                    g += 1
            a = a[:g] + k + a[g:]
        i += 1
    for j in range(len(a)):
        i = j + s
        if a[i] == "'" and a[i - 1] != ')':
            g = i
            while a[g] not in zn:
                g -= 1
            a = a[:g + 1] + 'diff(' + a[g + 1:i] + ')' + a[i + 1:]
            s += 5
        elif a[i] == "'" and a[i - 1] == ')':
            g = i - 2
            h = 1
            while h != 0:
                if a[g] == ')':
                    h += 1
                elif a[g] == '(':
                    h -= 1
                g -= 1
            a = a[:g + 1] + 'diff' + a[g + 1:i] + a[i + 1:]
            s += 3
        if (i + 1 != len(a) and a[i] not in zn + '({' and
        a[i + 1] not in zn + ")'" and (a[i] not in cfr or a[i + 1] not in cfr)):
            a = a[:i + 1] + '*' + a[i + 1:]
            s += 1
    a = a.replace(' - - - - - - - - -', 'log')
    a = a.replace(' - - - - - - - -', 'asin')
    a = a.replace(' - - - - - - -', 'acos')
    a = a.replace(' - - - - - -', 'atan')
    a = a.replace(' - - - - -', 'acot')
    a = a.replace(' - - - -', 'sin')
    a = a.replace(' - - -', 'cos')
    a = a.replace(' - -', 'tan')
    a = a.replace(' -', 'cot')
    a = a.replace('π', 'pi')
    return a


class MyWidget(QMainWindow):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(497, 629)
        mainWindow.setMinimumSize(QtCore.QSize(497, 629))
        mainWindow.setMaximumSize(QtCore.QSize(497, 629))
        font = QtGui.QFont()
        font.setPointSize(8)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 497, 161))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 159, 497, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.plainTextEdit_2.setAcceptDrops(True)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(-1, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(-1, 361, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(-1, 423, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(-1, 485, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(-1, 547, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 98, 101);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(185, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(371, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(61, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.buttonGroup.addButton(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(123, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.buttonGroup.addButton(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(247, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.buttonGroup.addButton(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(309, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.buttonGroup.addButton(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(433, 299, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.buttonGroup.addButton(self.pushButton_12)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(61, 361, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.buttonGroup.addButton(self.pushButton_14)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(185, 423, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.buttonGroup.addButton(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(249, 363, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.buttonGroup.addButton(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(61, 423, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.buttonGroup.addButton(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(61, 485, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.buttonGroup.addButton(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(311, 363, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.buttonGroup.addButton(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(373, 363, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.buttonGroup.addButton(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(185, 361, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.buttonGroup.addButton(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(123, 361, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.buttonGroup.addButton(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(61, 547, 65, 66))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.buttonGroup.addButton(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(123, 423, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.buttonGroup.addButton(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(433, 361, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.buttonGroup.addButton(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(249, 425, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_27.setObjectName("pushButton_27")
        self.buttonGroup.addButton(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(311, 425, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.buttonGroup.addButton(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(373, 425, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_29.setObjectName("pushButton_29")
        self.buttonGroup.addButton(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(433, 423, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.buttonGroup.addButton(self.pushButton_30)
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(123, 485, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_32")
        self.buttonGroup.addButton(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(185, 485, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setObjectName("pushButton_33")
        self.buttonGroup.addButton(self.pushButton_33)
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(249, 487, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_34.setObjectName("pushButton_34")
        self.buttonGroup.addButton(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(311, 487, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_35.setObjectName("pushButton_35")
        self.buttonGroup.addButton(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(373, 487, 63, 63))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_36.setObjectName("pushButton_36")
        self.buttonGroup.addButton(self.pushButton_36)
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(433, 485, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setObjectName("pushButton_37")
        self.buttonGroup.addButton(self.pushButton_37)
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(123, 547, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.buttonGroup.addButton(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(185, 547, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setObjectName("pushButton_40")
        self.buttonGroup.addButton(self.pushButton_40)
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(247, 547, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setObjectName("pushButton_41")
        self.buttonGroup.addButton(self.pushButton_41)
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(311, 549, 63, 64))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_42.setObjectName("pushButton_42")
        self.buttonGroup.addButton(self.pushButton_42)
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(373, 549, 125, 64))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(30)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(96, 160, 255);")
        self.pushButton_43.setObjectName("pushButton_43")
        self.buttonGroup.addButton(self.pushButton_43)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Калькулятор"))
        self.pushButton.setText(_translate("mainWindow", "sin(x)"))
        self.pushButton_2.setText(_translate("mainWindow", "cos(x)"))
        self.pushButton_3.setText(_translate("mainWindow", "tan(x)"))
        self.pushButton_4.setText(_translate("mainWindow", "cot(x)"))
        self.pushButton_5.setText(_translate("mainWindow", "DEL"))
        self.pushButton_6.setText(_translate("mainWindow", ")"))
        self.pushButton_7.setText(_translate("mainWindow", "="))
        self.pushButton_8.setText(_translate("mainWindow", "asin(x)"))
        self.pushButton_9.setText(_translate("mainWindow", "("))
        self.pushButton_10.setText(_translate("mainWindow", "<"))
        self.pushButton_11.setText(_translate("mainWindow", ">"))
        self.pushButton_12.setText(_translate("mainWindow", "/"))
        self.pushButton_14.setText(_translate("mainWindow", "acos(x)"))
        self.pushButton_16.setText(_translate("mainWindow", "√x"))
        self.pushButton_17.setText(_translate("mainWindow", "7"))
        self.pushButton_18.setText(_translate("mainWindow", "atan(x)"))
        self.pushButton_19.setText(_translate("mainWindow", "acot(x)"))
        self.pushButton_20.setText(_translate("mainWindow", "8"))
        self.pushButton_21.setText(_translate("mainWindow", "9"))
        self.pushButton_22.setText(_translate("mainWindow", " x²"))
        self.pushButton_23.setText(_translate("mainWindow", "xʸ"))
        self.pushButton_24.setText(_translate("mainWindow", "logᵧ(x)"))
        self.pushButton_25.setText(_translate("mainWindow", "ʸ√x"))
        self.pushButton_26.setText(_translate("mainWindow", "×"))
        self.pushButton_27.setText(_translate("mainWindow", "4"))
        self.pushButton_28.setText(_translate("mainWindow", "5"))
        self.pushButton_29.setText(_translate("mainWindow", "6"))
        self.pushButton_30.setText(_translate("mainWindow", "-"))
        self.pushButton_32.setText(_translate("mainWindow", "x"))
        self.pushButton_33.setText(_translate("mainWindow", "y"))
        self.pushButton_34.setText(_translate("mainWindow", "1"))
        self.pushButton_35.setText(_translate("mainWindow", "2"))
        self.pushButton_36.setText(_translate("mainWindow", "3"))
        self.pushButton_37.setText(_translate("mainWindow", "+"))
        self.pushButton_39.setText(_translate("mainWindow", "{"))
        self.pushButton_40.setText(_translate("mainWindow", "π"))
        self.pushButton_41.setText(_translate("mainWindow", "."))
        self.pushButton_42.setText(_translate("mainWindow", "0"))
        self.pushButton_43.setText(_translate("mainWindow", "↵"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        for i in self.buttonGroup.buttons():
            i.clicked.connect(self.vvod)
        self.pushButton_43.clicked.connect(self.res)
        self.x = 0
        self.y = 0

    def vvod(self):
        a = str(self.sender().text())
        cursor = self.plainTextEdit.textCursor()
        if cursor.blockNumber() != 0 or cursor.positionInBlock() != 0:
            self.y = cursor.blockNumber()
            self.x = cursor.positionInBlock()
        if a != 'y' and a != 'x':
            a = a.replace('y', '')
            a = a.replace('ᵧ', '')
            a = a.replace('x', '')
        if a == ' ²':
            a = '^2'
        if a == 'log()':
            a = 'log((),())'
        if a == '{':
            a = '\n'
        if a == 'ʸ√':
            a = '{}√()'
        if a == 'ʸ':
            a = '^()'
        if a == '√':
            a = '√()'
        if a == '↵':
            a = ''
        if a =='DEL':
            self.plainTextEdit.setPlainText('')
        else:
            b = str(self.plainTextEdit.toPlainText())
            p = 0
            y = self.y
            for i in range(len(b)):
                if b[i] == '\n':
                    y -= 1
                p += 1
                if y == 0:
                    break
            if self.y == 0:
                p -= 1
            b = b[:p + self.x] + a + b[p + self.x:]
            if a == '\n':
                self.y += 1
                self.x = 0
            else:
                self.x += len(a)
            self.plainTextEdit.setPlainText(b)


    def res(self):
        a = self.plainTextEdit.toPlainText()
        if len(a) != 0:
            try:
                a = preobr(a).split('\n')
                if len(a) == 1 and '=' not in a[0] and '>' not in a[0] and '<' not in a[0]:
                    a = expand(simplify(a[0]))
                    self.plainTextEdit_2.setPlainText(pretty(a).replace('⋅', '×'))
                else:
                    for i in range(len(a)):
                        if a[i].count('=') == 1 and a[i].count('>') == 0 and a[i].count('<') == 0:
                            a[i] = simplify(a[i].replace('=', '-(') + ')')
                        else:
                            a[i] = simplify(a[i])
                    else:
                        t = True
                        a = solve(a, set=True)
                        if type(a) == tuple and len(a) != 0:
                            a = (a[0], list(a[1]))
                            i = 0
                            while i < len(a[1]):
                                if 'I' in str(a[1][i]):
                                    del a[1][i]
                                    i -= 1
                                i += 1
                            if len(a[0]) == 1:
                                a = (a[0][0], a[1])
                            if len(a[1]) == 1:
                                a = (a[0], list(a[1])[0])
                            elif len(list(a[1])[0]) == 1:
                                a = (a[0], list(a[1]))
                                for i in range(len(a[1])):
                                    a[1][i] = list(a[1][i])[0]
                                a = (a[0], set(a[1]))
                            if len(a[1]) == 1:
                                a = (a[0], list(a[1])[0])
                        if a != [] and t:
                            self.plainTextEdit_2.setPlainText((pretty(a)).replace('⋅', '×'))
                        else:
                            self.plainTextEdit_2.setPlainText('')
            except Exception:
                print(a)
                self.plainTextEdit_2.setPlainText('НЕКОРЕКТНЫЙ ВВОД')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())