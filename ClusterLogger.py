from colorama import Fore, Back, Style
from colorama import init

from TxtBundler import  TxtBundler
import datetime

class ClusterLogger:
    def __init__(self,status,action,description):
        self.status = status
        self.action = str(action)
        self.description = str(description)
        self.cluster_id = 0

        self.green = str(Fore.GREEN)
        self.red = str(Fore.RED)
        self.yellow = str(Fore.YELLOW)
        self.blue = str(Fore.BLUE)
        self.white = str(Fore.WHITE)
        self.black = str(Fore.BLACK)

        self.bold = ""#'\033[1m'
        self.endbold = ""#'\033[0m'

        self.Show()

    def Show(self):
        Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.status is not None and self.status == 1:
            print(self.bold+"[" + self.green + " OK " + self.white + "] {}  {}".format(self.action, self.description))
        if self.status is not None and self.status == 2:
            print("\r\n"+self.bold+"[" + self.red + " FAIL " + self.white + "] {} == {} \r\n".format(self.action, self.description))
        if self.status is not None and self.status == 3:
            print("\r\n"+self.bold+"[" + self.yellow + " Warn " + self.white + "] {} == {} \r\n".format(self.action, self.description))
        if self.status is not None and self.status == 4:
            print(self.bold+"[" + self.blue + " Info " + self.white + "] {} == {}".format(self.action, self.description))


