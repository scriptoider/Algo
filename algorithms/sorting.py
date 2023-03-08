import random

class Sorting:

    def bubble(self, lis):
        for i in range(len(lis)-1):
            sorted = 1
            for j in range(len(lis)-1-i):
                if lis[j] > lis[j+1]:
                    sorted = 0
                    lis[j], lis[j+1] = lis[j+1], lis[j]
            if sorted == 1:
                break
        return lis

    def insert(self, lis):
        for i in range(1, len(lis)):
            k = lis[i]
            j = i - 1
            while j >= 0 and k < lis[j]:
                lis[j+1] = lis[j]
                j -= 1
            lis[j+1] = k
        return lis

    def select(self, lis):
        for i in range(len(lis)-1):
            for j in range(i, len(lis)):
                if lis[i] > lis[j]:
                    lis[i], lis[j] = lis[j], lis[i]
        return lis

    def quick(self, lis):
        def qsort(lis):
            ls = []
            eq = []
            lr = []
            if len(lis) > 1:
                pivot = lis[len(lis) // 2]
                for i in lis:
                    if i < pivot:
                        ls.append(i)
                    elif i == pivot:
                        eq.append(i)
                    elif i > pivot:
                        lr.append(i)
                return qsort(ls) + eq + qsort(lr)
            else:
                return lis
        lis = qsort(lis)
        return lis
