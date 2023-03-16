import numpy as np
import os

class Environment(object):
    g = 9.8         # m/s
    G = 6.67e-11    # gravitational constant
    def __init__(self,**kwargs):
        self.yi = kwargs['yi']        # y initial
   
class Normal_Object(Environment) :
    def __init__(self,**kwargs):
        self.mass = kwargs['mass']      # mass
        self.vi = kwargs['vi']          # velocity initial
        self.theta = kwargs['theta']    # angle of action

class Calculate(object):
    def G_Work_Instant(self,object:Normal_Object, env:Environment):
        W = object.mass * env.g * env.yi # J
        print(W)
        return W

    def Change_U(self,W:float): 
        print(-W)
        return -W #J

env = Environment(yi=8.38)
snowball = Normal_Object(mass=2.5,vi=10.8,theta=40)

calculator = Calculate()
W = calculator.G_Work_Instant(snowball, env)
calculator.Change_U(W)