# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

from model.base_classes import AbstractNeuron, AbstractSignal, BaseNeuron
import math

class Neuron(BaseNeuron):
    def activation(self, summa: float) -> float:
        # if summa <= -0.5:
        #     return 0.0
        # if summa >= 0.5:
        #     return 1.0
        # return summa + 0.5
        return math.tanh(summa)


if __name__ == "__main__":
    import time

    start = time.time()
    b = Neuron()
    neurons = list()
    for i in range(1000000):
        qurrent = Neuron()
        b.add_synaps(qurrent, 1.0)
        qurrent.add_synaps(b)
        neurons.append(qurrent)
    t1=time.time()
    print(t1 - start)
    for neuron in neurons:
        neuron.process()
    t2 = time.time()
    print(t2 - t1)
    b.process()
    print(time.time() - t2)
