class Difference:
    def __init__(self, a):
        self.__elements = a
        self._ = _
        self.maximumDifference = maximumDifference

    def computeDifference(self):
        global _
        global maximumDifference
        listaDeValores = []
        _ = int(_)
        if (_ >= 1 and _ <= 10):
            for n in range(0, _):
                if (a[n] >= 1 and a[n] <= 100):
                    sizeLista= len(a)
                    for i in range(sizeLista):
                        for y in range(sizeLista):
                            if (i != y):
                                valor = abs((a[i]) - (a[y]))
                                listaDeValores.append(valor)
                    self.maximumDifference = max(listaDeValores)

# self.maximumDifference = maximumDifference
# maximumDifference = 0
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()
print d.maximumDifference
