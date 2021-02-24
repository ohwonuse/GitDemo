from demo import Calcualtor


class ChileImpl(Calcualtor):
    num2 = 200

    def __init__(self):
        Calcualtor.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChileImpl()
print(obj.getCompleteData())