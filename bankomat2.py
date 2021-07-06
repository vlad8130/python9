from collections import OrderedDict
 
class ACM(object):
    def __init__(self, x=10):
        self.r = OrderedDict(((500, x), (100, x), (50, x), (20, x), (10, x), (5, x), (2, x), (1, x)))
        
    def get_money(self, s):
        res = {500: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
        for k, _ in self.r.items():
            if s == 0:
                break
            while self.r[k] > 0 and s >= k:
                self.r[k] = self.r[k] - 1
                res[k] += 1
                s -= k
                # print(s)
        if s == 0:
            print(res)
        else:
            raise ValueError
        
b = ACM()
b.get_money(800)
