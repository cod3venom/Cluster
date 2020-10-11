from hashlib import md5
import time
class Strings:
    blacklist = ["'","\n","\"", "\\n", 'Brand:']
    deepblacklist = ["]","[", ",","\"", "AWS!", ' ',"",'  ']
    entryCOM_del =  '!'
    emptylist = [" ","","   ", "      ",]


    def Clean(self,data):
        if data is not None and data !="":
            for black in self.blacklist:
                data = data.replace(black,"")
        return data

    def DeepCleaning(self,data):
        if data is not None and data !="":
            for black in self.deepblacklist:
                data = data.replace(black,"")
        return data
    def getKeyandVal(self,data,delim):
        if data is not None and delim is not None:
            return data.split(delim)

    def md5ID(self,type):
        if type == "random":
            millis = str(int(round(time.time() * 1000)))
            return str(md5(millis.encode("utf-8")).hexdigest())



    '''
     WHEN UDP PROTOCOL GETS SOME MESSAGES , NO MATTER WHAT TYPE OF DATA IS IT,
     EVERYTHING IS CONVERTED FROM BYTES TO STRING, THEN XPATH LIST[] FROM [Cortex] IN [Cluster] IS RECEIVED AS STRING
     SO NEED TO TRANSFORM STRING TO LIST
    '''
    def ReshapeAWSLinks(self,string):
        cpy = []
        if string!= None and "'" in string:
            string = string.replace("'",",").replace(",,","")
            cpy = string.split(",")
        return cpy
    def entryCOM(self,data):
        out = ''
        if data is not None and self.entryCOM_del in data:
            try:
                out = data.split(self.entryCOM_del)[0]
            except IndexError:
                pass
        return out