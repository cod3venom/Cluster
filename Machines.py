from __config__ import __config__

class Machines:
    id = 0

    def isClustered(self):
        pass

    def Register(self,ip,stack):
        self.id += 1
        __config__.__MACHINES__["MACHINES"].append({
            "ID":self.id,"IP":str(ip), "STACK":str(stack.decode())
        }),
        self.View()

    def View(self):
        pass
        #print(str(__config__.__MACHINES__["MACHINES"][self.id-1]))