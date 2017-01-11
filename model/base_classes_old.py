# -*- coding: utf-8 -*-
__author__ = 'Vit'

from abc import ABCMeta,abstractmethod

class Sygnal:
    n=0
    def __init__(self):
        self.sygnal=0.0

class AbstractNeuron(Sygnal):
    __metaclass__=ABCMeta

    @abstractmethod
    def add_synaps(self, other_neuron):
        pass

    @abstractmethod
    def process(self):
        pass


if __name__ == "__main__":
    a=AbstractNeuron()