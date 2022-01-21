import transactions as t




#------------------------------------- транзакции -------------------------------------
atr = t.VirtualATM()
atr.SendMoney('0000000000000001',400)
tr = t.Transaction('0000000000000001','0000000000000002',400,"CTC")
tr.Execute()
atr.WithdrawMoney('0000000000000002',400)


#---------------------- конец транзакций--------------------------------
"""
class EnterAccountInterface:
    def new_or_existing_acc(self):
        pass

class StartApp(EnterAccountInterface):
    def __init__(self, status):
        self.status = status

    def new_or_existing_acc(self):
        print("Welcome to dndBank, We care for you\n")
        self.status = int(input("To open a new bank account, Press 1\n" + "To access your existing account & transact press 2\n"))
        if self.status == 1:
             Registration.account_check()
        #elif self.status == 2:
             #существующий
        else:
            print("You have pressed the wrong key, please try again")
            new_or_existing_acc()
"""


class AccountManagerInterface:
    def SignUp(self, psevdoDB):
        pass

    def SignIn(self, psevdoBD, u_id, u_pass):
        pass

    def SignOut(self):
        pass


class Account(AccountManagerInterface):
    def __init__(self, current_user_id, card_numbers):
        self.current_user_id = current_user_id
        self.card_numbers = card_numbers

    def SignIn(self, psevdoBD, user_id, user_password):
        for user in psevdoBD:
            if user[0] == user_id:
                if user[1] == user_password:
                    self.current_user_id = user_id
                    self.card_numbers = user[2]

    def SignOut(self):
        self.current_user_id = 0
        self.card_numbers = []


class Registration(AccountManagerInterface):

    def generate_cardnum(self):
        pass

    def SingUp(self, psevdoDBA):
        last_id = psevdoDBA[len(psevdoDBA)-1][0] + 1
        account = [last_id]
        while True:
            try:
                upass = input("Enter password: ")
                if len(upass) < 5:
                    raise UpassTooSmallError("Your password is too short, try again")
                else:
                    account.append(upass)
                break
            except UpassTooSmallError as e:
                print("Attention!", e.message)

        while True:
            try:
                card_num = int(input('Enter card number: '))
                if len(str(card_num)) != 16:
                    raise CardNumLengthError("Card number should contain 16 numbers, try again")
                else:
                    account.append([card_num])

                break
            except CardNumLengthError as e:
                print(e.message)
            except ValueError:
                print('Card number should contain only numbers!')
            print(type(card_num))

        return account


def AddCard(psevdoBDA, card_num):
    user = psevdoBDA[len(psevdoBDA)][2][0]
    card = Card(card_num, '713', '12', '21', 25000.65)
    return card

#'------------------------Exceptions---------------------------------')


#class Error(Exception):
    #pass

class UpassTooSmallError(Exception):
    def __init__(self, message):
        self.message = message


class CardNumLengthError(Exception):
    def __init__(self, message):
        self.message = message


#'---------------------------------------------------------')

"""
psevdoBDAcc = []
psevdoBDAcc.append([1, '123', ['0000000000000000', '0000000000000001']])
psevdoBDAcc.append([2, '123', '0000000000000002'])
ac = Account(0, [])

ac.SignIn(psevdoBDAcc, 1, '123')
print(ac.current_user_id)

ac.SignOut()
print(ac.current_user_id)
regFrom = Registration()
psevdoBDAcc.append(regFrom.SingUp(psevdoBDAcc))
print(psevdoBDAcc)






class Account:
    def __init__(self, username, userpassword):
        self.username = username
        self.userpassword = userpassword

    def GetUsername(self):
        return self.username
    def GetUserpassword(self):
        return self.userpassword


class Registration(Account):
    
    def __init__(self, reg_username, reg_userpassword):
        self.reg_username = reg_username
        self.reg_userpassword = reg_userpassword
    

    def account_check(self):
        while self.username not in psevdoBDAccount and len(self.username) < 3:
            if self.username not in psevdoBDAccount:
                psevdoBDUsername.append(Account(self.username))
                break
            else:
                print("Sorry, that user name is already in use")

                
                ans = input("Are you already a member at this bank? (y/n)\n")
                if ans.lower() == 'y':
                    oldcuscheck()
                else:
                    cusaccountcheck()
                

        while len(self.userpassword) < 4:
            if len(self.userpassword) >= 4:
                psevdoBDUserpassword.append(self.userpassword)
                print("your pin has been successfully saved")
                print("Remember to always keep your pin safe and don't disclose it to anybody")

                break

            print("Sorry, that is a short password")

        return username, userpassword



class LogIn(Account):
    def __init__(self, login_username, login_userpassword):
        self.login_username = login_username
        self.login_userpassword = login_userpassword





psevdoBDAccount = []
psevdoBDAccount2 = []
#psevdoBDUsername = []
#psevdoBDUserpassword = []
#--------------------------
psevdoBDAccount.append(Account('qwerty', '12345'))
print(psevdoBDAccount[0].GetUsername(), psevdoBDAccount[0].GetUserpassword())
psevdoBDAccount = Registration(psevdoBDAccount[0].GetUsername(), psevdoBDAccount[0].GetUserpassword())
"""
