from __config__ import __config__
from Machines import Machines
from Map import Map
from Strings import Strings
from Commander import Commander

import socket, threading

class Server:
    stop = False
    socket_list = []
    def __init__(self, type):
        self.__machines__ = Machines()
        self.__map__ = Map()
        self.__ip__= ''
        self.__msg_ = ''
        self.string = Strings()
        self.com = Commander()

        if type == "UDP":
            self.udpModel = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.Open_U()

    def Open_T(self):
        pass

    def Open_U(self):
        if self.udpModel is not None:
            self.udpModel.bind((__config__.__HOST__,__config__.__PORT__ ))
            self.ListenU(self.udpModel)

    def ListenU(self, model):
        while self.stop == False:
            print("listen")
            __RECV__ = model.recvfrom(__config__.__BUFFER__)
            self.__ip__ = __RECV__[1]
            self.__stack__ = __RECV__[0]
            self.__machines__.Register(self.__ip__, self.__stack__)
            self.com.handler(self.__stack__.decode())




    def Send(self,target):
        pass

    def __cmd__(self):
        pass

    def debug(self, addr,msg):
        if addr != "" and msg != "":
            print("{} : {}".format(str(addr),str(msg)))












# users = {'USERS':[]}
# next = -1
# for i in range(100):
#     next += i
#     users['USERS'].append({"ID":str(i)})
#     users['USERS'][next] = []
#     users['USERS'][next].append({"ID":str(i), "USERNAME":"ABC"+str(i), "EMAIL":"ABC"+str(i)+"@gmail.com"})
