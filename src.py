import numpy as np
import math
import os

class Environment(object):
    g = 9.81        # m/s
    G = 6.67e-11    # gravitational constant
   
class Normal_Object(Environment) :
    def __init__(self,**kwargs):
        for key, val in kwargs.items():
            if(key == 'yi'): self.yi = kwargs['yi']          # y initial
            if(key == 'yf'): self.yf = kwargs['yf']          # y final
            if(key == 'mass'): self.mass = kwargs['mass']      # mass
            if(key == 'vi'): self.vi = kwargs['vi']          # velocity initial
            if(key == 'theta'): self.theta = kwargs['theta']    # angle of action

class Calculate(Environment):
    def G_Work_Instant(self,obj:Normal_Object):
        W = obj.mass * super().g * obj.yi # J
        print(W)
        return W

    def Change_U(self, W:float): 
        print(-W)
        return -W #J
    
    def Get_Vf(self, obj:Normal_Object):
        vf = math.sqrt(math.pow(obj.vi, 2) + (super().g * obj.yi)- (super().g*obj.yf))
        print(vf)
        return vf
rollerCoaster = Normal_Object(mass=831,vi=16.0 , yi=43.0, yf=0)

calculator = Calculate()
V = calculator.Get_Vf(rollerCoaster)