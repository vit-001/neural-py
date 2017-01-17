# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

from struct import unpack

from model.base_classes import BaseData


class MnistData(BaseData):
    def __init__(self, set_name:str):
        self.images = open('mnist/' + set_name + '-images.idx3-ubyte', 'rb')
        self.labels = open('mnist/' + set_name + '-labels.idx1-ubyte', 'rb')
        labels_majic, self.labels_size = unpack('>ii', self.labels.read(8))
        print(labels_majic, self.labels_size)

        image_majic, self.image_size, self.row, self.col = unpack('>iiii', self.images.read(16))
        print(image_majic, self.image_size, self.row, self.col)

    def next(self):
        (label,)=unpack('B',self.labels.read(1))
        data=unpack('B'*(self.col*self.row),self.images.read(self.col*self.row))
        return (label,data)

    def visualize(self,data):
        for col in range(m.col):
            for row in range(m.row):
                print('{:3} '.format(data[col * m.row + row]), end='')
            print()

if __name__ == "__main__":
    m = MnistData('t10k')
    m1= MnistData('train')
    print(m.images)
    print(m.labels)

    for i in range(100):
        label,data=m.next()
        print(label)
        m.visualize(data)


    # d=m.labels.read(8)
    # print(d)
    # majic,size=unpack('>ii', d)
    # print(majic,size)
    #
    # for i in range(size):
    #     (byte,)=unpack('B',m.labels.read(1))
    #     print(byte)
    #
    # print(m.labels.read(1))

    # while True:
    #     data=m.labels.read(1)
    #     print(unpack('B',data))
    #     if data == b'': break
