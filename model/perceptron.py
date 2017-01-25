# -*- coding: utf-8 -*-
__author__ = 'Vit'

from model.base_classes import BaseNetwork,BaseSignal,AbstractTrainingData
from model.neuron import Neuron
from typing import Tuple,List

def ErrorFunction(list_a:list(),list_b:list)->float:
    summa=0.0
    for a,b in zip(list_a,list_b):
        summa+=(a-b)**2
    return summa/2.0


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

    def training(self, data:AbstractTrainingData, training_speed:float=0.1):
        if data.get_inputs_count()!=len(self._input):
            raise RuntimeError('Неправильное количество входных данных')
        if data.get_outputs_count()!=len(self._output):
            raise RuntimeError('Неправильное количество выходных данных')
        for (input,output) in data:
            print(input,output)
            result=self.process(input)
            print(result)
            print(ErrorFunction(output,result))

    def process(self,data:list())->list():
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
    p=Perceptron(2,[3],1)
    print(p._input)
    print(p._hidden)
    print(p._output)

    from model.data.xor_data import XorData
    data=XorData()

    p.training(data)
