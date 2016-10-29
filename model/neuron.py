# -*- coding: utf-8 -*-
__author__ = 'Vit'

from model.base_classes import AbstractNeuron

class Neuron(AbstractNeuron):
    n=0

    def __init__(self):
        super().__init__()
        self.synapses=list()
        self.weights=list()

        self.num=Neuron.n
        Neuron.n+=1

    def add_synaps(self, other_neuron):
        self.synapses.append(other_neuron)
        self.weights.append(0.0)

    def process(self):
        summa=0.0
        for i in range(len(self.synapses)):
            summa+=self.weights[i]*self.synapses[i].sygnal

        self.sygnal=self.func(summa)

    def func(self,summa):
        if summa>=0.0: return 1.0
        else: return 0.0

    def __repr__(self):
        return self.num.__str__()


if __name__ == "__main__":
    n1=Neuron()
    n2=Neuron()
    n3=Neuron()

    print(n1.sygnal)

    n1.add_synaps(n2)
    n1.add_synaps(n3)
    n1.process()

    print(n1.sygnal)