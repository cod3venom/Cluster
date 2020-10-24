from Strings import Strings
from Map import Map
class Commander:
    def __init__(self):
        self.str = Strings()
        self.map = Map()
        self.vend  = VENDORS()

    def handler(self,input):
        com = self.str.entryCOM(input)[0]

        if com == self.vend.AWS:
            self.map.aws_map(input)

        if com == self.vend.PGP:
            self.map.pgp_map(input)



class VENDORS:
    AWS = "AWS"
    PGP = "PGP"