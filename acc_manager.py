import dbcontroller as dbc
import random

db = dbc.OracleDb("ANONYMOUS","password","localhost:1521/xe")

class AccountManagerInterface:
    def SignUp(self,log,pas):
        pass

    def SignIn(self, psevdoBD, u_id, u_pass):
        pass

    def SignOut(self):
        pass


class Account(AccountManagerInterface):
    def __init__(self, current_user_id, card_numbers):
        self.current_user_id = current_user_id
        self.card_numbers = []

    def SignIn(self,selfuser_log, user_password): 
        info = db.execute_return('''select U_ID, U_PASS from ACCOUNTS_INFO where U_LOGIN = :login''',login = selfuser_log)
        if info != []:
            u_id = info[0][0]
            pss = info[0][1]
            if user_password   == pss:
                self.current_user_id = u_id
                cards = db.execute_return(''' select num from main_cards_info where u_id = :u_id''', u_id = u_id)
                for row in cards:
                    self.card_numbers.append(row[0])
                return 1
            else:
                return 0
        else:
            return 0
                
    def SignOut(self):
        self.current_user_id = 0
        self.card_numbers = []

    def AddCard(self):
        month = db.execute_return('''select CAST(to_char(sysdate, 'MM') as int) from dual ''')[0][0]
        year =4 + db.execute_return('''select CAST(to_char(sysdate, 'YYYY') as int) from dual ''')[0][0]
        
        num = str(int(db.execute_return('''select max(num) from bankcards ''')[0][0]) + 1)
        num = (16-len(num))*"0" + num
        db.execute(''' insert into bankcards(NUM, CVV, MONTH, YEAR, BALANCE, USER_ID)
                        values (:NUM, :CVV, :mon, :year, 0, :USER_ID)''',
                       NUM = num, CVV =  random.randint(1,1000),USER_ID = self.current_user_id, mon = month,year = year)
        self.card_numbers.append(num)
class Registration(AccountManagerInterface):

    def SignUp(self,u_login,u_password,name,secname):
        
        month = db.execute_return('''select CAST(to_char(sysdate, 'MM') as int) from dual ''')[0][0]
        year =4 + db.execute_return('''select CAST(to_char(sysdate, 'YYYY') as int) from dual ''')[0][0]
        u_login = u_login.strip()
        u_password = u_password.strip()
        name = name.strip()
        secname = secname.strip()
        
        if len(name) < 6 and len(u_login) > 31:
            print(" Ошибка длины пароля")
            return 0
        elif len(secname) < 6 and len(u_login) > 31:
            print(" Ошибка длины пароля")
            return 0
        elif len(u_password) < 6 and len(u_login) > 21:
            print(" Ошибка длины пароля")
            return 0
        elif len(u_login) < 3 and len(u_login) > 17:
            print(" Ошибка длины логина")    
            return 0
        elif db.execute_return(""" select * from accounts_info where u_login = :login """, login = u_login) != []:
            print("логин занят")
            return 0
        else:
            print ("okey")
            num = str(int(db.execute_return('''select max(num) from bankcards ''')[0][0]) + 1)
            num = (16-len(num))*"0" + num
            db.execute(''' insert into accounts_info(U_NAME, U_SECONDNAME, U_LOGIN, U_PASS)
                            values (:U_NAME, :U_SECONDNAME, :U_LOGIN, :U_PASS)'''
                       ,U_NAME = name, U_SECONDNAME = secname, U_LOGIN = u_login, U_PASS = u_password)
            u_id = db.execute_return('''select max(u_id) from accounts_info ''')[0][0]
            db.execute(''' insert into bankcards(NUM, CVV, MONTH, YEAR, BALANCE, USER_ID)
                        values (:NUM, :CVV, :mon, :year, 0, :USER_ID)''',
                       NUM = num, CVV =  random.randint(1,1000),USER_ID = u_id, mon = month, year = year)
            return 1




