# -'- utf-8: -'-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QFont

#from oop import AccountManagerInterface, Registration
from uis.main_ui import Ui_MainWindow
from uis.too_buttons_settings import adjust_tool_buttons

import dbcontroller as dbc
db = dbc.OracleDb("ANONYMOUS","password","localhost:1521/xe")  
import acc_manager as acc
import os

ac = acc.Account(0,0)

u_id = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None, *args, **kwargs):

        f = open("temp.txt", "r")
        u_id = f.read()
        f.close()
        os.remove("temp.txt")
        ac.current_user_id = u_id
        cards = db.execute_return(''' select num from main_cards_info where u_id = :uu_id''', uu_id = u_id)
        for row in cards:
            ac.card_numbers.append(row[0])
                   
        QMainWindow.__init__(self)
        self.setupUi(self)
        adjust_tool_buttons(self=self)
        self.pushButton_add_card.clicked.connect(self.add_card_number_click)
        self.pushButton_set_card.clicked.connect(self.select_card_number_click)
        self.toolButton_refresh.clicked.connect(self.refresh_card_list_click)
        self.pushButton_top_up_card.clicked.connect(self.top_up_cardClick)
        self.pushButton_trans.clicked.connect(self.card_transClick)

    
    def toolButton_page_cardClick(self):
        self.stackedWidget.setCurrentIndex(0)

    def toolButton_page_add_cardClick(self):
        self.stackedWidget.setCurrentIndex(1)

    def toolButton_page_top_up_Click(self):
        self.stackedWidget.setCurrentIndex(2)

    def toolButton_page_2_transactionClick(self):
        self.stackedWidget.setCurrentIndex(3)

    def add_card_number_click(self):
        ac.AddCard()
        self.refresh_card_list_click()

    def top_up_cardClick(self):      #ПОПОЛНЕНИЕ КАРТЫ
        self.stackedWidget.setCurrentIndex(0)

    def card_transClick(self):        #ПЕРЕВЕСТИ ДЕНЬГИ
        self.stackedWidget.setCurrentIndex(0)




    """
    def delete_card_number_click(self):
        delete_card_num = self.listWidget.currentRow()
        self.listWidget.takeItem(delete_card_num)
    """

    def select_card_number_click(self):
        select_card_num = self.listWidget.currentItem().text()
        self.lcdNumber_2.display(select_card_num)

        
    def refresh_card_list_click(self):
        self.listWidget.clear()
        for card in ac.card_numbers:
            self.lcdNumber_2.display(card)
            card_num_widget1 = QtGui.QListWidgetItem()
            card_num_widget1.setText(card)
            self.listWidget.addItem(card_num_widget1)


def main():
    
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    








"""
def adjust_tool_buttons(self=None):
    # Кнопка перехода на виджет настройки рабочего пространства
    self.toolButton_card.clicked.connect(self.toolButton_page_cardClick)

    self.toolButton_add_card.clicked.connect(self.toolButton_page_add_cardClick)

    self.toolButton_top_up.clicked.connect(self.toolButton_page_top_up_cardClick)

    self.toolButton_transation.clicked.connect(self.toolButton_page_2_transactionClick)

"""
