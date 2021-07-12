# python_missing_math

## head to the Wiki (https://github.com/EMiner3/python_missing_math/wiki) for more information!


This small module contains:

 - basic low frequency oscillator (lfo)
  - Arguments:
    - parent - could be anything
    - wave - 'triangle' or 'square' or 'saw'
    - attenuation - multiplies output
    - min - bottom value of wave
    - max - top value of wave
    - cycletime - crude implementation of frequency
  - Use:
    - call run() to advance to next frame of wave, typically in a pygame while loop
    - this will return the value for this frame, which can be assigned to control anything


 - basic insertion sort algorithm
  - Arguments:
    - array - the array to sort
  - Use:
    - sorts the array from lowest value to highest



 - basic clamp function
  - Arguments:
    - value - the value to clamp
    - min - lower bound
    - max - upper bound
  - Use:
    - clamps a value between the lower and upper bounds
