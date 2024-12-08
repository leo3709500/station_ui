from PyQt5 import QtWidgets
from main_window import Ui_MainWindow as MainWindowUI
from login_window import Ui_MainWindow as LoginWindowUI
from manage_window import Ui_MainWindow as ManageWindowUI
from add import Ui_MainWindow as AddWindowUI
from user_find import Ui_MainWindow as UserFindWindowUI
from add_vehicle import Ui_MainWindow as AddVehicleUI
from add_violation import Ui_MainWindow as AddViolationUI
from question import Ui_MainWindow as QuestionUI
from other import Ui_MainWindow as OtherUI

class MainController:
    def __init__(self):
        # 初始化應用程式
        self.app = QtWidgets.QApplication([])
        self.main_window = QtWidgets.QMainWindow()
        self.stacked_widget = QtWidgets.QStackedWidget()

        # 初始化各個UI
        self.ui_main = MainWindowUI()
        self.ui_login = LoginWindowUI()
        self.ui_manage = ManageWindowUI()
        self.ui_add = AddWindowUI()
        self.ui_user_find = UserFindWindowUI()
        self.ui_add_vehicle = AddVehicleUI()
        self.ui_add_violation = AddViolationUI()
        self.ui_question = QuestionUI()
        self.ui_other = OtherUI()

        # 初始化各個視窗
        self.main_widget = QtWidgets.QMainWindow()
        self.login_widget = QtWidgets.QMainWindow()
        self.manage_widget = QtWidgets.QMainWindow()
        self.add_widget = QtWidgets.QMainWindow()
        self.user_find_widget = QtWidgets.QMainWindow()
        self.add_vehicle_widget = QtWidgets.QMainWindow()
        self.add_violation_widget = QtWidgets.QMainWindow()
        self.question_widget = QtWidgets.QMainWindow()
        self.other_widget = QtWidgets.QMainWindow()

        # 設定UI到各個視窗
        self.ui_main.setupUi(self.main_widget)
        self.ui_login.setupUi(self.login_widget)
        self.ui_manage.setupUi(self.manage_widget)
        self.ui_add.setupUi(self.add_widget)
        self.ui_user_find.setupUi(self.user_find_widget)
        self.ui_add_vehicle.setupUi(self.add_vehicle_widget)
        self.ui_add_violation.setupUi(self.add_violation_widget)
        self.ui_question.setupUi(self.question_widget)
        self.ui_other.setupUi(self.other_widget)

        # 將視窗加入堆疊小部件
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.manage_widget)
        self.stacked_widget.addWidget(self.add_widget)
        self.stacked_widget.addWidget(self.user_find_widget)
        self.stacked_widget.addWidget(self.add_vehicle_widget)
        self.stacked_widget.addWidget(self.add_violation_widget)
        self.stacked_widget.addWidget(self.question_widget)
        self.stacked_widget.addWidget(self.other_widget)

        # 設定主視窗的中央小部件
        self.main_window.setCentralWidget(self.stacked_widget)

        # 設定主視窗大小
        self.main_window.resize(800, 600)

        # 設定按鈕連接
        self.setup_connections()

    def setup_connections(self):
        # 設定按鈕點擊事件，切換不同的視窗
        self.ui_main.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.login_widget))
        self.ui_main.pushButton_2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.user_find_widget))
        self.ui_main.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.question_widget))
        self.ui_main.pushButton_6.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.other_widget))
        self.ui_login.pushButton.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))
        self.ui_manage.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_widget))
        
        self.ui_login.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        self.ui_user_find.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        
        self.ui_add.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))
        
        self.ui_manage.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        
        self.ui_manage.pushButton_7.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_vehicle_widget))
        
        self.ui_manage.pushButton_8.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_violation_widget))

        self.ui_add_violation.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))
        
        self.ui_add_vehicle.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))
        
        self.ui_question.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        self.ui_other.pushButton_6.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))

    def show_main_window(self):
        # 顯示主視窗
        self.main_window.show()

    def run(self):
        # 執行應用程式
        self.show_main_window()
        self.app.exec_()

if __name__ == "__main__":
    # 創建控制器並運行
    controller = MainController()
    controller.run() 