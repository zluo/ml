'''
Created on Feb 2, 2016

python -m unittest test_module1 test_module2

need to understand py deploy


@author: zluo
'''
import unittest
import numpy as np
from mylib.plots import *
from mylib.plots import _plot

class TestPlot(unittest.TestCase): 
    
    def test_pf(self):
       # a = np.random.rand(100)
        a = np.arange(0, 1, 0.01)
        b = np.sqrt(1 - a*a)  # a*a + b*b =1
        c = a*a  # a*a + b*b =1
        d = a*b
        e =d*c
        f=2*e
        g= a + b + c + d + e + f
        z = np.vstack((a, b, c, d, e, f, g))
        
        #pf(z)
        #scatter_features(z)
        _plot(a, c/b)
        _plot(a, a/b)
        
        
if __name__ == '__main__':
    unittest.main()