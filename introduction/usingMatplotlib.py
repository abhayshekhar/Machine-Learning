import matplotlib.pyplot as plt
import numpy as np


'''--Generate a sequence of numbers range from -10 to 10 in steps of 100--'''
x=np.linspace(-10,10,100)
'''create a second array using sine'''
y=np.sin(x)
'''plot function makes a line chart of one array against another'''
plt.plot(x,y,marker='x')
plt.show()