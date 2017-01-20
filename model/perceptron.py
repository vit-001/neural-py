# -*- coding: utf-8 -*-
__author__ = 'Vit'

from model.base_classes import BaseNetwork,BaseSignal,AbstractData
from model.neuron import Neuron
from typing import Tuple,List

class Perceptron(BaseNetwork):
    def __init__(self, inputs:int,hidden:list, outputs:int):

        def add_synapses(prev_layer,current_layer):
            for neuron in current_layer:
                for source in prev_layer:
                    neuron.add_synaps(source)

        self._input=[BaseSignal() for i in range(inputs)]

        prev_layer=self._input
        self._hidden=list()
        for i in hidden:
            layer=[Neuron() for j in range(i)]
            add_synapses(prev_layer,layer)
            prev_layer=layer
            self._hidden.append(layer)
        self._output=[Neuron() for i in range(outputs)]
        add_synapses(prev_layer,self._output)

    def training(self,data:AbstractData):
        pass


    def process(self,data:List(int))->List(int):
        if len(data)!=len(self._input):
            raise RuntimeError('Perceptron: неправильное количество данных на входе')
        for inp, value in zip(self._input,data):
            inp.signal=value

        def process_layer(layer:list):
            for item in layer:
                item.process()

        for layer in self._hidden:
            process_layer(layer)

        process_layer(self._output)

        return [item.signal for item in self._output]


if __name__ == "__main__":
    p=Perceptron(3,[3,2],3)
    print(p._input)
    print(p._hidden)
    print(p._output)

    print(p.process([1.0,2.0,3.0]))

    for inp in p._input:
        print(inp,inp.signal)

    for layer in p._hidden:
        for item in layer:
            print(item,item.signal)

    for out in p._output:
        print(out,out.signal)

