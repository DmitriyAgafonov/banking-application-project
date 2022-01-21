import cx_Oracle
import card

class OracleDb:
    def __init__(self, username, password, db_name):
        self.__user = username
        self.__password = password
        self.__db_name = db_name

    @property
    def _connection(self):
        try:
          return cx_Oracle.connect(self.__user, self.__password, self.__db_name)
        except cx_Oracle.DatabaseError as e:
          self.__handle_exception(e)

    def execute(self, command, **params):
        with self._connection as con:
            try:
                with con.cursor() as cur:
                      cur.execute(command, **params)
            except cx_Oracle.DatabaseError as e:
                return self.__handle_exception(e)
            else:
                con.commit()
                return 1
            
    def execute_return(self, command, **params):
        res = []
        with self._connection as con:
            try:
                with con.cursor() as cur:
                      cur.execute(command, **params)
                      for row in cur:
                          res.append(row)        
            except cx_Oracle.DatabaseError as e:
                self.__handle_exception(e)
            else:
                con.commit()
                return res
            
    def __handle_exception(self, e):
        print(e)
        return 0


    def GetCardInfo(self, numb):
        card_info = []
        with self._connection as con:
            try:
                with con.cursor() as cur:
                    cur.execute('''
                            select num, balance
                            from bankcards
                            where num = :num             

                        ''',
                        num = numb
                        )
                    for row in cur:
                        card_info.append(row[0])
                        card_info.append(row[1])
                    
            except cx_Oracle.DatabaseError as e:
                self.__handle_exception(e)
            else:
                con.commit()
                return card_info


    def SaveTransaction(self, mem):
        with cx_Oracle.connect("ANONYMOUS","password","localhost:1521/xe") as con:
            try:
                with con.cursor() as cur:
                    cur.execute('''
                      INSERT INTO TRANSATIONHISTORY(SENDNUM,RECNUM, MONEY, TYPE,DATE_TIME)
                      VALUES (:send,:rec, :mon, :tpe,sysdate)''',
                      send = mem.GetSCN(),
                      rec = mem.GetRCN(),
                      mon = mem.GetMoney(),
                      tpe = mem.GetType()
                    )
            except:
                print("Smth went wrong")
            else:
                con.commit()

    
    

