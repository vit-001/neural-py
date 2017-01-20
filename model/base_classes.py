# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

from typing import Tuple,List

class AbstractSignal:
    # @property
    # def signal(self):
    #     return self._signal

    def __init__(self):
        self.signal=0.0

class AbstractNeuron(AbstractSignal):
    def add_synaps(self, other, weight=0.0):
        pass
    def process(self):
        pass
    def activation(self, summa:float)->float:
        raise RuntimeError('Переопределите AbstractNeuron.activation')

class AbstractNetwork:
    pass

class AbstractData:
    def get_inputs_count(self)->int:
        return 0
    def get_outputs_count(self)->int:
        return 0
    def __next__(self)->Tuple(List(int),List(int)): #intputs list, outputs list
        raise StopIteration

class BaseSignal(AbstractSignal):
    _n = 0
    def __init__(self):
        super().__init__()
        BaseSignal._n += 1
        self._num = BaseSignal._n

    def __repr__(self):
        return "s"+self._num.__str__()

class BaseNeuron(AbstractNeuron):
    """ Нейрон без функции активации """
    _n = 0

    def __init__(self):
        super().__init__()
        self._synapses = list()
        BaseNeuron._n += 1
        self._num = BaseNeuron._n

    def add_synaps(self, source: AbstractSignal, weight=1.0):
        self._synapses.append((source, weight))

    def process(self):
        summa = 0.0
        for (signal, weight) in self._synapses:
            summa += signal.signal * weight
        self.signal = self.activation(summa)

    def __repr__(self):
        str="n"+self._num.__str__()+"<"
        for (synaps,weight) in self._synapses:
            str+=synaps.__repr__().partition('<')[0]+';'
        str=str.rstrip(';')+'>'
        return str


class BaseNetwork(AbstractNetwork):
    def training(self,data:AbstractData):
        pass
    def process(self, inputs:List(int))->List(int):
        pass

class BaseData(AbstractData):
    pass


if __name__ == "__main__":
    pass