'''
Created on Feb 2, 2016

@author: zluo
'''
import matplotlib.pyplot as plt
'''
  m is a nynum array[[],[],[]]
'''
def plot_features(m): 
    print('-----------print features----------')
    len = m.shape[0]
    i = 0
    while i < len :
       li = premature(i, len, m)
       plot_scatter(i , li)
       i += 1
            
def premature(i, len, m): 
    li =[]
    j = i + 1
    while(j < len):
        li.append((m[i],m[j]))
        j += 1
    return li

def plot_scatter(index, li):
        i=index + 1
        for tup in li:
            #plt.scatter(tup[0], tup[1])
            plt.plot(tup[0], tup[1], label = 'F(' + str(index) +  ',' + str(i) + ')')
            i += 1
        plt.legend()
        plt.show()
        
        
           
    