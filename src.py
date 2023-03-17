import numpy as np
import math
import os

class Force(object):
    def __init__(self, **kwargs):
        for key, _ in kwargs.items():
            if(key == 'A'): self.fa = kwargs['A']            # N Applied Force       
            if(key == 'theta'): self.theta = kwargs['theta'] # angle of force

class Normal_Material(object):
    def __init__(self,**kwargs):
        for key, _ in kwargs.items():
            if(key == 'kf'): self.kf = kwargs['kf']          # mu kinetic friction coeficient
            if(key == 'deth'): self.deth = kwargs['deth']       # J change in kinetic energy

class Normal_Object(object) :
    def __init__(self,**kwargs):
        for key, _ in kwargs.items():
            if(key == 'kei'): self.kei = kwargs['kei']       # J kinetic enery initial
            if(key == 'kef'): self.kef = kwargs['kef']       # J kinetic energy final
            if(key == 'dke'): self.dke = kwargs['dke']       # J change in kinetic energy
            if(key == 'ethi'): self.ethi = kwargs['ethi']    # J thermal energy inital
            if(key == 'ethf'): self.ethf = kwargs['ethf']    # J thermal energy final
            if(key == 'deth'): self.deth = kwargs['deth']    # J change in thermal energy
            if(key == 'xi'): self.xi = kwargs['xi']          # x initial
            if(key == 'xf'): self.xf = kwargs['xf']          # x final
            if(key == 'dx'): self.dx = kwargs['dx']          # x change in x
            if(key == 'yi'): self.yi = kwargs['yi']          # y initial
            else:self.yi = 0
            if(key == 'yf'): 
                self.yf = kwargs['yf']                       # y final
                self.dy = self.yf - self.yi                  # change y
            if(key == 'mass'): self.mass = kwargs['mass']    # kg mass
            if(key == 'vi'): self.vi = kwargs['vi']          # m/s velocity initial
            if(key == 'vf'): self.vf = kwargs['vf']          # m/s velocity final
            if(key == 'theta'): self.theta = kwargs['theta'] # angle of action
            else: self.theta = 0.0

class Environment(object):
    g = 9.81        # m/s
    G = 6.67e-11    # gravitational constant

    
    class Calculate():

        def Work_Instant(self, obj:Normal_Object, force:Force):
            W = math.cos(obj.theta) * force.fa * obj.dx
            print(W)
            return W
        
        def G_Work_Instant(self,obj:Normal_Object):
            W = obj.mass * Environment.g * obj.yi # J
            print(W)
            return W

        def Chg_Kinetic_Energy(self, obj:Normal_Object, force:Force, deth:float):
            work = self.Work_Instant(obj,force)
            obj.dke = work - deth
            print(obj.dke)
            return obj.dke # J

        def Chg_Thermal_Energy_Friction(self,obj:Normal_Object, material:Normal_Material):
            dethf = material.kf * obj.mass*super().g * obj.dx
            print(dethf)
            return dethf # J

        def Chg_Thermal_Energy_Material(self, material:Normal_Material, obj:Normal_Object):
            material.deth = self.Chg_Thermal_Energy_Friction(obj,material) - obj.deth
            print(material.deth)
            return material.deth # J

        def Chg_Potential_Energy(self, W:float): # change in potential energy
            print(-W)
            return -W #J
        
        def Get_Vi_Projectile_Vf(self,obj:Normal_Object, time):
            vi = obj.vf*math.sin(math.pi/2) - (Environment.g * time)
            print(vi)
            return vi # m/s

        def Get_Vi_Projectile_Dy(obj:Normal_Object, time):
            vi = (obj.dy-(0.5 * Environment.g * math.pow(time,2))) / (math.sin(math.pi/2) * time)
            print(vi)
            return vi # m/s

        def Get_Vi_Ke(obj:Normal_Object):
            vi = math.sqrt((2*obj.kei)/ obj.mass)
            print(vi)
            return vi
        def Get_Vf(self, obj:Normal_Object):
            vf = math.sqrt(math.pow(obj.vi, 2) + 2*(Environment.g * obj.yi) - 2*(Environment.g*obj.yf))
            print(vf)
            return vf # m/s
        
        def Get_Max_Height(self, obj:Normal_Object):
            hmax = (0.5*math.pow(obj.vi,2) + Environment.g*obj.yi) / Environment.g
            print(hmax)
            return hmax

env = Environment()

particle = Normal_Object(mass=0.88, kei=400)
env.Calculate.Get_Vi_Ke(particle)