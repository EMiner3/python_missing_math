import math

def clamp(value,min,max):
    if value >= min and value <= max:
        return value
    elif value < min:
        return min
    elif value > max:
        return max

def sort_insertion(array): 
  
    #loop through the array 
    for i in range(1, len(array)): 
  
        currentItem = array[i] 
  
        #move elements of array[0..i-1], that are 
        #greater than current, to a position ahead
        
        j = i-1
        while j >= 0 and currentItem < array[j] : 
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = currentItem
        print('Comparison>',array)
    return array



class lfo:
    def __init__(self,parent,wave,attenuation,min,max,cycletime):
        self.in_value = 0
        self.out_value = 0
        self.current_value = max
        self.parent = parent
        self.atten = attenuation
        self.direction = True
        self.wave = wave
        self.cycle_time = cycletime
        self.min = min
        self.max = max
        self.lfo_out = 0

    def triangle(self):
        if self.current_value >= self.max:
            self.direction = False
        elif self.current_value <= self.min:
            self.direction = True
        if self.direction:
            self.current_value = self.current_value + 1 * self.cycle_time
        else:
            self.current_value = self.current_value - 1 * self.cycle_time
        self.lfo_out_1 = self.attenuation()
        return self.lfo_out_1


    def saw(self):
        if self.current_value >= self.max:
            self.direction = True
            self.current_value = self.min
        if self.direction:
            self.current_value = self.current_value + 1 * self.cycle_time
        else:
            self.current_value = self.current_value - 1 * self.cycle_time
        self.lfo_out_1 = self.attenuation()
        return self.lfo_out_1


    def square(self):
        if self.current_value >= self.max:
            self.direction = False
        elif self.current_value <= self.min:
            self.direction = True
        if self.direction:
            self.current_value = self.max
        else:
            self.current_value = self.min
        self.lfo_out_1 = self.attenuation()
        return self.lfo_out_1


    def run(self):
        if self.wave == 'triangle' or self.wave == 'tri':
            self.lfo_out = self.triangle()
            return self.lfo_out
        if self.wave == 'saw':
            self.lfo_out = self.saw()
            return self.lfo_out
        if self.wave == 'square' or self.wave == 'sqr':
            self.lfo_out = self.square()
            return self.lfo_out


    def attenuation(self):
        
        if self.current_value > self.max:
            self.current_value = self.max
        elif self.current_value < self.min:
            self.current_value = self.min
        self.out_value = math.floor(self.current_value*self.atten)
        
        return self.out_value




'''


Quake Fast inverse square root
add 'import numpy as np' to top to enable



def Q_rsqrt(number):
    threehalfs = 1.5
    x2 = number * 0.5
    y = np.float32(number)
    
    i = y.view(np.int32)                        # evil floating point bit level hacking
    i = np.int32(0x5f3759df) - np.int32(i >> 1) # what the fuck?
    y = i.view(np.float32)
    
    y = y * (threehalfs - (x2 * y * y))         #1st iteration
    # y = y * (threehalfs - (x2 * y * y))         #2nd iteration, this can be removed
    return float(y)



'''