import os, locale
class TxtBundler:
    def __init__(self):
        self.__location__ = locale.getdefaultlocale()
        if self.__location__ is not None:
            self.__init_file__ = str("TXT/Texts_{}.init".format(self.__location__[0]))


    def getString(self,num):
        if os.path.isfile(self.__init_file__):
            with open(self.__init_file__, "r") as __reader:
                for i,line in enumerate(__reader):
                    if i == int(num):
                        line = line.strip()
                        if line is None:
                            return  "LINE {} IN {} IS NoneType".format(str(num),self.__init_file__)
                        else:
                            if "#" in line:
                                return line.split("#")[1]

