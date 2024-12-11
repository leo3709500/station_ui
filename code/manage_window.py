# -*- coding: utf-8 -*-

# 由 PyQt5 UI 代碼生成器 5.15.10 從 'C:\DBMS\ui\manage_window.ui' 讀取的表單實現
#
# 警告：此文件的任何手動更改將在再次運行 pyuic5 時丟失。除非您知道自己在做什麼，否則不要編輯此文件。

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設定主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 612)
        
        # 設定中央小工具
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設定佈局小工具
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 751, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        
        # 設定水平佈局
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # 設定各個按鈕
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        
        # 設定網格佈局小工具
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 90, 551, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        # 設定網格佈局
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 設定下拉選單
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 0, 3, 1, 1)
        
        # 設定標籤
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 5, 1, 1)
        
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 設定標題標籤
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        # 設定表格視圖
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 190, 751, 381))
        self.tableView.setObjectName("tableView")
        
        # 設定主視窗的中央小工具、選單欄和狀態欄
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 重新翻譯 UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 設定翻譯
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "刪除"))
        self.pushButton_3.setText(_translate("MainWindow", "查詢"))
        self.pushButton_4.setText(_translate("MainWindow", "新增使用者"))
        self.pushButton_7.setText(_translate("MainWindow", "新增車輛"))
        self.pushButton_8.setText(_translate("MainWindow", "新增違規狀態"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_5.setText(_translate("MainWindow", "返回主畫面"))
        self.comboBox.setItemText(0, _translate("MainWindow", "所有車種"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SUV"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Coupe"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Truck"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Sedan"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Van"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "所有檢驗項目"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "101"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "102"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "103"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "104"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "105"))
        self.label_2.setText(_translate("MainWindow", "違規項目："))
        self.label_3.setText(_translate("MainWindow", "檢驗項目："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "所有違規"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1001"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1002"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1003"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1004"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "1005"))
        self.label.setText(_translate("MainWindow", "車輛種類："))
        self.label_4.setText(_translate("MainWindow", "管理員查詢系統"))

if __name__ == "__main__":
    import sys
    # 創建應用程序對象
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 執行應用程序的主循環
    sys.exit(app.exec_())
