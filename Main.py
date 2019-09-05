import Neuron, ActvFunc
import random as r

r.seed()
n=Neuron.Neuron()
n.setAFun(ActvFunc.sigmoid)
n.addInput(0.71,0,0.3)
n.addInput(0.32,0,0.2)
n.addInput(0.41,0,0.1)
n.feature()
n.training(0.74,0.01)
print('\n:',n.out)
