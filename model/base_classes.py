# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

from typing import Tuple,List
from collections import Iterable



class BackPropogationData():
    def __init__(self):
        self._delta_from_childs=0.0

class AbstractSignal(BackPropogationData):
    # @property
    # def signal(self):
    #     return self._signal

    def __init__(self):
        super().__init__()
        self.signal=0.0

class AbstractNeuron(BackPropogationData):
    def __init__(self):
        BackPropogationData.__init__(self)

    def add_synaps(self, other, weight=0.0):
        pass
    def process(self):
        pass
    def activation(self, summa:float)->float:
        raise RuntimeError('Переопределите AbstractNeuron.activation')

class AbstractNetwork:
    pass

class AbstractTrainingData(Iterable):
    def get_inputs_count(self)->int:
        return 0
    def get_outputs_count(self)->int:
        return 0

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
        self._weight=list()
        BaseNeuron._n += 1
        self._num = BaseNeuron._n

    def add_synaps(self, source: AbstractSignal, weight=0.0):
        self._synapses.append(source)
        self._weight.append(weight)


    def process(self):
        summa = 0.0
        for (signal, weight) in zip(self._synapses,self._weight):
            summa += signal.signal * weight
        self.signal = self.activation(summa)
        self._delta_from_childs=0.0

    def __repr__(self):
        str="n"+self._num.__str__()+"<"
        for (synaps,weight) in zip(self._synapses,self._weight):
            str+=synaps.__repr__().partition('<')[0]+';'
        str=str.rstrip(';')+'>'
        return str

    def correct_weight(self, delta, training_speed):
        for i in range(len(self._weight)):
            self._synapses[i]._delta_from_childs+=self._weight[i]*delta
            self._weight[i]+=self._synapses[i].signal*delta*training_speed

class BaseNetwork(AbstractNetwork):
    def training(self, data:AbstractTrainingData):
        pass
    def process(self, inputs:list())->list():
        pass

class BaseTrainingData(AbstractTrainingData):
    pass


if __name__ == "__main__":
    pass