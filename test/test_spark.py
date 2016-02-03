'''
Created on Feb 3, 2016

@author: zluo
'''
from pyspark import SparkConf,SparkContext
import os
import numpy as np

sparkConf = SparkConf().setAppName('WordCounts').setMaster('local')
sc = SparkContext(conf = sparkConf)


a = np.arange(0, 1, 0.01)
b = np.sqrt(1 - a*a)  # a*a + b*b =1
c = a*a  # a*a + b*b =1
d = a*b
e =d*c
f=2*e
g= a + b + c + d + e + f
z = np.vstack((a, b, c, d, e, f, g))
        
rdd =sc.parallelize(z.T, 2)

print(rdd.take(2))