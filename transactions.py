import cx_Oracle
import dbcontroller as dbc

db = dbc.OracleDb("ANONYMOUS","password","localhost:1521/xe")  
                
class Memento():
    def __init__(self, sendingCardNum, recievingCardNum, money, t_type):
        self.__sendingCardNum = sendingCardNum
        self.__recievingCardNum = recievingCardNum
        self.__money = money
        self.__t_type = t_type
        
    def GetSCN(self):
        return self.__sendingCardNum
    def GetRCN(self):
        return self.__recievingCardNum
    def GetMoney(self):
        return self.__money
    def GetType(self):
        return self.__t_type

    
class Transaction():
    def __init__(self, sendingCardNum, recievingCardNum, money, t_type):
        self.__sendingCardNum = sendingCardNum
        self.__recievingCardNum = recievingCardNum
        self.__money = money
        self.__t_type = t_type


    def SetMemento(self, mem):
        self.__sendingCardNum = mem.GetSCN()
        self.__recievingCardNum = mem.GetRCN()
        self.__money = mem.GetMoney()
        self.__t_type = mem.GetType()
    def CreateMemento(self):
        return Memento(self.__sendingCardNum, self.__recievingCardNum, self.__money, self.__t_type)
        
    
    def Execute(self):
        if self.__t_type == "CTC":
            done = db.execute('''
                      update BANKCARDS 
                      set balance = balance - :balance
                      where num = :card_number''',
                      balance = self.__money,
                      card_number = self.__sendingCardNum
                    )
            if done :
                db.execute('''
                          update BANKCARDS 
                          set balance = balance + :balance
                          where num = :card_number''',
                          balance = self.__money,
                          card_number = self.__recievingCardNum
                        )
            
            
                
        elif self.__t_type == "ATC":
            db.execute('''
                update BANKCARDS 
                set balance = :balance
                where num = :card_number''',
                balance=self.__money,
                card_number=self.__recievingCardNum
            )
        elif self.__t_type == "CTA":
            
            db.execute('''
                        update BANKCARDS 
                        set balance = balance - :balance
                        where num = :card_number''',
                        balance = self.__money,
                        card_number = self.__sendingCardNum
                    )
        db.SaveTransaction(self.CreateMemento())
                

class VirtualATM():

    def SendMoney(self,CardNum, cash):
        tr = Transaction("",CardNum, cash,"ATC").Execute()    
    

    def WithdrawMoney(self, CardNum, cash):
        tr = Transaction(CardNum, "", cash,"CTA").Execute()  
