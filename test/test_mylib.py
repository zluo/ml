'''
Created on Feb 2, 2016

python -m unittest test_module1 test_module2

need to understand py deploy


@author: zluo
'''
import unittest
import numpy as np
from mylib.plots import plot_features as pf

class TestPlot(unittest.TestCase): 
    
    def test_pf(self):
        a = np.random.rand(100)
        b = np.sqrt(1 - a*a)  # a*a + b*b =1
        c = np.vstack((a, b))
        pf(c)

if __name__ == '__main__':
    unittest.main()