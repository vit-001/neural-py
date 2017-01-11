# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

class AbstractSignal:
    @property
    def signal(self):
        return 0.0

class AbstractNeuron(AbstractSignal):
    def add_sinaps(self, other, weight=0.0):
        pass


class Neuron(AbstractNeuron):
    _n=0

    def __init__(self):
        self._synapses=list()
        Neuron._n+=1
        self._num=Neuron._n

    def add_synaps(self, source:AbstractNeuron, weight=0.0):
        self._synapses.append((source,weight))


    def __repr__(self):
        return self._num.__str__()


if __name__ == "__main__":
    a1=Neuron()
    a2 = Neuron()
    b=Neuron()
    b.add_synaps(a1)
    b.add_synaps(a2)
    print(a1,b)
    print(b._synapses)
    print(b.signal)