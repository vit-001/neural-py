# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

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


class BaseNeuron(AbstractNeuron):
    """ Нейрон без функции активации """
    _n = 0

    def __init__(self):
        super().__init__()
        self._synapses = list()
        BaseNeuron._n += 1
        self._num = BaseNeuron._n

    def add_synaps(self, source: AbstractSignal, weight=0.0):
        self._synapses.append((source, weight))

    def process(self):
        summa = 0.0
        for (signal, weight) in self._synapses:
            summa += signal.signal * weight
        self.signal = self.activation(summa)

    def __repr__(self):
        return self._num.__str__()



if __name__ == "__main__":
    pass