class Card:
    def __init__(self, number, balance):
        self.__number = number
  
        self.__balance = balance

    def SetBalance(self, balance):
        self.__balance = balance

    def GetNumber(self):
        return self.__number

    def GetBalance(self):
        return self.__balance
