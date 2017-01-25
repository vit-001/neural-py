# -*- coding: utf-8 -*-
__author__ = 'Nikitin'
from collections import Iterable


class A(Iterable):
    def __iter__(self):

        for i in range(10):
            yield (i,1)



if __name__ == "__main__":
    a=A()
    b=A()
    for i,j in zip(a,b):
        print(i,j)

    for i in b:
        print(i)
