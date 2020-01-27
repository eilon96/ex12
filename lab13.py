def bunch_together(iterable, n):
    return MyIter(iterable, n)


class MyIter():
    def __init__(self, iterable, n):
        self.index = 0
        self.lst = []
        k=0
        tup=()
        for i in iterable:
            if k == n:
                k = 1
                self.lst.append(tup)
                tup = (i,)
            else:
                k += 1
                new_tup = (i,)
                tup = tup + new_tup

        if tup != ():
            tup = tup + (n - len(tup)) * (None,)
            self.lst.append(tup)


    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            self.index += 1
            return self.lst[self.index - 1]
        else:
            raise StopIteration
if __name__ == '__main__':
    for x in bunch_together(range(10),3): print(x)


