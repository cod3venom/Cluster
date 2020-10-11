import mysql.connector
from mysql.connector import Error
class Stmt:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",database="Cortex",user="root",password="")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cursor.close()


    def InsertDict(self,query,stack):
        if query is not None:
            try:
                self.cursor.execute(query, stack.keys(), stack.values())
                self.Commit()
            except mysql.connector.errors.DataError as ex:
                print(str(ex))
                pass
    def Insert(self,query):
        self.cursor.execute(query)
        self.Commit()

    def Commit(self):
        try:
            self.conn.commit()
        except mysql.connector.Error as err:
            print(str(err))
        finally:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()