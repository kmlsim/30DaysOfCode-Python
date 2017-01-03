# import pdb; pdb.set_trace()
class Difference:
    listaDeValores = []
    #maximumDifference = 0
    def __init__(self, a):
        self.__elements = a
        self._ = _
        #self.maximumDifference = maximumDifference
# Add your code here
    def computeDifference(self):
        global _
        global maximumDifference

        if (_ >= 1 and _ <= 10):
            for _ in range(0, 10):
                if (a[n] in range(1, 100)):
                    sizeLista= len(a)
                    for i in range(sizeLista):
                        for y in range(sizeLista):
                            if (i != y):
                                valor = abs((a[i]) - (a[y]))
                                listaDeValores.append(valor)
                    maximumDifference = max(listaDeValores)

        # return maximumDifference


_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
