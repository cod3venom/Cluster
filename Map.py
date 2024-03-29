from Strings import Strings
from Vendors.Expandica.Expandica_aws import AWS
from Vendors.PGP.PGP_AWS import PGP_AWS
class Map:
    def __init__(self):
        self.strs = Strings()
        self.aws = AWS()
        self.pgp =PGP_AWS()

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

    def pgp_map(self,data):
        if data is not None and data !="":
            data = str(data).strip()
            lines = data.split("\n")
            for line in lines:
                cleaned = self.strs.DeepCleaning(line)
                stack = self.strs.getKeyandVal(cleaned,'~')
                self.pgp.Segregate(serialized=stack)
            self.pgp.end = True
            self.pgp.Segregate(serialized=None)
