import mysql.connector
from mysql.connector import Error
from ClusterLogger import ClusterLogger
from TxtBundler import TxtBundler
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
                ClusterLogger(2, TxtBundler().getString(59), str(ex), "")
                pass
    def Insert(self,query):
        try:
            self.cursor.execute(query)
            self.Commit()
        except mysql.connector.errors.ProgrammingError:
            pass

    def Commit(self):
        try:
            self.conn.commit()
        except mysql.connector.Error as ex:
            ClusterLogger(2, TxtBundler().getString(59), str(ex), "")
        finally:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()