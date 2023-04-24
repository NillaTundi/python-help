class temperature:
    ##class variables/values/constants
    tscale = {'C':'Celsius','F':'Fahrenheit','K':'Kelvin','R':'Reaumur','Ra':'Rankine','D':'Delisle'}
    def __init__(self,newVal=0.0,newScale='C'):
       self.val = newVal
       self.scale = newScale
    def scale(self):
        return (self.scale)
    def set(self,newVal,newScale): 
        self.val = float(newVal)
        self.scale = newScale
    def degC(self):
        return self.val
    def degF(self):
        return self.val*(9.0/5.0)+32.0
    def degK(self):
        return self.val+273.15
    def degR(self):
        return self.val*0.8
    def degRa(self):
        return self.val*(9.0/5.0)+491.67
    def degD(self):
        return (100-self.val*(2/3))
    def convert_to(self, newScale):
        if self.scale == newScale:
            return self.val
        elif self.scale == 'C':
            if newScale == 'F':
                return self.degF()
            elif newScale == 'K':
                return self.degK()
            elif newScale == 'R':
                return self.degR()
            elif newScale == 'Ra':
                return self.degRa()
            elif newScale == 'D':
                return self.degD()
        elif self.scale == 'F':
            if newScale == 'C':
                return (self.val - 32) * (5/9)
            elif newScale == 'K':
                return (self.val + 459.67) * (5/9)
            elif newScale == 'R':
                return (self.val - 32) * (4/9)
            elif newScale == 'Ra':
                return self.val + 459.67
            elif newScale == 'D':
                return (212 - self.val) * (5/6)
        elif self.scale == 'K':
            if newScale == 'C':
                return self.val - 273.15
            elif newScale == 'F':
                return self.val * (9/5) - 459.67
            elif newScale == 'R':
                return self.val * (4/5)
            elif newScale == 'Ra':
                return self.val * (9/5)
            elif newScale == 'D':
                return (373.15 - self.val) * (2/3)
        elif self.scale == 'R':
            if newScale == 'C':
                return self.val * (5/4)
            elif newScale == 'F':
                return self.val * (9/4) + 32
            elif newScale == 'K':
                return self.val * (5/4)
            elif newScale == 'Ra':
                return self.val * (9/4)
            elif newScale == 'D':
                return (80 - self.val) * (15/8)
        elif self.scale == 'Ra':
            if newScale == 'C':
                return (self.val - 491.67) * (5/9)
            elif newScale == 'F':
                return self.val - 459.67
            elif newScale == 'K':
                return self.val * (5/9)
            elif newScale == 'R':
                return self.val
            elif newScale == 'D':
                return (671.67 - self.val) * (5/6)
        elif self.scale == 'D':
            if newScale == 'C':
                return 100 - self.val * (3/2)
            elif newScale == 'F':
                return 212 - self.val * (6/5)
            elif newScale == 'K':
                return 373.15 - self.val * (3/2)
            elif newScale == 'R':
                return 80 - self.val * (8/15)
            elif newScale == 'Ra':
                return 671.67 - self.val * (6/5)
        else:
            raise ValueError("Invalid temperature scale")

    ##customization
    def __str__(self):
                return "{:.1f}{}".format(self.val, self.scale)
    def __lt__(self,RHS):
       
        return self.convert_to(self.scale) < RHS.convert_to(self.scale)
        
    def __gt__(self,RHS):
        
        return self.convert_to(self.scale) > RHS.convert_to(self.scale)
        
    def __le__(self,RHS):
        
        return self.convert_to(self.scale) <= RHS.convert_to(self.scale)
    def __ge__(self,RHS):
        
        return self.convert_to(self.scale) >= RHS.convert_to(self.scale)

    def __eq__(self,RHS):
        
        if isinstance(RHS, temperature):
            RHS_val = RHS.convert(self.scale())
            return self.val == RHS_val
        else:
            return False
    
    def __ne__(self,RHS):
        
         if isinstance(RHS, temperature):
            RHS_val = RHS.convert(self.scale())
            return self.val != RHS_val
         else:
            return True
    
    def __sub__(self,RHS):
        
        if isinstance(RHS, temperature):
            
            RHS_val = RHS.convert_to(self.scale())
            return temperature(self.val - RHS_val, self.scale())
        else:
            raise TypeError("Cannot subtract non-temperature value from temperature")
        
    def __int__(self):
    
        return int(self.val)
    
    def __float__(self):
       
        return float(self.val)
    
    def myScale(self):
       
        return self.scale()
    
if __name__ == "__main__":
    ##testing driver
    aTemp = temperature(4.6,'F')
    aTemp.set(54.5,'C')
    print(aTemp)
    anotherTemp = temperature(250,'K')
    anotherTemp.set(400,'Ra')
    if (anotherTemp < aTemp):
        print("passes < test")
    else:
        print("fails < test")
    print(int(aTemp))
    print(float(aTemp))
    print(aTemp)
    print(aTemp - anotherTemp)
    print(aTemp.myScale())
