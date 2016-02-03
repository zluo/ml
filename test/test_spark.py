'''
Created on Feb 3, 2016

@author: zluo
'''
from pyspark import SparkConf,SparkContext
import os

sparkConf = SparkConf().setAppName('WordCounts').setMaster('local')
sc = SparkContext(conf = sparkConf)

textFile =sc.parallelize([1,2], 2)

print (textFile.take(2))