##This is an entery
import random as r
import math as m
class InPut:
    val=0
    noise=0
    wage=0
    endVal=0

    def __init__(self, iniVal, mean, sig):
        self.val=iniVal
        self.wage=r.random()
        self.noise=r.gauss(mean,sig)
        self.calculate()

    def printInputStat(self):
        print(f"""
        !! Input:
        IniVal={self.val}
        EndVal={self.endVal}
        Noise={self.noise}
        Wage(a)={self.wage}
        """)

    def calculate(self):
        self.endVal=self.wage*(m.fabs(self.val-self.noise*r.uniform(0.0001,0.1)))
