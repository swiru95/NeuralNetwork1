import Neuron

x=[ [1,0],
    [1,1],
    [0,1],
    [0,0]]

Y=[1,0,1,0]

l1=[Neuron.Neuron(),Neuron.Neuron()]
l2=Neuron.Neuron()

l1[0].addInput(x[0][0],s=0.1)
l1[0].addInput(x[0][1],s=0.1)
l1[0].setAFun(Neuron.ActvFunc.sigmoid)

l1[1].addInput(x[0][0],s=0.2)
l1[1].addInput(x[0][1],s=0.2)
l1[1].setAFun(Neuron.ActvFunc.sigmoid)

l1[0].feature()
l1[1].feature()

l2.addInput(l1[0].out)
l2.addInput(l1[1].out)
l2.setAFun(Neuron.ActvFunc.sigmoid)

l2.feature()

func=Neuron.ActvFunc.dsigmoid

for i in range(1000):
    print(f"\n\n__ROUND__[{i}]\n\n\n")
    l2.training(Y[0],0.2)
    delta=(Y[0]-l2.out)*func(l2.out,l2.beta)
    l1[0].training(l1[0].out+delta,0.2)
    l1[1].training(l1[1].out+delta,0.2)

print(f"FINIShED: {[Y[0],l2.out]} \a")
p=list()
p.append(input("> "))
p.append(input("> "))
while(p[0]!='-' and p[1]!='-'):
    l1[0].inVec[0].val=int(p[0])
    l1[0].inVec[0].calculate()
    l1[0].inVec[1].val=int(p[1])
    l1[0].inVec[1].calculate()

    l1[1].inVec[0].val=int(p[0])
    l1[1].inVec[0].calculate()
    l1[1].inVec[1].val=int(p[1])
    l1[1].inVec[1].calculate()

    l1[0].feature()
    l1[1].feature()
    l2.inVec[0].val=l1[0].out
    l2.inVec[1].val=l1[1].out
    l2.inVec[0].calculate()
    l2.inVec[1].calculate()
    l2.feature()
    print(f"FINIShED: {[Y[0],l2.out]} \a")
    p[0]=input("> ")
    p[1]=input("> ")
