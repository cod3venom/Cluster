from __config__ import __config__
from Strings import Strings
from Vendors.AWS import AWS
class Map:
    def __init__(self):
        self.strs = Strings()
        self.aws = AWS()
    def aws_map(self,data):
        if data is not None and data !="":
            data = str(data).strip()
            lines = data.split("\n")
            for line in lines:
                cleaned = self.strs.DeepCleaning(line)
                stack = self.strs.getKeyandVal(cleaned,'~')
                self.aws.Segregate(serialized=stack)
            self.aws.end = True
            self.aws.Segregate(serialized=None)
