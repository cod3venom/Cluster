from DataAccess.Stmt import Stmt
from Strings import Strings
from ClusterLogger import ClusterLogger
from TxtBundler import TxtBundler
from Logos import Logos
import  threading

class PGP_AWS:
    second = {}
    def __init__(self):
        self.keywords = AWSKeywords()
        self.end = False
        self.str = Strings()
        self.single_query = ''
        self.stacked_query = ''
        self.vendor = "PGP"
        self.HASHID = self.str.md5ID("random")
        self.brand = Logos()


    def DictToDb(self,query,dict):
        self.stmt.InsertDict(query,dict)

    def QueToDb(self,query):
        Stmt().Insert(query)
        ClusterLogger(1,TxtBundler().getString(56), query,self.vendor )


    def Segregate(self,serialized:dict) ->int:

        try:
            if serialized!=None and serialized!="":
                self.end = False
                ClusterLogger(1,TxtBundler().getString(55), "{} = {}".format(serialized[0], str(serialized[1]).replace(r"\n","")),self.vendor)
                self.keywords.SINGLE_DATA["HASHID"] = self.HASHID
                if serialized[0] == self.keywords.LINK:
                    self.keywords.SINGLE_DATA[self.keywords.LINK] = self.str.DeepCleaning(serialized[1])
                if serialized[0] == self.keywords.TITLE:
                    self.keywords.SINGLE_DATA[self.keywords.TITLE] = self.str.DeepCleaning(serialized[1])
                elif serialized[0] == self.keywords.SELLER:
                    self.keywords.SINGLE_DATA[self.keywords.SELLER] = self.str.DeepCleaning(serialized[1])
                elif serialized[0] == self.keywords.SELLER_LINK:
                    self.keywords.SINGLE_DATA[self.keywords.SELLER_LINK] = self.str.DeepCleaning(serialized[1])
                elif serialized[0] == self.keywords.OFFER_PRICE:
                    self.keywords.SINGLE_DATA[self.keywords.OFFER_PRICE] = self.str.DeepCleaning(serialized[1])


                elif serialized[0] == self.keywords.OFFER_DELIVERY_INFO:
                    self.keywords.SINGLE_DATA[self.keywords.OFFER_DELIVERY_INFO] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.OFFER_SHORT_DESCRIPTION:
                    self.keywords.SINGLE_DATA[self.keywords.OFFER_SHORT_DESCRIPTION] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_BRAND:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_BRAND] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_MODEL_NUMBER:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_MODEL_NUMBER] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_COLOUR:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_COLOUR] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_DIMENSIONS:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_DIMENSIONS] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_MATERIAL:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_MATERIAL] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_WEIGHT:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_WEIGHT] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_ASIN:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_ASIN] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_RATINGS:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_RATINGS] = self.str.DeepCleaning(serialized[1])

                elif serialized[0] == self.keywords.PRODUCT_BEST_SELLERS_RANK:
                    self.keywords.SINGLE_DATA[self.keywords.PRODUCT_BEST_SELLERS_RANK] = self.str.DeepCleaning(serialized[1])



        except IndexError:
            pass
        finally:
            if serialized==None and self.keywords.SINGLE_DATA[self.keywords.TITLE] != "":
                self.finalize()

    """
        INSERT INTO DATABASE DICT TYPE DATA
    """
    def STACKED_INSERT(self, stack,table,col1,col2):
        if stack!=None and len(stack) > 0:
            try:
                stack = str(stack).replace("'",",").replace(",,",",")
                if "," in stack:
                    stacked = stack.split(",")
                    for pointer in stacked:
                        if len(pointer) > 10:
                            self.stacked_query = AWSQuery().StackedLinksQuery(table,col1,col2,self.HASHID,pointer)
                            self.QueToDb(self.stacked_query)
            except IndexError:
                pass


    def PriceInsert(self,pack,table,col1,col2):
        if pack != None and "'" in pack:
            pack = str(pack).replace("'",",").replace(", ,",",")
            if pack != '' and pack!=',':
                pack = pack.split(",")
                for packet in pack:
                    if packet != "":
                        self.keywords.CUSTOMER_WHO_REVIEWED_PRICE_QUERY = AWSQuery().StackedLinksQuery(table,col1,col2,self.HASHID, packet)
                        self.QueToDb(self.keywords.CUSTOMER_WHO_REVIEWED_PRICE_QUERY)

    def RatingInsert(self, pack, table,col1,col2):
        if pack != None and table != "" and col1 != "" and col2 != "":
            if "'" in pack:
                pack = str(pack).replace("'",",").replace(",,",",").replace(pack[:1],"")
                pack = pack.split(",")
                for rating in pack:
                    if rating !="":
                        self.keywords.CUSTOMER_WHO_REVIEWED_RATING_QUERY = AWSQuery().StackedLinksQuery(table,col1,col2,self.HASHID, rating)
                        self.QueToDb(self.keywords.CUSTOMER_WHO_REVIEWED_RATING_QUERY)

    def finalize(self):
        self.end = True
        self.single_query = AWSQuery().dictToSql(self.keywords.SINGLE_DATA)
        self.QueToDb(self.single_query)
        self.UpdateHash()

    """
        UPDATE FULL OFFER IDENTIFICATION HASH
    """
    def UpdateHash(self):
        self.HASHID = self.str.md5ID("random")

class AWSQuery:
    """
     THIS FUNCTION IS USED TO CONVERT
     DICTIONARY TYPE DATA INTO MYSQL QUERY
    """
    def dictToSql(self,serialized):
        table='AWS_PGP_OFFERS'
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in serialized.keys())
        values = ', '.join('"' + str(x).replace('/', '_') + '"' for x in serialized.values())
        return "INSERT INTO %s ( %s ) " \
               "VALUES " \
               "( %s );" % (table, columns, values)

    def StackedLinksQuery(self,table,col1,col2,param1,param2):
        data = 'INSERT INTO {} (`{}`,`{}`) VALUES ("{}","{}");'.format(table,col1,col2,param1,param2)
        return data



class AWSKeywords:
    HASHID ="HASHID"
    LINK ="LINK"
    TITLE="TITLE"
    SELLER="SELLER"
    SELLER_LINK="SELLER_LINK"
    OFFER_PRICE="OFFER_PRICE"
    OFFER_DELIVERY_INFO="OFFER_DELIVERY_INFO"
    OFFER_SHORT_DESCRIPTION="OFFER_SHORT_DESCRIPTION"
    PRODUCT_BRAND = "PRODUCT_BRAND"
    PRODUCT_MODEL_NUMBER = "PRODUCT_MODEL_NUMBER"
    PRODUCT_COLOUR = "PRODUCT_COLOUR"
    PRODUCT_DIMENSIONS = "PRODUCT_DIMENSIONS"
    PRODUCT_MATERIAL = "PRODUCT_MATERIAL"
    PRODUCT_WEIGHT="PRODUCT_WEIGHT"
    PRODUCT_ASIN="PRODUCT_ASIN"
    PRODUCT_RATINGS="PRODUCT_RATINGS"
    PRODUCT_BEST_SELLERS_RANK="PRODUCT_BEST_SELLERS_RANK"

    SINGLE_DATA = {

    }
