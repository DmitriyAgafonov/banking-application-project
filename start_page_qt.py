# -'- utf-8: -'-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QFont
from PyQt4.QtGui import QDialog

from uis.start_page import Ui_MainWindow
from uis.too_buttons_settings import start_page_tool_buttos
import acc_manager as acc
import main_ui_qt as muqt
#from uis.success_dialog import Ui_Dialog

ac = acc.Account(0,0)



class MainWindowStartPage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        start_page_tool_buttos(self=self)
        self.toolButton_reg.clicked.connect(self.toolButton_regClick)
        self.toolButton_enter.clicked.connect(self.toolButton_enterClick)
        self.dialogs = list()

    def toolButton_to_regClick(self):
        self.stackedWidget_start_page.setCurrentIndex(1)

    def toolButton_to_enterClick(self):
        self.stackedWidget_start_page.setCurrentIndex(0)

    def toolButton_regClick(self):
        """
        login_reg = self.reg_login.text()
        login_arr.append(login_reg)
        password_reg = self.reg_pass.text()
        pass_arr.append(password_reg)
        print(login_arr, pass_arr)
        """

        login_reg = self.reg_login.text()
        password_reg = self.reg_pass.text()
        name_reg = self.reg_name.text()
        surname_reg = self.reg_surname.text()

        reg = acc.Registration()
        print(reg.SignUp(login_reg, password_reg, name_reg, surname_reg))



    def toolButton_enterClick(self):

        login_enter = self.enter_login.text()
        password_enter = self.enter_pass.text()
        if ac.SignIn(login_enter, password_enter):
            f=open("temp.txt", "w+")
            u_id = f.write(str(ac.current_user_id))
            f.close() 
            dialog = muqt.MainWindow(self)
            self.dialogs.append(dialog)
            dialog.show()
            
        else:
            print('otsosi')





def main_start_page():
    app = QApplication(sys.argv)
    main = MainWindowStartPage()
    main.show()
    sys.exit(app.exec_())

main_start_page()









