from DataAccess.Stmt import Stmt
from Strings import Strings
from ClusterLogger import ClusterLogger
from TxtBundler import TxtBundler
from Logos import Logos
import  threading

class AWS:
    second = {}
    def __init__(self):
        self.keywords = AWSKeywords()
        self.end = False
        self.str = Strings()
        self.single_query = ''
        self.stacked_query = ''
        self.vendor = "AMAZON"
        self.HASHID = self.str.md5ID("random")
        self.brand = Logos()


    def DictToDb(self,query,dict):
        self.stmt.InsertDict(query,dict)

    def QueToDb(self,query):
        Stmt().Insert(query)
        ClusterLogger(1,TxtBundler().getString(56) + "\r\n\r\n", query,self.vendor )


    def Segregate(self,serialized=None):

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
               elif serialized[0] == self.keywords.OFFER_RATING:
                   self.keywords.SINGLE_DATA[self.keywords.OFFER_RATING] = self.str.DeepCleaning(serialized[1][:4])

               elif serialized[0] == self.keywords.OFFER_PRICE:
                   self.keywords.SINGLE_DATA[self.keywords.OFFER_PRICE] = self.str.DeepCleaning(serialized[1])

               elif serialized[0] == self.keywords.OFFER_SHIPPING_INFO:
                   self.keywords.SINGLE_DATA[self.keywords.OFFER_SHIPPING_INFO] = self.str.DeepCleaning(serialized[1])
               elif serialized[0] == self.keywords.PRODUCT_INFO_TABLE_KEY:
                   self.keywords.SINGLE_DATA[self.keywords.PRODUCT_INFO_TABLE_KEY] = self.str.DeepCleaning(serialized[1])
               elif serialized[0] == self.keywords.PRODUCT_INFO_TABLE_VALUE:
                   self.keywords.SINGLE_DATA[self.keywords.PRODUCT_INFO_TABLE_VALUE] = self.str.DeepCleaning(serialized[1])
               elif serialized[0] == self.keywords.PRODUCT_DESCRIPTION:
                   self.keywords.SINGLE_DATA[self.keywords.PRODUCT_DESCRIPTION] = self.str.DeepCleaning(serialized[1])
               elif serialized[0] == self.keywords.PRODUCT_FROM_MANUFACTURER:
                   self.keywords.SINGLE_DATA[self.keywords.PRODUCT_FROM_MANUFACTURER] = self.str.DeepCleaning(serialized[1])


               elif serialized[0] == self.keywords.CUSTOMERS_WHO_REVIEWED_LINK:
                    self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.CUSTOMERS_WHO_REVIEWED_LINK, self.keywords.HASHID, self.keywords.LINK)

               elif serialized[0] == self.keywords.CUSTOMERS_WHO_REVIEWED_IMAGE:
                    self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.CUSTOMERS_WHO_REVIEWED_IMAGE, self.keywords.HASHID, self.keywords.IMAGE)

               elif serialized[0] == self.keywords.CUSTOMERS_WHO_REVIEWED_TITLE:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.CUSTOMERS_WHO_REVIEWED_TITLE, self.keywords.HASHID, self.keywords.TITLE)

               elif serialized[0] == self.keywords.CUSTOMERS_WHO_REVIEWED_PRICE:
                   self.STACKED_INSERT(serialized[1],self.keywords.CUSTOMERS_WHO_REVIEWED_PRICE, self.keywords.HASHID, self.keywords.PRICE)

               elif serialized[0] == self.keywords.CUSTOMERS_WHO_REVIEWED_STARS:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.CUSTOMERS_WHO_REVIEWED_STARS, self.keywords.HASHID, self.keywords.STARS)

               elif serialized[0] == self.keywords.PRODUCT_REVIEW_USER:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.PRODUCT_REVIEW_USER, self.keywords.HASHID, self.keywords.USERNAME)

               elif serialized[0] == self.keywords.PRODUCT_REVIEW_USER_LINK:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.PRODUCT_REVIEW_USER_LINK, self.keywords.HASHID, self.keywords.Link)

               elif serialized[0] == self.keywords.PRODUCT_REVIEW_USER_AVATAR:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.PRODUCT_REVIEW_USER_AVATAR, self.keywords.HASHID, self.keywords.AVATAR)

               elif serialized[0] == self.keywords.PRODUCT_REVIEW_USER_STARS:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.PRODUCT_REVIEW_USER_STARS, self.keywords.HASHID, self.keywords.STARS)

               elif serialized[0] == self.keywords.PRODUCT_REVIEW_USER_LOCATION_DATE:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.PRODUCT_REVIEW_USER_LOCATION_DATE, self.keywords.HASHID, self.keywords.DATE)

               elif serialized[0] == self.keywords.PRODUCT_REVIEW_USER_COMMENT:
                   self.STACKED_INSERT(self.str.DeepCleaning(serialized[1]),self.keywords.PRODUCT_REVIEW_USER_COMMENT, self.keywords.HASHID, self.keywords.COMMENT)

        except IndexError:
            pass
        finally:
            if serialized==None and self.keywords.SINGLE_DATA[self.keywords.TITLE] != "":
                self.finalize()


    def STACKED_INSERT(self, stack,table,col1,col2):
        if stack!=None and len(stack) > 0:
            try:
                stack = str(stack).replace("'",",").replace(",,",",")
                if "," in stack:
                    stacked = stack.split(",")
                    for pointer in stacked:
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
        table='PRODUCTS'
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in serialized.keys())
        values = ', '.join('"' + str(x).replace('/', '_') + '"' for x in serialized.values())
        return "INSERT INTO %s ( %s ) " \
               "VALUES " \
               "( %s );" % (table, columns, values)

    def StackedLinksQuery(self,table,col1,col2,param1,param2):
        data = 'INSERT INTO {} (`{}`,`{}`) VALUES ("{}","{}");'.format(table,col1,col2,param1,param2)
        return data



class AWSKeywords:
    HASHID='HASHID'
    LINK ="LINK"
    TITLE="TITLE"
    SELLER="SELLER"
    SELLER_LINK="SELLER_LINK"
    OFFER_RATING="OFFER_RATING"
    OFFER_TOTAL_RATING="OFFER_TOTAL_RATING"
    OFFER_PRICE="OFFER_PRICE"
    OFFER_PRICE_IS="OFFER_PRICE_IS"
    OFFER_PRICE_WAS="OFFER_PRICE_WAS"
    OFFER_SHIPPING_INFO="OFFER_SHIPPING_INFO"
    OFFER_SHORT_DESCRIPTION="OFFER_SHORT_DESCRIPTION"
    CUSTOMERS_WHO_REVIEWED_TITLE="CUSTOMERS_WHO_REVIEWED_TITLE"
    CUSTOMERS_WHO_REVIEWED_LINK="CUSTOMERS_WHO_REVIEWED_LINK"
    CUSTOMERS_WHO_REVIEWED_IMAGE="CUSTOMERS_WHO_REVIEWED_IMAGE"
    CUSTOMERS_WHO_REVIEWED_STARS="CUSTOMERS_WHO_REVIEWED_STARS"
    CUSTOMERS_WHO_REVIEWED_PRICE="CUSTOMERS_WHO_REVIEWED_PRICE"
    PRODUCT_INFO_TABLE_KEY="PRODUCT_INFO_TABLE_KEY"
    PRODUCT_INFO_TABLE_VALUE="PRODUCT_INFO_TABLE_VALUE"
    PRODUCT_DESCRIPTION="PRODUCT_DESCRIPTION"
    PRODUCT_FROM_MANUFACTURER="PRODUCT_FROM_MANUFACTURER"
    PRODUCT_REVIEW_USER = "PRODUCT_REVIEW_USER"
    PRODUCT_REVIEW_USER_LINK = "PRODUCT_REVIEW_USER_LINK"
    PRODUCT_REVIEW_USER_AVATAR = "PRODUCT_REVIEW_USER_AVATAR"
    PRODUCT_REVIEW_USER_STARS = "PRODUCT_REVIEW_USER_STARS"
    PRODUCT_REVIEW_USER_LOCATION_DATE = "PRODUCT_REVIEW_USER_LOCATION_DATE"
    PRODUCT_REVIEW_USER_COMMENT = "PRODUCT_REVIEW_USER_COMMENT"

    SINGLE_DATA = {

    }

    REVIEW_LINKS = []

    PRICES = []

    """ 
        TABLE NAME DEFINITIONS
    """

    CUSTOMERS_WHO_REVIEWED_TITLE="CUSTOMERS_WHO_REVIEWED_TITLE"
    CUSTOMERS_WHO_REVIEWED_LINK="CUSTOMERS_WHO_REVIEWED_LINK"
    CUSTOMERS_WHO_REVIEWED_IMAGE="CUSTOMERS_WHO_REVIEWED_IMAGE"
    CUSTOMERS_WHO_REVIEWED_STARS="CUSTOMERS_WHO_REVIEWED_STARS"
    CUSTOMERS_WHO_REVIEWED_PRICE="CUSTOMERS_WHO_REVIEWED_PRICE"

    PRODUCT_REVIEW_USER = "PRODUCT_REVIEW_USER"

    """
        COLUMN NAME DEFINITIONS
    """
    IMAGE = "IMAGE"
    PRICE = "PRICE"
    STARS = "STARS"
    COMMENT = 'COMMENT'
    DATE = 'DATE'
    AVATAR = 'AVATAR'
    USERNAME = 'USERNAME'
    Link = 'LINK'

    """
        EMPTY QUERY INITIALIZATIONS
    """
    CUSTOMER_WHO_REVIEWED_PRICE_QUERY = ''
    CUSTOMER_WHO_REVIEWED_RATING_QUERY = ''
    PRODUCT_REVIEW_USER_QUERY = ''