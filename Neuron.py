import ActvFunc,InPut
import random as r
import math
class Neuron:
    aFun=0
    inVec=list()
    out=0
#learn-wsp uczenia.
    learn,alpha,beta,b1,b2,b3,b4=0,0,0,0,0,0,0

    def __init__(self):
        self.alpha=r.random()
        self.beta=r.random()
        self.b1=r.random()
        self.b2=r.random()
        self.b3=r.random()
        self.b4=r.random()
        self.learn=r.uniform(0.001,0.01)

    def setAFun(self,x):
        self.aFun=x

    def addInput(self,var,m=0,s=0):
        n=InPut.InPut(var,m,s)
        self.inVec.append(n)

    def feature(self):
        sum=0

        for i in self.inVec:
            i.calculate()
            sum+=i.endVal
        if self.aFun==ActvFunc.sigmoid:
            self.out=self.aFun(sum,self.beta)
        else:
            self.out=self.aFun(sum,self.alpha,self.b1,self.b2,self.b3,self.b4)

    def training(self,y,error):
        delta=math.fabs(y-self.out)
        d1=delta
        lenx=len(self.inVec)
        while(delta>error):
            for i in range(lenx):
                self.inVec[i].wage+=self.learn*(y-self.out)*self.inVec[i].endVal
                print(f"{[i+1]}: ",self.inVec[i].wage,end=' ')
            self.feature()
            delta=math.fabs(y-self.out)
            if delta==d1:
                for i in range(lenx):
                    r.seed()
                    self.inVec[i].wage=r.random()
                    self.alpha=r.random()
                    self.beta=r.random()
                    self.b1=r.random()
                    self.b2=r.random()
                    self.b3=r.random()
                    self.b4=r.random()
                    self.learn=r.uniform(0.001,0.01)
                    self.feature()
            else:
                d1=delta
            print('\nOUT: ',self.out,f"\tD: {delta}")
