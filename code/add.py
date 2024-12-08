# -*- coding: utf-8 -*-

# 這個檔案是由 PyQt5 UI 代碼生成器生成的，從 'C:\DBMS\ui\add.ui' 讀取
# 警告：任何手動更改都會在重新運行 pyuic5 時丟失。除非您知道自己在做什麼，否則不要編輯此文件。

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設置主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        
        # 創建中央小部件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設置輸入欄位的網格佈局
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 80, 431, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 姓名標籤
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 電話輸入欄位
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        
        # 電話標籤
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        
        # 地址標籤
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        
        # 身分證字號標籤
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        # 出生年月日標籤
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        
        # 姓名輸入欄位
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        
        # 身分證字號輸入欄位
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        
        # 地址輸入欄位
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        
        # 信箱標籤
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        
        # 信箱輸入欄位
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        
        # 出生年月日輸入欄位
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 1, 1, 1)
        
        # 設置按鈕的水平佈局
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 420, 431, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # 新增按鈕
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        # 清除按鈕
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        # 上一頁按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        # 設置主視窗的中央小部件
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 設置菜單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 設置狀態欄
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 重新翻譯 UI 元素
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 設置清除按鈕的功能
        self.pushButton_2.clicked.connect(self.clear_fields)

    def clear_fields(self):
        # 清除所有輸入欄位的內容
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())

    def retranslateUi(self, MainWindow):
        # 設置 UI 元素的文字
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_5.setText(_translate("MainWindow", "電話："))
        self.label_4.setText(_translate("MainWindow", "地址："))
        self.label_2.setText(_translate("MainWindow", "身分證字號："))
        self.label_6.setText(_translate("MainWindow", "出生年月日："))
        self.label_7.setText(_translate("MainWindow", "信箱："))
        self.pushButton.setText(_translate("MainWindow", "新增"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "上一頁"))

if __name__ == "__main__":
    import sys
    # 創建應用程序對象
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 進入應用程序的主循環
    sys.exit(app.exec_())
