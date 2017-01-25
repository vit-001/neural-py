# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

from model.base_classes import BaseTrainingData


class XorData(BaseTrainingData):
    def get_inputs_count(self) -> int:
        return 2

    def get_outputs_count(self) -> int:
        return 1

    def __iter__(self):
        for i in range(2):
            for j in range(2):
                if i==j:
                    xor=0
                else:
                    xor=1
                yield ([i,j],[xor])


if __name__ == "__main__":
    pass